from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker
from newbit import models


class Core:

    def __init__(self):
        self.set_db_engine('sqlite')
        self.build_db()

        Session = sessionmaker(bind=self.db_engine)
        self.db_session = Session()

    def set_db_engine(self, db_engine_choice):
        if db_engine_choice == 'sqlite':
            self.db_engine_type = db_engine_choice
            self.db_engine = create_engine('sqlite:///newbit.db', echo=False)

    def build_db(self):
        models.Base.metadata.create_all(self.db_engine, checkfirst=True)

    def add_news_request(self, topic: str):
        news_request = models.NewsRequest(topic=topic)
        self.db_session.add(news_request)
        self.db_session.commit()

    def add_news_information(self, news_request, headlines):
        news_request.is_processed = True
        news_request.information = [models.NewsInformation(headlines=headlines)]
        self.db_session.add(news_request)
        self.db_session.commit()

    @property
    def next_news_request(self):
        return self.db_session.query(models.NewsRequest).filter_by(is_processed=False).first()

    @property
    def news_request_list(self):
        return self.db_session.query(models.NewsRequest).all()

    def get_news_information(self, news_request_id):
        return self.db_session.query(models.NewsInformation).filter_by(news_request_id=news_request_id).first()
