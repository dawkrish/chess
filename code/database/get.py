from .connect import connect


def get(table, conditions, limit = 1):
    '''
    Get results from the selected table with specified conditions upto a given limit
    '''

    connection = connect()
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {table} WHERE {conditions} LIMIT {limit}")
    result = cursor.fetchall()

    return result

