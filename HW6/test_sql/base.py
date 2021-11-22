import pytest

from mysql_orm.client import MySQLORMClient
from mysql_orm.builder import MySQLBuilder


class MysqlBase:

    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_orm_client):
        self.mysql: MySQLORMClient = mysql_orm_client
        self.mysql_builder: MySQLBuilder = MySQLBuilder(self.mysql)
        
        self.prepare()