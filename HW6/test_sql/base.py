import pytest

from mysql_orm.builder import MySQLBuilder


class MysqlBase: 

    @pytest.fixture(scope='class')
    def create_table_count_request(self, mysql_orm_client):
        type(self).mysql = mysql_orm_client
        type(self).mysql_builder = MySQLBuilder(self.mysql)
        self.mysql.connect(db_created=True)
        self.mysql.create_table(table_name='count_request')
        self.mysql.connection.close()

    @pytest.fixture(scope='class')
    def create_table_request_types_count(self, mysql_orm_client):
        type(self).mysql = mysql_orm_client
        type(self).mysql_builder = MySQLBuilder(self.mysql)
        self.mysql.connect(db_created=True)
        self.mysql.create_table(table_name='request_types_count')
        self.mysql.connection.close()

    
    @pytest.fixture(scope='class')
    def create_table_most_frequent_requests(self, mysql_orm_client):
        type(self).mysql = mysql_orm_client
        type(self).mysql_builder = MySQLBuilder(self.mysql)
        self.mysql.connect(db_created=True)
        self.mysql.create_table(table_name='most_frequent_requests')
        self.mysql.connection.close()


    @pytest.fixture(scope='class')
    def create_table_largest_4xx_requests(self, mysql_orm_client):
        type(self).mysql = mysql_orm_client
        type(self).mysql_builder = MySQLBuilder(self.mysql)
        self.mysql.connect(db_created=True)
        self.mysql.create_table(table_name='largest_4xx_requests')
        self.mysql.connection.close()

    @pytest.fixture(scope='class')
    def create_table_users_with_5xx_requests(self, mysql_orm_client):
        type(self).mysql = mysql_orm_client
        type(self).mysql_builder = MySQLBuilder(self.mysql)
        self.mysql.connect(db_created=True)
        self.mysql.create_table(table_name='users_with_5xx_requests')
        self.mysql.connection.close()

    def get_count_records(self, model):
        self.mysql.session.commit() 
        count_records = self.mysql.session.query(model).count()
        return count_records