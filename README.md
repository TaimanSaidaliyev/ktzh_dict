# Справочник сотрудников АО Грузовые перевозки

### Технологии
Данное приложение было написано на **Python Django 5.1**. Версия Python 3.10

### Установка
1. Для начала выгрузите из git и разверните на сервере.
2. Необходимо установить в корне проекта venv и развернуть для этого проекта.
```html
sudo apt install python3-venv
```

```html
python3 -m venv venv
```
Активировать venv
```html
source venv/bin/activate
```

3. Установить зависимости
```html
pip install -r requirements.txt
```

4. Запуск приложения
```html
python manage.py runserver
```

При желании можете запустить его на определенном порту.
```html
python manage.py runserver 0.0.0.0:8000
```

Нет необходимости установки базы данных, т.к. здесь используются локальная DBSQLITE