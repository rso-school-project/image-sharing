import time

from typing import List
from fastapi import APIRouter, Depends
from starlette.requests import Request
from func_timeout import func_set_timeout
from sqlalchemy.orm import Session

from image_sharing import settings
from image_sharing.utils import fallback
from image_sharing.database import crud, models, schemas, get_db, engine

try:
    models.Base.metadata.create_all(bind=engine, checkfirst=True)
except:
    pass

router = APIRouter()


@router.post('/share')
async def test_configs():
    return {}
