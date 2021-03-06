from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CountRequest(Base):
    __tablename__ = "count_request"
    __table_args__ = {'mysql_charset': 'utf8'}

    count = Column(Integer, nullable=False, primary_key=True)
    
    def __repr__(self):
        return f"<CountRequest(count='{self.count}'>"

class RequestTypeCount(Base):
    __tablename__ = 'request_types_count'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    req_type = Column(String(300), nullable=False)
    count = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<RequestTypeCount("\
            f"id='{self.id}'"\
            f"req_type='{self.req_type}'," \
            f"count='{self.count}')>"

class MostFrequentRequest(Base):
    __tablename__ = 'most_frequent_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(300), nullable=False)
    count = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<MostFrequentRequest(id='{self.id}', url='{self.url}', count='{self.count}')>"

class Largest4xxRequest(Base):
    __tablename__ = 'largest_4xx_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(300), nullable=False)
    size = Column(Integer, nullable=False)
    ip = Column(String(30), nullable=False)

    def __repr__(self):
        return f"<Largest4xxRequest(id='{self.id}', url='{self.url}', size='{self.size}', IP='{self.ip}')>"


class UserWith5xxRequests(Base):
    __tablename__ = 'users_with_5xx_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(30), nullable=False)
    requests_number = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<UserWith5xxRequests(id='{self.id}', IP='{self.ip}', requests_number='{self.requests_number}')>"
