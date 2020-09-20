from fastapi import FastAPI
import uvicorn

import requests
from pydantic import BaseModel, HttpUrl

from bs4 import BeautifulSoup

app = FastAPI()


class URL(BaseModel):
    url: HttpUrl

@app.get('/')
def index():
    return {'message': "Hello Everyone ﾟ･✿ヾ╲(｡◕‿◕｡)╱✿･ﾟ"}


@app.get('/about')
def about():
    return {'about': "Version 1"}


@app.get('/user')
def about():
    return {'user': "Test User 1"}


@app.post('/scrape_tags')
async def scrape_tags(url: URL):
    page = requests.get(str(url.url))
    soup = BeautifulSoup(page.text, 'html.parser')


    def get_keywords():

        if soup.head.find('meta', attrs={'name': 'keywords'}):
            keywords = soup.head.find('meta', attrs={'name': 'keywords'}).get('content')
        else:
            keywords = None

        return keywords

    def get_title():

        if soup.head.find('title'):
            return soup.head.find('title').text
        else:
            return "Title Tag was not found."


    def get_description():

        if soup.head.find('meta', attrs={'name': 'description'}):
            main_description = soup.head.find('meta', attrs={'name': 'description'}).get('content')
        else:
            main_description = None

        if soup.find('meta', property="og:description"):
            og_description = soup.find('meta', property="og:description").get('content')
        else:
            og_description = None

        return main_description or og_description or None


    def get_image():

        if soup.find('meta', property="og:image"):
            og_image = soup.find('meta', property="og:image").get('content')
        else:
            og_image = None

        return og_image

    return{
        "message_1": "Taking a break from Django (ノಠ益ಠ)ノ彡┻━┻",
        "message_2": "Learning FastAPI (づ￣ ³￣)づ",
        "message_3": "Web Scraping using BS4 ლ(｡-﹏-｡ ლ)",
        "title": get_title(),
        "description": get_description(),
        "keywords": get_keywords(),
        "image": get_image(),
    }
