from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Book
from database import SessionLocal, engine
from schemas import BookCreate, Book
from sqlalchemy.orm import Session

# Создаём приложение FastAPI
app = FastAPI()

# Создаем таблицы в базе данных
from models import Base
Base.metadata.create_all(bind=engine)

# Функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD операции

# Получить все книги
@app.get("/books/", response_model=list[Book])
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

# Получить книгу по id
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Создать книгу
@app.post("/books/", response_model=Book)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(title=book.title, author=book.author, description=book.description)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Обновить книгу
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db_book.title = book.title
    db_book.author = book.author
    db_book.description = book.description
    db.commit()
    db.refresh(db_book)
    return db_book

# Удалить книгу
@app.delete("/books/{book_id}", response_model=Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return db_book