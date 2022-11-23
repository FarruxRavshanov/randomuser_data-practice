def get_all_numbers(data: dict) -> list[str]:
    '''get all phone numbers from users data
    
    Args:
        data (dict): users data.
        
    Returns:
        list: list of phone numbers.
    '''
    phone_numbers = []
    for phone_number in data['results']:
        phone_numbers.append(phone_number['phone'])
    return phone_numbers