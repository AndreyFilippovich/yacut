# YaCut
## Описание:
Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

## Технологии

* [Python 3](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [WTForms](https://wtforms.readthedocs.io/en/)
* [Flask-WTF](https://flask-wtf.readthedocs.io/en/)
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/)

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd yacut
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
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Применить миграции:

```
flask db upgrade
```

Запустить проект:

```
flask run
```

Проект будет доступен по адресу:

```
http://127.0.0.1:5000/
```

### Автор проекта:

Филиппович А.В.
