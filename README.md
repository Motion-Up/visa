# Проект Health Test
Веб-приложени для отправки своей заявки на почту.
Вы можете посмотреть веб-приложение перейдя по ссылке https://visatobali.com

### Technology:
Python, Django, nginx, gunicorn, supervisor, mailgun, https сетрификат

### Установка:
Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/Motion-Up/visa.git
```
```
cd visa
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
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
