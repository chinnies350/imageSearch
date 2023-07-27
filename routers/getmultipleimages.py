# from fastapi import FastAPI, Response
# from fastapi.routing import APIRouter
# from typing import List
# import requests
# from io import BytesIO
# from PIL import Image
# import schemas

# # app = FastAPI()
# router= APIRouter(prefix="/getmultipleimages",tags=['getmultipleimages'])

# @router.post("/images/")
# async def get_images(request:schemas.getimages):
#     images = []
#     for url in request.urls:
#         response = requests.get(url)
#         image_data = BytesIO(response.content)
#         img = Image.open(image_data)
#         images.append(img)
#     return images
#     # return Response(content=response.content, media_type="image/jpeg")