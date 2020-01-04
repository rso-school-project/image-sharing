import time

from typing import List
from fastapi import APIRouter, Depends, HTTPException
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



@router.put('/share/image/{image_id}', response_model=List[schemas.ImageShare])
def update_share(share: schemas.ImageShareCreate, image_id: int, db: Session = Depends(get_db)):
    return crud.update_share(db=db, share=share, image_id=image_id)


@router.delete('/share/image/{image_id}/user/{user_id}', response_model=schemas.ImageShare)
def delete_share(request: Request, image_id: int, user_id: int, db: Session = Depends(get_db)):
    db_share = crud.delete_share(db=db, image_id=image_id, user_id=user_id)
    if db_share is None:
        raise HTTPException(status_code=404, detail='Share not found')
    return db_share


@router.get('/share/image/{image_id}', response_model=List[schemas.ImageShare])
def get_share_by_image(image_id: int, db: Session = Depends(get_db)):
    return crud.get_share_by_image(db=db, image_id=image_id)


@router.get('/share/user/{user_id}', response_model=List[schemas.ImageShare])
def get_share_by_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_share_by_user(db=db, user_id=user_id)