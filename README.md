### Описание:

Данный проект предназначен для созднания, изменения своих постов и чтения чужих, также вы можете комментировать, подписываться на интересных авторов и объединяться в группы по интересам

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/akkrn/api_final_yatube.git
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source venv/Scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Пример использования API:

После запуска проекта, вы можете ознакомиться с документацией API по адресу: http://127.0.0.1:8000/redoc/

Вот один из возможных GET-запросов:
http://127.0.0.1:8000/api/v1/posts/

```
[
    {
        "id": 1,
        "author": "admin",
        "text": "Это тестовый пост для примера использования API",
        "pub_date": "2023-03-13T08:43:43.793402Z",
        "image": null,
        "group": null
    }
]
```
