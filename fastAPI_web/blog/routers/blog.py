from fastapi import APIRouter
from .. import schemas
from typing import List
from .. import schemas, database, models, oauth2
from fastapi import FastAPI, Depends, status, Response, HTTPException, Depends
from sqlalchemy.orm import Session
from ..repository import blog
from datetime import datetime


router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


@router.get('/', response_model=List[schemas.Showblog])
def element_database(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


@router.delete('/{id}')
def destroy(id, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.Showblog)
def show(id, response: Response, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, response, db)


@router.post('/timekeeper',  status_code=status.HTTP_201_CREATED)
def create_timekeeper(request: schemas.TimeKeeper, db: Session = Depends(database.get_db)):
    new_timekeeper = models.Timekeeping(name=request.name, id=request.id)
    db.add(new_timekeeper)
    db.commit()
    db.refresh(new_timekeeper)
    return new_timekeeper






