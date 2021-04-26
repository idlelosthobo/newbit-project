from newbit.utils import get_news
from newbit.core import Core
from time import sleep


newbit = Core()

while True:

    next_news_request = newbit.next_news_request

    if next_news_request:
        newbit.add_news_information(next_news_request, get_news(next_news_request.topic))

    sleep(1)