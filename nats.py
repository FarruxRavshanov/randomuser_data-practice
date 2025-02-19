def get_all_nats(data: dict) -> list[str]:
    '''get all nats from users data
    
    Args:
        data (dict): users data.
        
    Returns:
        list: list of nats.
    '''
    nats = []
    for nat in data['results']:
        nats.append(nat['nat'])
    return nats