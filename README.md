# conference
https://github.com/Aturaya25/conference.git

Перейти в папку:
```bash
cd locallibrary
```
* Запустить следующий файл
```bash
bash ./start.sh
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

Можно смотреть детали конкретных презентаций, аудиторий и расписаний.

Докладчикам доступно создавать, изменять и отменять выступление и те же действия с презентацией.

* Запуск тестов
```bash
python3 manage.py test
```
