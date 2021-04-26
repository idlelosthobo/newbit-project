from newbit.core import Core
from typing import Optional
from fastapi import FastAPI


app = FastAPI()
newbit = Core()


@app.get('/list_request/')
async def read_root():
    return newbit.news_request_list


@app.get('/request/{request_id}')
async def read_item(request_id: Optional[int] = None):
    headlines = list()
    for headline in str(newbit.get_news_information(request_id).headlines).split('|'):
        if headline != '':
            headlines.append(headline)
    return {'headlines': headlines}


@app.get('/add_request/{topic}')
async def read_item(topic: Optional[str] = None):
    newbit.add_news_request(topic)
    return {'status': 'success'}
