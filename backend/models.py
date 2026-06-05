from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    summary = Column(Text, nullable=False)
    cover = Column(String(500), nullable=True)
    tags = Column(String(500), default="")
    views = Column(Integer, default=0)
    likes = Column(Integer, default=0)
    comments = Column(Integer, default=0)
    date = Column(String(20), default="")
    read_time = Column(String(20), default="")
    content = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)


class Photo(Base):
    __tablename__ = "photos"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(500), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(String(500), default="")
    likes = Column(Integer, default=0)
    comments = Column(Integer, default=0)
    date = Column(String(20), default="")
    created_at = Column(DateTime, default=datetime.utcnow)


class WorkspaceItem(Base):
    __tablename__ = "workspace_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    type = Column(String(20), default="file")
    updated_at = Column(String(20), default="")
    size = Column(String(20), nullable=True)
    parent_id = Column(Integer, ForeignKey("workspace_items.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    children = relationship("WorkspaceItem", backref="parent", remote_side=[id])


class TimelineEvent(Base):
    __tablename__ = "timeline_events"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String(20), default="")
    title = Column(String(200), nullable=False)
    description = Column(Text, default="")
    type = Column(String(50), default="article")
    created_at = Column(DateTime, default=datetime.utcnow)


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    tech_stack = Column(String(500), default="")
    stars = Column(Integer, default=0)
    forks = Column(Integer, default=0)
    url = Column(String(500), default="")
    demo_url = Column(String(500), nullable=True)
    status = Column(String(50), default="active")
    created_at = Column(DateTime, default=datetime.utcnow)


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    completed = Column(Boolean, default=False)
    priority = Column(String(20), default="medium")
    due_date = Column(String(20), nullable=True)
    category = Column(String(50), default="其他")
    created_at = Column(DateTime, default=datetime.utcnow)


class Requirement(Base):
    __tablename__ = "requirements"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False)
    status = Column(String(50), default="pending")
    priority = Column(String(20), default="medium")
    category = Column(String(50), default="")
    date = Column(String(20), default="")
    tech_stack = Column(String(500), default="")
    difficulty = Column(String(50), default="")
    description = Column(Text, default="")
    tags = Column(String(500), default="")
    created_at = Column(DateTime, default=datetime.utcnow)


class Friend(Base):
    __tablename__ = "friends"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    avatar = Column(String(10), default="")
    description = Column(String(500), default="")
    url = Column(String(500), default="")
    tags = Column(String(500), default="")
    created_at = Column(DateTime, default=datetime.utcnow)


class TechCategory(Base):
    __tablename__ = "tech_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    items = relationship("TechItem", back_populates="category", cascade="all, delete-orphan")


class TechItem(Base):
    __tablename__ = "tech_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    icon = Column(String(20), default="")
    proficiency = Column(Integer, default=0)
    description = Column(String(500), default="")
    category_id = Column(Integer, ForeignKey("tech_categories.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    category = relationship("TechCategory", back_populates="items")


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(500), nullable=False)
    time_text = Column(String(50), default="")
    type = Column(String(50), default="")
    created_at = Column(DateTime, default=datetime.utcnow)
