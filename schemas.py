from pydantic import BaseModel
from datetime import datetime,date,time
from typing import Dict, Optional,List
from fastapi import Query
from xmlrpc.client import boolean


class getimages(BaseModel):
    urls:List
    
# class getmultipleimages(BaseModel):
#     multipleimages:Optional[List[getimages]] = None
   