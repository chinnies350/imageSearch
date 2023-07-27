from fastapi.routing import APIRouter
import schemas
# from routers.config import engine
# from routers import Response
# from starlette.responses import Response
from fastapi import FastAPI, Response
from typing import Optional
from fastapi import Query
import json
import requests

router= APIRouter(prefix="/getimage",tags=['getimage'])

@router.get('')
async def get_image(url: str):
    try:
        # Fetch the image content
        response = requests.get(url)

        # Return the image content
        return Response(content=response.content, media_type="image/jpeg")
    except Exception as e:
        print("Exception Error",str(e))
        return{"statusCode":0,"response":"Server Error"}
    
