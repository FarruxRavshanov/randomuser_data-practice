def get_all_streets(data: dict) -> list[str]:
    '''get all streets from users data
    
    Args:
        data (dict): users data.
        
    Returns:
        list: list of streets.
    '''
    streets = []
    for street in data['results']:
        streets.append(street['location']['street']['name'])
    return streets