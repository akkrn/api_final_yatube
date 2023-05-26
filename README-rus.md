<div><a href="https://github.com/akkrn/api_final_yatube/blob/main/README.md" ><img alt="ru" src="https://img.shields.io/badge/version-on%20english-white"/></a></div>

<details open><summary><h2>📚 Описание</h2></summary>

Данный проект - полноценное API для [данного сервиса](https://github.com/akkrn/hw05_final) . С помощью него вы можете создавать, изменять свои посты, читать чужие записи, также вы можете их комментировать. Подписывайтесь на интересных авторов и объединяйтесь в группы по интересам

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

</details>

<details><summary><h2>🛠️ Стэк технологий</h2></summary>
<img src="https://img.shields.io/badge/Python-%2314354c.svg?logo=Python&logoColor=white&style=flat" alt="Python" /> <img src="https://img.shields.io/badge/Django-%23092e20.svg?logo=django&logoColor=white&style=flat" alt="Django" /> <img src="https://img.shields.io/badge/Django-REST-ff1709?style=flat&logo=django&logoColor=white&color=ff1709&labelColor=gray" alt="DRF" />  <img src="https://img.shields.io/badge/JWT-000000?style=flat&logo=JSON%20web%20tokens&logoColor=white" alt="JWT" /> <img src="https://img.shields.io/badge/SQLite-07405E?style=flat&logo=sqlite&logoColor=white" alt="SQLite" />


</details>
<details><summary><h2>🏗️ Развертывание</h2></summary>
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
    source venv/bin/activate
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

</details>
