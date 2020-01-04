from sqlalchemy import Column, Integer, String, ARRAY

from image_sharing.database import Base


class ImageShare(Base):
    __tablename__ = 'image_share'

    id = Column(Integer, primary_key=True, index=True)
    image_id = Column(Integer)
    shared_to = Column(Integer)
