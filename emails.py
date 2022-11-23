def get_all_emails(data: dict) -> list[str]:
    '''get all emails from users data
    
    Args:
        data (dict): users data.
        
    Returns:
        list: list of emails.
    '''
    emails = []
    for email in data['results']:
        emails.append(email['email'])
    return emails