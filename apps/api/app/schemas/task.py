from pydantic import BaseModel, ConfigDict


class TaskCreate(BaseModel):
    title: str
    description: str | None = None


class TaskRead(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool

    model_config = ConfigDict(from_attributes=True)