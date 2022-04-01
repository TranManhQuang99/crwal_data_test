from fastapi import APIRouter
import datetime
from .. import schemas
from typing import List
from .. import schemas, database, models, oauth2
from fastapi import FastAPI, Depends, status, Response, HTTPException, Depends
from sqlalchemy.orm import Session
from ..repository import blog


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


@router.post('/timekeeper', status_code=status.HTTP_201_CREATED)
def create_timekeeper(request: schemas.TimeKeeper, db: Session = Depends(database.get_db)):
    new_timekeeper = models.Timekeeping(name=request.name)
    db.add(new_timekeeper)
    db.commit()
    db.refresh(new_timekeeper)
    return new_timekeeper


@router.get('/timekeeper/{name}', status_code=200)
def show_timekeeper(name, db: Session = Depends(database.get_db)):
    # return blog.show(id, response, db)
    now = datetime.datetime.now()
    today8h30am = now.replace(hour=8, minute=30, second=0,microsecond=0)
    show_timekeep = db.query(models.Timekeeping).filter(models.Timekeeping.name == name).first()
    if not show_timekeep:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'{name} is not available ')

    check_timekeeper = show_timekeep.timekeeping > today8h30am
    return check_timekeeper


# now = datetime.now()
# time_string = now.strftime("%Y-%m-%d %H:%M:%S")
# print(time_string)
# ĐẦU RA
# >>> import datetime
# >>> now = datetime.datetime.now()
# >>> today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)
# >>> now < today8am
# True
# >>> now == today8am
# False
# >>> now > today8am
# False

