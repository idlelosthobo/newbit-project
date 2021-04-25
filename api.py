from newbit.core import Core
from typing import Optional
from fastapi import FastAPI


app = FastAPI()
newbit = Core()


@app.get('/list/')
async def read_root():
    return newbit.news_request_list


@app.get('/add/{topic}')
async def read_item(topic: Optional[str] = None):
    newbit.add_news_request(topic)
    return {'status': 'success'}
