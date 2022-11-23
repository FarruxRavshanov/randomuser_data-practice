def get_all_pictures_url(data: dict) -> list[str]:
    '''get all pictures_url from users data
    
    Args:
        data (dict): users data.
        
    Returns:
        list: list of pictures_url.
    '''
    pictures = []
    for picture in data['results']:
        pictures.append(picture['picture']['medium'])
    return pictures