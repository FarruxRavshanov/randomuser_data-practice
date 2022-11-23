def get_all_cities(data: dict) -> list[str]:
    '''get all ages from users data
    
    Args:
        data (dict): users data.
        
    Returns:
        list: list of cities.
    '''
    city = []
    for cities in data['results']:
        city.append(cities['location']['city'])
    return city