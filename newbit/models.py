from sqlalchemy import Column, String, Text, Integer, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class NewsRequest(Base):
    __tablename__ = 'news_request'

    id = Column(Integer, primary_key=True)

    topic = Column(String)
    is_processed = Column(Boolean, default=False)
    information = relationship('NewsInformation', backref='news_request')

    def __repr__(self):
        return f'Topic: {self.topic}'


class NewsInformation(Base):
    __tablename__ = 'news_information'

    id = Column(Integer, primary_key=True)
    news_request_id = Column(Integer, ForeignKey('news_request.id'))

    headlines = Column(String)