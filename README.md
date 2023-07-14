# Blogicum
# django_sprint4
## Описание
Социальная сеть для публикации личных дневников.
Сайт, на котором пользователь может создать свою страницу и 
публиковать на ней сообщения («посты»).


## Установка и запуск

**Версия Python3.9**

Клонировать репозиторий:
```sh
git clone <https or SSH URL>
```

Перейти в папку проекта:
```sh
cd django_sprint4
```

### Далее два варианта на выбор
***
### 1. Автоматическая установка
Запустить скрипт и следовать инструкциям:
```sh
bash install.sh
```

***
### 2. Пошаговая установка
Создать и активировать виртуальное окружение:
```sh
python3 -m venv venv
source venv/bin/activate
```

Обновить pip:
```sh
python3 -m pip install --upgrade pip
```

Установить библиотеки:
```sh
pip install -r requirements.txt
```

Выполнить миграции:
```sh
python3 blogicum/manage.py migrate
```

Загрузить фикстуры DB:
```sh
python3 blogicum/manage.py loaddata db.json
```

Создать суперпользователя:
```sh
python3 blogicum/manage.py createsuperuser
```

Запустить сервер django:
```sh
python3 blogicum/manage.py runserver
```