import json

def read_data(file_path: str) -> dict:
    '''read data from a file
    
    Args: 
        file_path (str): file path
        
    Returns:
        dict: dict data from file
    '''
    reading = open(file_path).read()
    dict_file = json.loads(reading)
    return dict_file