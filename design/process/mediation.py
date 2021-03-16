class Interventions:
    '''
    Action Interventions: 
    1.     "Operations team, continue working on and refining your current plan." 
    2.     "Operations team, try evaluating and/or submitting your plan."  
    3.     "Operations team, try running the path-planning agent."  
    4.      "Drone design team, continue working on and refining your current drone design."
    5.     "Drone design team, try evaluating and/or submitting your design." 
    6.     "Drone design team, try running the drone design agent." 
    Communication Interventions:
    7.     "Team, try focusing more on the design parameters, requirements, and  goals (e.g., cost, capacity, speed, budget, weight, etc.)
    8.     "Team, try focusing more on your strategy (e.g., optimizing, adding/removing, increasing/decreasing, balancing, etc.)." 
    9.      "Team, try to ensure your communication is more aligned with each other.
    10.   "Operations team, try communicating with each other more
    11.  "Drone design team, try communicating with each other more."  
    12.   "Problem manager, try communicating with your team more."  
    No Intervention Needed: 
    13.  No intervention.  

    '''

    ACTION_1 = 'Ops planners, why don’t you continue working on and refining your plans a bit more.'
    ACTION_2 = 'Hey operations team, try evaluating and/or submitting your plan and start fresh.'
    ACTION_3 = 'Hi operations team, try running the path-planning agent to help.'
    ACTION_4 = 'Drone designers, why don’t you continue working on and refining your drone designs a bit more.'
    ACTION_5 = 'Hey drone design team, try evaluating and/or submitting your design and start fresh.'
    ACTION_6 = 'Hi drone design team, try running the drone design agent to help.'
    COMMUNICATION_1 = 'Team, try focusing more on some of the design parameters and goals of the problem, such as: cost, capacity, speed, budget, weight, etc.'
    COMMUNICATION_2 = 'Team, try focusing more on your problem-solving strategies; try optimizing, adding/removing, increasing/decreasing components.'
    COMMUNICATION_3 = 'Hi team, why don’t you all try aligning your communication with each other more.'
    COMMUNICATION_4 = 'Ops team, please try talking with each other more.'
    COMMUNICATION_5 = 'Drone designers, please try talking with each other more.'
    COMMUNICATION_6 = 'Hi problem manager, please try talking with your team more.'
    NO_INTERVENTION = 'No intervention.'

    def add_intervention_constants(context):
        context['ACTION_1'] = Interventions.ACTION_1
        context['ACTION_2'] = Interventions.ACTION_2
        context['ACTION_3'] = Interventions.ACTION_3
        context['ACTION_4'] = Interventions.ACTION_4
        context['ACTION_5'] = Interventions.ACTION_5
        context['ACTION_6'] = Interventions.ACTION_6
        context['COMMUNICATION_1'] = Interventions.COMMUNICATION_1
        context['COMMUNICATION_2'] = Interventions.COMMUNICATION_2
        context['COMMUNICATION_3'] = Interventions.COMMUNICATION_3
        context['COMMUNICATION_4'] = Interventions.COMMUNICATION_4
        context['COMMUNICATION_5'] = Interventions.COMMUNICATION_5
        context['COMMUNICATION_6'] = Interventions.COMMUNICATION_6
        context['NO_INTERVENTION'] = Interventions.NO_INTERVENTION
        return context