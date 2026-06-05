from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ArticleBase(BaseModel):
    title: str
    summary: str
    cover: Optional[str] = None
    tags: str = ""
    views: int = 0
    likes: int = 0
    comments: int = 0
    date: str = ""
    read_time: str = ""
    content: str = ""


class ArticleCreate(ArticleBase):
    pass


class ArticleUpdate(BaseModel):
    title: Optional[str] = None
    summary: Optional[str] = None
    cover: Optional[str] = None
    tags: Optional[str] = None
    views: Optional[int] = None
    likes: Optional[int] = None
    comments: Optional[int] = None
    date: Optional[str] = None
    read_time: Optional[str] = None
    content: Optional[str] = None


class Article(ArticleBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class PhotoBase(BaseModel):
    url: str
    title: str
    description: str = ""
    likes: int = 0
    comments: int = 0
    date: str = ""


class PhotoCreate(PhotoBase):
    pass


class PhotoUpdate(BaseModel):
    url: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    likes: Optional[int] = None
    comments: Optional[int] = None
    date: Optional[str] = None


class Photo(PhotoBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class WorkspaceItemBase(BaseModel):
    name: str
    type: str = "file"
    updated_at: str = ""
    size: Optional[str] = None
    parent_id: Optional[int] = None


class WorkspaceItemCreate(WorkspaceItemBase):
    pass


class WorkspaceItem(WorkspaceItemBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class TimelineEventBase(BaseModel):
    date: str = ""
    title: str
    description: str = ""
    type: str = "article"


class TimelineEventCreate(TimelineEventBase):
    pass


class TimelineEventUpdate(BaseModel):
    date: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None


class TimelineEvent(TimelineEventBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ProjectBase(BaseModel):
    name: str
    description: str
    tech_stack: str = ""
    stars: int = 0
    forks: int = 0
    url: str = ""
    demo_url: Optional[str] = None
    status: str = "active"


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    tech_stack: Optional[str] = None
    stars: Optional[int] = None
    forks: Optional[int] = None
    url: Optional[str] = None
    demo_url: Optional[str] = None
    status: Optional[str] = None


class Project(ProjectBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class TodoBase(BaseModel):
    title: str
    completed: bool = False
    priority: str = "medium"
    due_date: Optional[str] = None
    category: str = "其他"


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None
    priority: Optional[str] = None
    due_date: Optional[str] = None
    category: Optional[str] = None


class Todo(TodoBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class RequirementBase(BaseModel):
    title: str
    status: str = "pending"
    priority: str = "medium"
    category: str = ""
    date: str = ""
    tech_stack: str = ""
    difficulty: str = ""
    description: str = ""
    tags: str = ""


class RequirementCreate(RequirementBase):
    pass


class RequirementUpdate(BaseModel):
    title: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    category: Optional[str] = None
    date: Optional[str] = None
    tech_stack: Optional[str] = None
    difficulty: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[str] = None


class Requirement(RequirementBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class FriendBase(BaseModel):
    name: str
    avatar: str = ""
    description: str = ""
    url: str = ""
    tags: str = ""


class FriendCreate(FriendBase):
    pass


class FriendUpdate(BaseModel):
    name: Optional[str] = None
    avatar: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    tags: Optional[str] = None


class Friend(FriendBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class TechItemBase(BaseModel):
    name: str
    icon: str = ""
    proficiency: int = 0
    description: str = ""


class TechItemCreate(TechItemBase):
    pass


class TechItemUpdate(BaseModel):
    name: Optional[str] = None
    icon: Optional[str] = None
    proficiency: Optional[int] = None
    description: Optional[str] = None


class TechItem(TechItemBase):
    id: int
    category_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class TechCategoryBase(BaseModel):
    name: str


class TechCategoryCreate(TechCategoryBase):
    pass


class TechCategory(TechCategoryBase):
    id: int
    items: List[TechItem] = []
    created_at: datetime

    class Config:
        from_attributes = True


class ActivityBase(BaseModel):
    content: str
    time_text: str = ""
    type: str = ""


class ActivityCreate(ActivityBase):
    pass


class Activity(ActivityBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
