from pydantic import BaseModel


class ImageShareBase(BaseModel):
    pass


class ImageShareCreate(ImageShareBase):
    shared_to_list: list


class ImageShare(ImageShareBase):
    id: int
    image_id: int
    shared_to: int

    class Config:
        orm_mode = True
