def get_all_ages(data: dict) -> list[int]:
    '''get all ages from users data
    
    Args:
        data (dict): users data.
        
    Returns:
        list: list of ages.
    '''
    ages = []
    for user in data['results']:
        ages.append(user['dob']['age'])
    return ages

def get_the_oldest_age(ages: list[int]) -> int:
    '''get the oldest age from ages
    
    Args:
        ages (list): list of ages.
        
    Returns:
        int: the oldest age.
    '''
    d = 0
    for i in ages:
        if d < i:
            d = i
    return d

def get_the_youngest_age(ages: list[int]) -> int:
    '''get the youngest age from ages
    
    Args:
        ages (list): list of ages.
        
    Returns:
        int: the youngest age.
    '''
    mn = ages[0]
    for i in ages:
        if i < mn:
            mn = i
    return mn
            