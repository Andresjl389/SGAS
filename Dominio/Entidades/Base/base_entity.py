import uuid
from typing import Optional
from sqlmodel import Column, DateTime, Field, SQLModel, func

class BaseEntity(SQLModel):
    id: Optional[uuid.UUID] = Field(primary_key=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.id:
            self.id = uuid.uuid4()