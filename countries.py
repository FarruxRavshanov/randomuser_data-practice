def get_all_countries(data: dict) -> list[str]:
    '''get all ages from users data
    
    Args:
        data (dict): users data.
        
    Returns:
        list: list of countries.
    '''
    countries = []
    for country in data['results']:
        countries.append(country['location']['country'])
    return countries