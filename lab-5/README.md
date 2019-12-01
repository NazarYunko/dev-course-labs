1. Створив базову структуру проекту.

2. Копіюю файли з репозиторію devops_course у відповідні папки свого. Ознайомлююсь із вмістом кожного з файлів.

3. Виконую данні команди:[pipenv --python 3.7], [pipenv install -r requirements.txt], [pipenv run python app.py]

4. Сервер запустився, проте видав помилки. [redis.exceptions.ConnectionError], через те що відсутній redis server.

5. Встановлюю redis-сервер, щоб виправити помилки.

![Farmers Market Finder Demo](https://github.com/NazarYunko/dev-course-labs/tree/master/lab5/images/first_run.png)

6. Ініціалізовую тести [pipenv run pytest test_app.py --url http://localhost:5000].


