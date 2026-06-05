from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional

import models, schemas, database
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Blog API is running"}


# ==================== Articles ====================
@app.get("/api/articles", response_model=List[schemas.Article])
def get_articles(db: Session = Depends(get_db)):
    return db.query(models.Article).order_by(models.Article.id.desc()).all()


@app.get("/api/articles/{article_id}", response_model=schemas.Article)
def get_article(article_id: int, db: Session = Depends(get_db)):
    article = db.query(models.Article).filter(models.Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article


@app.post("/api/articles", response_model=schemas.Article)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    db_article = models.Article(**article.model_dump())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


@app.put("/api/articles/{article_id}", response_model=schemas.Article)
def update_article(article_id: int, article: schemas.ArticleUpdate, db: Session = Depends(get_db)):
    db_article = db.query(models.Article).filter(models.Article.id == article_id).first()
    if not db_article:
        raise HTTPException(status_code=404, detail="Article not found")
    for key, value in article.model_dump(exclude_unset=True).items():
        setattr(db_article, key, value)
    db.commit()
    db.refresh(db_article)
    return db_article


@app.delete("/api/articles/{article_id}")
def delete_article(article_id: int, db: Session = Depends(get_db)):
    db_article = db.query(models.Article).filter(models.Article.id == article_id).first()
    if not db_article:
        raise HTTPException(status_code=404, detail="Article not found")
    db.delete(db_article)
    db.commit()
    return {"message": "Article deleted"}


# ==================== Photos ====================
@app.get("/api/photos", response_model=List[schemas.Photo])
def get_photos(db: Session = Depends(get_db)):
    return db.query(models.Photo).order_by(models.Photo.id.desc()).all()


@app.post("/api/photos", response_model=schemas.Photo)
def create_photo(photo: schemas.PhotoCreate, db: Session = Depends(get_db)):
    db_photo = models.Photo(**photo.model_dump())
    db.add(db_photo)
    db.commit()
    db.refresh(db_photo)
    return db_photo


@app.put("/api/photos/{photo_id}", response_model=schemas.Photo)
def update_photo(photo_id: int, photo: schemas.PhotoUpdate, db: Session = Depends(get_db)):
    db_photo = db.query(models.Photo).filter(models.Photo.id == photo_id).first()
    if not db_photo:
        raise HTTPException(status_code=404, detail="Photo not found")
    for key, value in photo.model_dump(exclude_unset=True).items():
        setattr(db_photo, key, value)
    db.commit()
    db.refresh(db_photo)
    return db_photo


@app.delete("/api/photos/{photo_id}")
def delete_photo(photo_id: int, db: Session = Depends(get_db)):
    db_photo = db.query(models.Photo).filter(models.Photo.id == photo_id).first()
    if not db_photo:
        raise HTTPException(status_code=404, detail="Photo not found")
    db.delete(db_photo)
    db.commit()
    return {"message": "Photo deleted"}


# ==================== Workspace Items ====================
@app.get("/api/workspace", response_model=List[schemas.WorkspaceItem])
def get_workspace_items(parent_id: Optional[int] = None, db: Session = Depends(get_db)):
    query = db.query(models.WorkspaceItem)
    if parent_id is not None:
        query = query.filter(models.WorkspaceItem.parent_id == parent_id)
    else:
        query = query.filter(models.WorkspaceItem.parent_id.is_(None))
    return query.order_by(models.WorkspaceItem.type.desc(), models.WorkspaceItem.id).all()


@app.post("/api/workspace", response_model=schemas.WorkspaceItem)
def create_workspace_item(item: schemas.WorkspaceItemCreate, db: Session = Depends(get_db)):
    db_item = models.WorkspaceItem(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.delete("/api/workspace/{item_id}")
def delete_workspace_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.WorkspaceItem).filter(models.WorkspaceItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted"}


# ==================== Timeline ====================
@app.get("/api/timeline", response_model=List[schemas.TimelineEvent])
def get_timeline(db: Session = Depends(get_db)):
    return db.query(models.TimelineEvent).order_by(models.TimelineEvent.id.desc()).all()


@app.post("/api/timeline", response_model=schemas.TimelineEvent)
def create_timeline_event(event: schemas.TimelineEventCreate, db: Session = Depends(get_db)):
    db_event = models.TimelineEvent(**event.model_dump())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


@app.put("/api/timeline/{event_id}", response_model=schemas.TimelineEvent)
def update_timeline_event(event_id: int, event: schemas.TimelineEventUpdate, db: Session = Depends(get_db)):
    db_event = db.query(models.TimelineEvent).filter(models.TimelineEvent.id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    for key, value in event.model_dump(exclude_unset=True).items():
        setattr(db_event, key, value)
    db.commit()
    db.refresh(db_event)
    return db_event


@app.delete("/api/timeline/{event_id}")
def delete_timeline_event(event_id: int, db: Session = Depends(get_db)):
    db_event = db.query(models.TimelineEvent).filter(models.TimelineEvent.id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(db_event)
    db.commit()
    return {"message": "Event deleted"}


# ==================== Projects ====================
@app.get("/api/projects", response_model=List[schemas.Project])
def get_projects(db: Session = Depends(get_db)):
    return db.query(models.Project).order_by(models.Project.id.desc()).all()


@app.post("/api/projects", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = models.Project(**project.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


@app.put("/api/projects/{project_id}", response_model=schemas.Project)
def update_project(project_id: int, project: schemas.ProjectUpdate, db: Session = Depends(get_db)):
    db_project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    for key, value in project.model_dump(exclude_unset=True).items():
        setattr(db_project, key, value)
    db.commit()
    db.refresh(db_project)
    return db_project


@app.delete("/api/projects/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    db_project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(db_project)
    db.commit()
    return {"message": "Project deleted"}


# ==================== Todos ====================
@app.get("/api/todos", response_model=List[schemas.Todo])
def get_todos(filter: Optional[str] = Query(None), db: Session = Depends(get_db)):
    query = db.query(models.Todo)
    if filter == "active":
        query = query.filter(models.Todo.completed == False)
    elif filter == "completed":
        query = query.filter(models.Todo.completed == True)
    return query.order_by(models.Todo.id.desc()).all()


@app.post("/api/todos", response_model=schemas.Todo)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    db_todo = models.Todo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


@app.put("/api/todos/{todo_id}", response_model=schemas.Todo)
def update_todo(todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db)):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    for key, value in todo.model_dump(exclude_unset=True).items():
        setattr(db_todo, key, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo


@app.delete("/api/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted"}


# ==================== Requirements ====================
@app.get("/api/requirements", response_model=List[schemas.Requirement])
def get_requirements(
    search: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(models.Requirement)
    if status and status != "all":
        query = query.filter(models.Requirement.status == status)
    if search:
        query = query.filter(models.Requirement.title.contains(search))
    return query.order_by(models.Requirement.id.desc()).all()


@app.get("/api/requirements/stats")
def get_requirement_stats(db: Session = Depends(get_db)):
    total = db.query(models.Requirement).count()
    completed = db.query(models.Requirement).filter(models.Requirement.status == "completed").count()
    in_progress = db.query(models.Requirement).filter(models.Requirement.status == "in-progress").count()
    completion_rate = round((completed / total) * 100) if total > 0 else 0
    return {
        "total": total,
        "completed": completed,
        "in_progress": in_progress,
        "completion_rate": completion_rate
    }


@app.post("/api/requirements", response_model=schemas.Requirement)
def create_requirement(req: schemas.RequirementCreate, db: Session = Depends(get_db)):
    db_req = models.Requirement(**req.model_dump())
    db.add(db_req)
    db.commit()
    db.refresh(db_req)
    return db_req


@app.put("/api/requirements/{req_id}", response_model=schemas.Requirement)
def update_requirement(req_id: int, req: schemas.RequirementUpdate, db: Session = Depends(get_db)):
    db_req = db.query(models.Requirement).filter(models.Requirement.id == req_id).first()
    if not db_req:
        raise HTTPException(status_code=404, detail="Requirement not found")
    for key, value in req.model_dump(exclude_unset=True).items():
        setattr(db_req, key, value)
    db.commit()
    db.refresh(db_req)
    return db_req


@app.delete("/api/requirements/{req_id}")
def delete_requirement(req_id: int, db: Session = Depends(get_db)):
    db_req = db.query(models.Requirement).filter(models.Requirement.id == req_id).first()
    if not db_req:
        raise HTTPException(status_code=404, detail="Requirement not found")
    db.delete(db_req)
    db.commit()
    return {"message": "Requirement deleted"}


# ==================== Friends ====================
@app.get("/api/friends", response_model=List[schemas.Friend])
def get_friends(db: Session = Depends(get_db)):
    return db.query(models.Friend).order_by(models.Friend.id.desc()).all()


@app.post("/api/friends", response_model=schemas.Friend)
def create_friend(friend: schemas.FriendCreate, db: Session = Depends(get_db)):
    db_friend = models.Friend(**friend.model_dump())
    db.add(db_friend)
    db.commit()
    db.refresh(db_friend)
    return db_friend


@app.put("/api/friends/{friend_id}", response_model=schemas.Friend)
def update_friend(friend_id: int, friend: schemas.FriendUpdate, db: Session = Depends(get_db)):
    db_friend = db.query(models.Friend).filter(models.Friend.id == friend_id).first()
    if not db_friend:
        raise HTTPException(status_code=404, detail="Friend not found")
    for key, value in friend.model_dump(exclude_unset=True).items():
        setattr(db_friend, key, value)
    db.commit()
    db.refresh(db_friend)
    return db_friend


@app.delete("/api/friends/{friend_id}")
def delete_friend(friend_id: int, db: Session = Depends(get_db)):
    db_friend = db.query(models.Friend).filter(models.Friend.id == friend_id).first()
    if not db_friend:
        raise HTTPException(status_code=404, detail="Friend not found")
    db.delete(db_friend)
    db.commit()
    return {"message": "Friend deleted"}


# ==================== Tech Stack ====================
@app.get("/api/tech-stack", response_model=List[schemas.TechCategory])
def get_tech_stack(db: Session = Depends(get_db)):
    return db.query(models.TechCategory).order_by(models.TechCategory.id).all()


@app.post("/api/tech-stack/categories", response_model=schemas.TechCategory)
def create_tech_category(category: schemas.TechCategoryCreate, db: Session = Depends(get_db)):
    db_cat = models.TechCategory(**category.model_dump())
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat


@app.post("/api/tech-stack/categories/{category_id}/items", response_model=schemas.TechItem)
def create_tech_item(category_id: int, item: schemas.TechItemCreate, db: Session = Depends(get_db)):
    db_item = models.TechItem(**item.model_dump(), category_id=category_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.delete("/api/tech-stack/categories/{category_id}")
def delete_tech_category(category_id: int, db: Session = Depends(get_db)):
    db_cat = db.query(models.TechCategory).filter(models.TechCategory.id == category_id).first()
    if not db_cat:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(db_cat)
    db.commit()
    return {"message": "Category deleted"}


@app.delete("/api/tech-stack/items/{item_id}")
def delete_tech_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.TechItem).filter(models.TechItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted"}


# ==================== Activities ====================
@app.get("/api/activities", response_model=List[schemas.Activity])
def get_activities(limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Activity).order_by(models.Activity.id.desc()).limit(limit).all()


@app.post("/api/activities", response_model=schemas.Activity)
def create_activity(activity: schemas.ActivityCreate, db: Session = Depends(get_db)):
    db_activity = models.Activity(**activity.model_dump())
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity


@app.delete("/api/activities/{activity_id}")
def delete_activity(activity_id: int, db: Session = Depends(get_db)):
    db_activity = db.query(models.Activity).filter(models.Activity.id == activity_id).first()
    if not db_activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    db.delete(db_activity)
    db.commit()
    return {"message": "Activity deleted"}
