1. Створив базову структуру проекту.

2. Копіюю файли з репозиторію devops_course у відповідні папки свого. Ознайомлююсь із вмістом кожного з файлів.

3. Виконую данні команди:[pipenv --python 3.7], [pipenv install -r requirements.txt], [pipenv run python app.py]

4. Сервер запустився, проте видав помилки. [redis.exceptions.ConnectionError], через те що відсутній redis server.

5. Встановлюю redis-сервер, щоб виправити помилки.

![Image](https://github.com/NazarYunko/dev-course-labs/tree/master/lab5/images/first_run.png)

6. Ініціалізовую тести [pipenv run pytest test_app.py --url http://localhost:5000].

7. За допомогою команди [make -f Makefile] створюю Docker імеджі для додатку та для тестів.

8. Запускаю додаток і бачу наступне:

![Image](https://github.com/NazarYunko/dev-course-labs/tree/master/lab5/images/makefile_run.png)

Dockerhub: https://hub.docker.com/repository/docker/1995755/nyunko-lab-5 .

9. Очищаю всі імеджі за допомогою команди [make docker-prune].

10. Створюю docker-compose.yml

11. Запускаю docker-compose.

12. Перевіряю чи працює сайт.

![Image](https://github.com/NazarYunko/dev-course-labs/tree/master/lab5/images/docker_compose_run.png)

13. Я віддаю перевагу docker-compose, тому що він більш зручніший і більше зрозуміла стурктура.

14. Створив docker-compose для лабораторноi роботи №4.



