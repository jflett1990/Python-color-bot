def choose_developer(desired_lift, hair_condition):
    # Determine the developer strength based on the desired level of lift
    if desired_lift <= 2:
        developer = '10vol'
    elif desired_lift == 2:
        developer = '20vol'
    elif desired_lift == 3:
        developer = '30vol'
    elif desired_lift >= 4:
        developer = '40vol'
    
    # If the hair condition is damaged, do not use developer over 30vol
    if hair_condition == 'damaged' and developer == '40vol':
        developer = '30vol'
    
    return developer
