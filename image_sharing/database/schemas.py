from pydantic import BaseModel


class ImageShareBase(BaseModel):
    owner_id: int
    shared_to: list


class ImageShareCreate(ImageShareBase):
    pass


class ImageShare(ImageShareBase):
    id: int

    class Config:
        orm_mode = True
