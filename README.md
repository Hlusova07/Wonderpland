# Wonderpland ✦

**Your own little wonderland**

Wonderpland — это приложение-планировщик, которое помогает организовать повседневные задачи и планы.

Проект сделан в рамках учебного проекта 6 семестра.

## Что умеет приложение

Сейчас в приложении можно:

* посмотреть список задач;
* добавить новую задачу;
* отметить задачу выполненной;
* изменить задачу;
* удалить задачу;
* сохранить задачи в базе данных PostgreSQL.

## Используемые технологии

**Backend:**

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Alembic

**Frontend:**

* HTML
* CSS
* JavaScript

**Тестирование:**

* Pytest
* FastAPI TestClient

## Структура проекта

```text
Wonderpland/
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   └── models.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── tests/
│   └── test_tasks.py
│
├── docs/
│   ├── user-stories.md
│   └── models.md
│
├── alembic/
│   └── versions/
│
├── .gitignore
├── alembic.ini
├── requirements.txt
└── README.md
```

## Как работает приложение

Frontend отправляет запросы на FastAPI.

FastAPI работает с базой данных через SQLAlchemy.

Для хранения данных используется PostgreSQL.

```text
Frontend
   ↓
FastAPI
   ↓
SQLAlchemy
   ↓
PostgreSQL
```

Для создания и изменения таблиц используется Alembic.

## Установка

Сначала нужно скачать проект:

```bash
git clone <URL_REPOSITORY>
cd Wonderpland
```

Создать виртуальное окружение:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Установить библиотеки:

```bash
pip install -r requirements.txt
```

## База данных

Для работы проекта нужен PostgreSQL.

Название базы данных:

```text
wonderpland
```

Данные для подключения находятся в файле `.env`.

В `.env` используется переменная:

DATABASE_URL=postgresql+psycopg2://postgres:password@localhost:5432/wonderpland

Файл `.env` не добавляется в GitHub.

## Запуск проекта

Перед запуском применить миграции:

```bash
alembic upgrade head
```

После этого запустить сервер:

```bash
uvicorn backend.main:app --reload
```

Приложение откроется по адресу:

```text
http://127.0.0.1:8000
```

## Тесты

Для запуска тестов:

```bash
python -m pytest
```

Сейчас проверяются основные действия с задачами:

* получение задач;
* создание задачи;
* изменение задачи;
* удаление задачи.

## Что можно добавить в будущем

В дальнейшем в Wonderpland можно добавить:

* регистрацию пользователей;
* календарь;
* привычки;
* финансовый раздел;
* список прочитанных книг;
* заметки;
* напоминания;
* статистику;
* мобильную версию.
