from pydantic import BaseModel


class TaskCreate(BaseModel):

    project_id: int

    title: str

    description: str

    assignee: str


class TaskResponse(BaseModel):

    id: int

    title: str

    status: str

    assignee: str

    class Config:
        from_attributes = True