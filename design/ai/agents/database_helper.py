import json
from datetime import datetime, timedelta

from exper.models import UserPosition, GroupPosition, Session, SessionTeam, Group
from repo.models import Scenario, Vehicle, Plan, Customer, PathCustomer, Path, Warehouse, CustomerScenario, DataLog
from repo.serializers import ScenarioSerializer
from django.db.models import Q

from chat.messaging import new_vehicle_message, new_plan_message, new_scenario_message

# helper for agents to load and save database objects
class DatabaseHelper:

    def __init__(self, session):

        self.session = session                      # save the session object of the experimental session
        self.user_primary_groups = {}               # dictionary that saves the primary user group to a user name (to save objects)
        self.user_roles = {}                        # dictionary that save the user roles to a user name
        self.user_positions = {}                    # dictionary that saves the user positions to a user name (to save data logs)
        self.first_simulation_time_date = None      # save the first event time to save to save datalog with the correct time when running in batch mode

        self.st = SessionTeam.objects.filter(Q(session=self.session)).first()       # get the session team
        ups = UserPosition.objects.filter(Q(session=self.st.session))               # get the user positions of the session
        for u in ups:                                                               # for each user position
            self.user_roles[u.user.username] = u.position.role.name                 # get the role
            self.user_positions[u.user.username] = u                                # store the user position based on the user name
            # for each user, find multile groups itis associated with
            groups = GroupPosition.objects.filter(Q(position=u.position)&Q(position__structure=self.st.session.structure))  # get all groups of the user position
            for gp in groups:
                if gp.primary:
                    self.user_primary_groups[u.user.username] = gp.group            # save objects should use the user positions primary group

    # gets the user roles (ex. designer, ops planner, ...)
    def get_user_roles(self):
        return self.user_roles

    # sets the user name
    def set_user_name(self, user_name):
        self.user_name = user_name

    # query vehicles for a user
    def query_vehicles(self):
        return Vehicle.objects.filter(session=self.session, group=self.user_primary_groups[self.user_name])

    # query vehicles for a user with a tag and configuration
    def query_vehicles_with_tag(self, vehicle_tag, config):
        return Vehicle.objects.filter(session=self.session, group=self.user_primary_groups[self.user_name], tag=vehicle_tag, config=config)

    # submit a vehicle to the database
    def submit_vehicle_db(self, tag, config, range, capacity, cost, velocity):

        # check for a vehicle with a similar tag and configuration
        vehicle_query = self.query_vehicles_with_tag(tag, config)

        # if no instances return
        if len(vehicle_query) == 0:

            # create a Vehicle object and save
            v = Vehicle()
            v.group = self.user_primary_groups[self.user_name]
            v.session = self.session
            v.tag = tag
            v.config = config
            v.range = range
            v.payload = capacity
            v.cost = cost
            v.velocity = velocity
            v.save()

            # for real time agents notify user of a new vehicle
            new_vehicle_message(self.user_primary_groups[self.user_name], self.session, v.tag)

            return v

        else:
            print(tag + ": already in the database")

        return None

    # gets the latest scenario for the group
    def get_scenario(self):

        # query for a scenarios
        scenarios = Scenario.objects.filter(Q(group=self.user_primary_groups[self.user_name])&Q(session=self.session))
        if scenarios.exists():
            scenario = scenarios.order_by('version').last()
        else:
            # this will create a new scenario
            warehouse = Warehouse.objects.filter(Q(session=self.session)).first()
            scenario = Scenario.objects.create(tag='Initial Scenario', warehouse=warehouse, group=self.user_primary_groups[self.user_name], session = self.session)
            # also need to select all of the customer's in this market
            market = self.session.market
            customers = Customer.objects.filter(market=market)
            for customer in customers:
                # this may be a little slow - keep an eye on it
                # may want to create a lsit of objects and then use bulk_create
                CustomerScenario.objects.create(customer=customer, scenario=scenario, selected=True)

        # convert to a json object by deserailizing to a string and then to a json object
        # I had issues with the serializer.data so I converted to string and then back to json, look into this
        serializer = ScenarioSerializer(scenario)
        scenario_str = json.dumps(serializer.data)
        scenario_obj = json.loads(scenario_str)

        return scenario_obj

    # submit a scenario to the database
    def submit_scenario(self, selected_nodes):

        # get current scenarios, if any exist, get the last version number
        scenarios = Scenario.objects.filter(Q(group=self.user_primary_groups[self.user_name])&Q(session=self.session))
        version = 1
        if scenarios.exists():
            version = scenarios.order_by('version').last().version + 1

        # get the session
        warehouse = Warehouse.objects.filter(Q(group=self.user_primary_groups[self.user_name])&Q(session=self.session)).first()
        scenario = Scenario.objects.create(tag='Scenario', version=version, warehouse=warehouse, group=self.user_primary_groups[self.user_name], session = self.session)
        # also need to select all of the customer's in this market
        market = self.session.market
        customers = Customer.objects.filter(market=market)
        for customer in customers:
            # this may be a little slow - keep an eye on it
            # may want to create a list of objects and then use bulk_create
            selected_customer = True
            key_test = str(customer.address.x) + "|" + str(customer.address.z)
            if key_test in selected_nodes:
                if selected_nodes[key_test] == 'False':
                    selected_customer = False;
            CustomerScenario.objects.create(customer=customer, scenario=scenario, selected=selected_customer)

        # return a string version of the scenario for datalog
        serializer = ScenarioSerializer(scenario)
        scenario_str = json.dumps(serializer.data)

        # for real time agents notify user of a new scenario
        new_scenario_message(self.user_primary_groups[self.user_name], self.session)

        return scenario_str

    # query plans by session
    def query_plans(self):
        return Plan.objects.filter(session=self.session)

    # plan submit
    def plan_submit(self, plan_json):

        # get the latest session object
        scenarios = Scenario.objects.filter(Q(session=self.session))
        scenario = scenarios.order_by('version').last()
        # first step is to create a plan object
        plan = Plan.objects.create(tag=plan_json['tag'], scenario=scenario, group=self.user_primary_groups[self.user_name], session=self.session)
        # next is to create the path objects
        for p in plan_json['paths']:
            vehicle = Vehicle.objects.get(id=p.get('vehicle')['id'])
            path = Path.objects.create(plan=plan, vehicle=vehicle, warehouse=scenario.warehouse, leavetime=p.get('leavetime',0.0),
                returntime=p.get('returntime',0.0))
            # next we need to define the customers in the path
            customers = p.get('customers')
            stop=1
            for c in customers:
                customer = Customer.objects.get(id=c['id'])
                PathCustomer.objects.create(path=path, customer=customer, stop=stop)
                stop=stop+1

        # for real time agents notify user of a new scenario
        new_plan_message(self.user_primary_groups[self.user_name], self.session, plan.tag)

        return plan

    # submits a datalog
    def submit_data_log(self, user_name, action, real_time, time_min):

        # if the user name is saved in the user positions (# a team agent is not in the user positions, so this is why the check is here)
        if user_name in self.user_positions:

            dl = DataLog()                                      # create a new Datalog object
            dl.session = self.session                           # assign the session to the DataLog
            dl.user = self.user_positions[user_name].user       # assign a user to the datalog
            dl.action = action                                  # add the action
            if not real_time and self.first_simulation_time_date is None:               # if a team simulation, store the time of the first event
                self.first_simulation_time_date = datetime.now()
            if not real_time:                                                           # set the time of the event based on the minutes value
                dl.time=self.first_simulation_time_date + timedelta(minutes=time_min)
            dl.type = "digital_twin"                                                    # save the type of the Datalog as digital twin for now
            dl.save()