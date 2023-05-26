<div><a href="https://github.com/akkrn/api_final_yatube/blob/main/README-rus.md" ><img alt="ru" src="https://img.shields.io/badge/%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%8F-%D0%BD%D0%B0%20%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%BC-white"/></a></div>
<details open><summary><h2>📚 Description</h2></summary>

This project is a fully-featured API for [this service](https://github.com/akkrn/hw05_final). With it you can create, modify your posts, read other people's posts, you can also comment on them. Subscribe to interesting authors and join interest groups

### Example of using the API:
Once the project is up and running, you can check out the API documentation at: http://127.0.0.1:8000/redoc/

Here is one possible GET request:
http://127.0.0.1:8000/api/v1/posts/

```
[
    {
        "id": 1,
        "author": "admin",
        "text": "This is a test post for an example of how to use the API.",
        "pub_date": "2023-03-13T08:43:43.793402Z",
        "image": null,
        "group": null
    }
]
```
</details>

<details><summary><h2>🛠️ Tech Stack</h2></summary>
<img src="https://img.shields.io/badge/Python-%2314354c.svg?logo=Python&logoColor=white&style=flat" alt="Python" /> <img src="https://img.shields.io/badge/Django-%23092e20.svg?logo=django&logoColor=white&style=flat" alt="Django" /> <img src="https://img.shields.io/badge/Django-REST-ff1709?style=flat&logo=django&logoColor=white&color=ff1709&labelColor=gray" alt="DRF" />  <img src="https://img.shields.io/badge/JWT-000000?style=flat&logo=JSON%20web%20tokens&logoColor=white" alt="JWT" /> <img src="https://img.shields.io/badge/SQLite-07405E?style=flat&logo=sqlite&logoColor=white" alt="SQLite" />
</details>
<details><summary><h2>🏗️ Installation</h2></summary>
Clone the repository and go to it on the command line:

```
git clone https://github.com/akkrn/api_final_yatube.git
```

Create and activate a virtual environment:

```
python3 -m venv venv
```

* If you have Linux/macOS

    ```
    source venv/bin/activate
    ```

* If you have windows

    ```
    source venv/Scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Install dependencies from the requirements.txt file:

```
pip install -r requirements.txt
```

Perform migrations:

```
python3 manage.py migrate
```

Run the project:

```
python3 manage.py runserver
```
</details>
