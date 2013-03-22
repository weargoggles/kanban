from eveapi import EVEAPIConnection

connection = EVEAPIConnection()

def get_connection():
    """returns the current connection"""
    return connection

