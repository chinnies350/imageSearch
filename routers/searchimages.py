from fastapi.routing import APIRouter
# import schemas
# from routers.config import engine
from routers import Response
from typing import Optional
from fastapi import Query
import json
from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests

router=APIRouter(prefix="/searchImages",tags=['searchImages'])

@router.get('')
def getimages(query:Optional[str]=Query(None)):
    try:
        url = f"https://www.google.com/search?q={query}&source=lnms&tbm=isch"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        image_links = []
        for img in soup.find_all("img"):
            if "src" in img.attrs:
                image_link = img.attrs["src"]
                if "googlelogo" not in image_link:
                    image_links.append(image_link)
        return {"statusCode":1,"image_links": image_links}
    except Exception as e:
        print("Exception Error",str(e))
        return{"statusCode":0,"response":"Server Error"}
    

