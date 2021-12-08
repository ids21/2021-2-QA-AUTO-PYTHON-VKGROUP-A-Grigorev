import pytest 

from mysql_orm.client import MySQLORMClient



def pytest_configure(config):
    mysql_orm_client = MySQLORMClient(user='root', password='pass', db_name='TEST_SQL')
    if not hasattr(config, 'workerinput'):
        mysql_orm_client.recreate_db()
    # mysql_orm_client.connect(db_created=True) 
    # if not hasattr(config, 'workerinput'):
    #     mysql_orm_client.create_table(table_name='count_request')
    #     mysql_orm_client.create_table(table_name='request_types_count')
    #     mysql_orm_client.create_table(table_name='most_frequent_requests')
    #     mysql_orm_client.create_table(table_name='largest_4xx_requests')
    #     mysql_orm_client.create_table(table_name='users_with_5xx_requests')
    #     mysql_orm_client.connection.close()
        
    config.mysql_orm_client = mysql_orm_client

@pytest.fixture(scope='session')
def mysql_orm_client(request) -> MySQLORMClient:
    client = request.config.mysql_orm_client
    yield client
    client.connection.close()