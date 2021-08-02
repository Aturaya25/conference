# conference
https://github.com/Aturaya25/conference.git
Перейти в папку:
```bash
cd locallibrary
```
Создать и активировать виртуальное окружение Python.
Установить зависимости из файла **requirements.txt**:
```bash
pip install -r requirements.txt
```

# Выполнить следующие команды:
* Команда для создания миграций приложения для базы данных
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

* Создание суперпользователя
```bash
python3 manage.py createsuperuser
```
```bash
Username (leave blank to use 'admin'): admin
Email address: admin@admin.com
Password: ********
Password (again): ********
Superuser created successfully.
```
* Команда для заполнения данных
```bash
python3 manange.py loaddata catalog/room.json
python3 manange.py loaddata catalog/presentation.json
```
* Команда для запуска приложения
```bash
python3 manange.py runserver
```

Главная страница содержит количество аудиторий, презентация и намеченных выступлений
http://127.0.0.1:8000/catalog/

Расписание
http://127.0.0.1:8000/catalog/schedule/

Презентации
http://127.0.0.1:8000/catalog/presentation/

Аудитории
http://127.0.0.1:8000/catalog/room/

Вся функциональность организованна с переходами по ролям.
Роли: admin, presenter, listener.
