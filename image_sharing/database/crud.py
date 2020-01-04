from sqlalchemy.orm import Session

from . import models, schemas

'''
def get_comments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Comments).offset(skip).limit(limit).all()


def get_comments_by_image(db: Session, image_id: int):
    return db.query(models.Comments).filter(models.Comments.image_id == image_id).all()

'''
def update_share(db: Session, share: schemas.ImageShareCreate, image_id: int):
    db.query(models.ImageShare).filter(models.ImageShare.image_id == image_id).delete()
    db.commit()

    list_shares = []

    for shared_to in share.shared_to_list:
        db_share = models.ImageShare(image_id=image_id, shared_to=shared_to)
        db.add(db_share)
        db.commit()
        db.refresh(db_share)
        list_shares.append(db_share)

    return list_shares


def delete_share(db: Session, image_id: int, user_id: int):
    db_share = db.query(models.ImageShare).filter(models.ImageShare.image_id == image_id).filter(models.ImageShare.shared_to == user_id).first()
    if db_share:
        db.delete(db_share)
        db.commit()
    return db_share


def get_share_by_image(db: Session, image_id: int):
    db_share = db.query(models.ImageShare).filter(models.ImageShare.image_id == image_id).all()
    return db_share


def get_share_by_user(db: Session, user_id: int):
    db_share = db.query(models.ImageShare).filter(models.ImageShare.shared_to == user_id).all()
    return db_share