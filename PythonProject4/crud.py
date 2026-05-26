from sqlalchemy.orm import Session
from models import Author, Post, Comment
from datetime import datetime

def create_author(session: Session, name: str, email: str) -> Author:
    '''Создает нового автора, возвращает объект'''
    new_author = Author(name=name, email=email)
    session.add(new_author)
    session.commit()
    session.refresh(new_author)  # Обновляем объект, чтобы получить id
    return new_author

def get_author_by_email(session: Session, email: str) -> Author | None:
    """Ищет автора по email"""
    return session.query(Author).filter(Author.email == email).first()

def create_post(session: Session, title: str, content: str,
                author_id: int, published: bool = False) -> Post:
    """Создает новый пост"""
    new_post = Post(
        title=title,
        content=content,
        author_id=author_id,
        published=published
    )
    session.add(new_post)
    session.commit()
    session.refresh(new_post)
    return new_post

def get_published_posts(session: Session, limit: int = 10) -> list[Post]:
    """Возвращает только опубликованные посты (published=True)"""
    return session.query(Post).filter(Post.published == True).limit(limit).all()

def get_posts_by_author(session: Session, author_id: int, limit: int = 10) -> list[Post]:
    """Возвращает все посты конкретного автора"""
    return session.query(Post).filter(Post.author_id == author_id).limit(limit).all()


def update_post_status(session: Session, post_id: int, published: bool) -> bool:
    """Меняет статус публикации поста, возвращает True если успешно"""
    post = session.query(Post).filter(Post.id == post_id).first()
    if post is None:
        return False  # Пост не найден

    post.published = published
    session.commit()
    return True

def add_comment(session: Session, post_id: int, author_name: str, text: str) -> Comment:
    """Добавляет комментарий к посту"""
    new_comment = Comment(
        post_id=post_id,
        author_name=author_name,
        text=text
    )
    session.add(new_comment)
    session.commit()
    session.refresh(new_comment)
    return new_comment


def get_top_authors_by_posts(session: Session, limit: int = 3) -> list[tuple[str,int]]:
    """
    Возвращает топ авторов по количеству постов.
    Пример возврата: [('Анна', 12), ('Иван', 8), ('Мария', 5)]
    """
    from sqlalchemy import func, desc

    # Запрос с агрегацией: считаем количество постов для каждого автора
    result = (session.query(
        Author.name,
        func.count(Post.id).label('post_count')
            )
            .join(Post)  # Присоединяем таблицу постов по foreign key
            .group_by(Author.id)  # Группируем по автору
            .order_by(desc('post_count'))  # Сортируем по убыванию количества
            .limit(limit)  # Берём только топ-N
            .all())

    # result — это список кортежей: [('Анна', 12), ('Иван', 8), ...]
    return result


# Добавьте в конец файла crud.py

def get_author_by_name(session: Session, name: str) -> Author | None:
    """1. Находит автора по имени"""
    return session.query(Author).filter(Author.name == name).first()


def get_published_posts_by_date(session: Session, date: datetime) -> list[Post]:
    """2. Выводит опубликованные посты за определенную дату"""
    # Начало и конец указанного дня
    start_of_day = datetime(date.year, date.month, date.day, 0, 0, 0)
    end_of_day = datetime(date.year, date.month, date.day, 23, 59, 59)

    return (session.query(Post)
            .filter(Post.published == True)
            .filter(Post.created_at >= start_of_day)
            .filter(Post.created_at <= end_of_day)
            .all())


def create_multiple_authors(session: Session, authors_data: list[dict]) -> list[Author]:
    """3. Добавляет сразу нескольких авторов в БД
       authors_data = [
           {"name": "Имя1", "email": "email1@example.com"},
           {"name": "Имя2", "email": "email2@example.com"},
       ]
    """
    created_authors = []
    for data in authors_data:
        new_author = Author(name=data["name"], email=data["email"])
        session.add(new_author)
        created_authors.append(new_author)

    session.commit()

    # Обновляем объекты, чтобы получить id
    for author in created_authors:
        session.refresh(author)

    return created_authors


def get_post_with_comments(session: Session, post_id: int) -> dict | None:
    """4. Находит пост по id и возвращает пост с комментариями в виде словаря"""
    post = session.query(Post).filter(Post.id == post_id).first()

    if post is None:
        return None

    return {
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "published": post.published,
        "created_at": post.created_at,
        "author": {
            "id": post.author.id,
            "name": post.author.name,
            "email": post.author.email
        },
        "comments": [
            {
                "id": comment.id,
                "author_name": comment.author_name,
                "text": comment.text,
                "created_at": comment.created_at
            }
            for comment in post.comments
        ]
    }