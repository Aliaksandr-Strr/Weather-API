“Погода”

В проекте используется api.openweathermap.org/data/2.5/weather?q=Minsk,uk&APPID=447f8c8e9662b33ea7d21aceaed9c98e.
Через restful api передаются нужные данные клиенту.

"python manage.py updated_weather" - Вызывает пользовательскую команду, которая получает актуальные погодные данные для Минска и сохраняет их в БД.
"python manage.py updated_weather -c Moscow" - Позволяет получить актуальные погодные данные для любого города

Запуск приложения- "python manage.py runserver"

"http://127.0.0.1:8000/api/weather/" -по урлу получаем последние внесенные в БД данные о погоде.

В приложении используется:

 python == 3.6.1

djangorestframework==3.11.0

Django==2.2

requests==2.23.0

sqlite3
