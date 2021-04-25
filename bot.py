from newbit.utils import get_news
from newbit.core import Core


newbit = Core()

print(newbit.news_request_list)

next_topic = newbit.next_news_request.topic

if next_topic:
    print(next_topic)
    get_news(next_topic)