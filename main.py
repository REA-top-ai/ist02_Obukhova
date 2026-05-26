from database import SessionLocal, engine, Base
from models import Author, Post, Comment
from crud import *
from datetime import datetime, date


def main():
    # Создаём таблицы, если их нет (безопасно: если есть — ничего не меняет)
    Base.metadata.create_all(bind=engine)

    # Создаём сессию для работы с БД
    session = SessionLocal()

    try:
        print("Начинаем тестирование...\n")

        # 1. Создаём тестовых авторов
        print("Создаём авторов...")
        author1 = create_author(session, "Анна Иванова", "annav@example.com")
        author2 = create_author(session, "Иван Алексеев", "ivana@example.com")
        print(f"{author1.name} (id={author1.id})")
        print(f"{author2.name} (id={author2.id})\n")

        # 2. Создаём посты для Анны
        print("Создаём посты...")
        post1 = create_post(session, "Первый пост", "Это содержание первого поста. Оно достаточно длинное.", author1.id,
                            published=True)
        post2 = create_post(session, "Черновик", "Этот пост пока не опубликован.", author1.id, published=False)
        post3 = create_post(session, "Пост Ивана", "Текст от Ивана.", author2.id, published=True)
        print(f"'{post1.title}' (опубликован)")
        print(f"'{post2.title}' (черновик)")
        print(f"'{post3.title}' (опубликован)\n")

        # 3. Добавляем комментарии к первому посту
        print("Добавляем комментарии...")
        add_comment(session, post1.id, "Читатель1", "Отличная статья, очень полезно!")
        add_comment(session, post1.id, "Читатель2", "Спасибо за материал, жду продолжения.")
        add_comment(session, post1.id, "Аноним", "Коротко.")
        print("3 комментария добавлены к первому посту\n")

        # 4. Публикуем черновик
        print("Публикуем черновик...")
        success = update_post_status(session, post2.id, published=True)
        if success:
            print(f"'{post2.title}' теперь опубликован\n")

        # 5. Выводим все опубликованные посты
        print("Все опубликованные посты:")
        published = get_published_posts(session)
        for post in published:
            print(f"'{post.title}' — автор: {post.author.name}")
        print()

        # 6. Топ авторов по количеству постов
        print("🏆 Топ авторов по количеству постов:")
        top_authors = get_top_authors_by_posts(session, limit=3)
        for rank, (name, count) in enumerate(top_authors, 1):
            print(f"{rank}. {name}: {count} пост(ов)")
        print()

        # 7. Поиск автора по email
        print("Поиск автора по email...")
        found = get_author_by_email(session, "anna@example.com")
        if found:
            print(f"Найдено: {found.name}\n")
        else:
            print("Автор не найден\n")

        # ========== НОВЫЕ ТЕСТЫ ==========

        # 8. ТЕСТ: Поиск автора по имени
        print("=" * 50)
        print("ТЕСТ 1: Поиск автора по имени")
        author_by_name = get_author_by_name(session, "Анна Петрова")
        if author_by_name:
            print(f"Найден автор: {author_by_name.name}, email: {author_by_name.email}")
        else:
            print("Автор не найден")
        print()

        # 9. ТЕСТ: Поиск опубликованных постов за сегодняшнюю дату
        print("ТЕСТ 2: Поиск опубликованных постов за сегодня")
        today = datetime.now()
        posts_today = get_published_posts_by_date(session, today)
        if posts_today:
            print(f" Найдено постов за сегодня: {len(posts_today)}")
            for post in posts_today:
                print(f"   - {post.title}")
        else:
            print(" Постов за сегодня не найдено")
        print()

        # 10. ТЕСТ: Добавление нескольких авторов
        print("ТЕСТ 3: Добавление нескольких авторов сразу")
        new_authors_data = [
            {"name": "Петр Иванов", "email": "petr@example.com"},
            {"name": "Мария Смирнова", "email": "maria@example.com"},
            {"name": "Сергей Козлов", "email": "sergey@example.com"}
        ]
        new_authors = create_multiple_authors(session, new_authors_data)
        print(f"✅ Добавлено {len(new_authors)} авторов:")
        for author in new_authors:
            print(f"   - {author.name} (id={author.id})")
        print()

        # 11. ТЕСТ: Поиск поста с комментариями
        print("ТЕСТ 4: Поиск поста с комментариями")
        post_with_comments = get_post_with_comments(session, post1.id)
        if post_with_comments:
            print(f" Найден пост: '{post_with_comments['title']}'")
            print(f"   Автор: {post_with_comments['author']['name']}")
            print(f"   Содержание: {post_with_comments['content'][:100]}...")
            print(f"   Количество комментариев: {len(post_with_comments['comments'])}")
            if post_with_comments['comments']:
                print("   Комментарии:")
                for comment in post_with_comments['comments']:
                    print(f"     - {comment['author_name']}: {comment['text'][:50]}")
        else:
            print(" Пост не найден")
        print()

    except Exception as e:
        print(f"Ошибка: {e}")
        session.rollback()
    finally:
        session.close()
        print("\n" + "=" * 50)
        print("Тестирование завершено. Сессия закрыта.")


if __name__ == "__main__":
    main()