1. Тестую чи встановленний докер та переврка версії за допомогою команд та перенаправляю вивід у файл docker.log docker -v docker -h
2. Створюю імедж із Django зробленим у попередній роботі.

[docker pull python:3.7-slim]
[docker images]
[docker inspect python:3.7-slim]

3. Створюю файл з іменем Dockerfile. Копіюю туди вміст такого ж файлу з репозиторію devops_course.
4. Створюю власний репозиторій на DockerHub. Назва аккаунту - [1995755] У вкладці Repositories -> кнопку Create new repository. Називаю його nyunko-lab4
5. Роблю білд імеджа та завантажую його до репозиторію. 
Для цього вказую правильну назву репозиторію та TAG.

[docker build -t 1995755/nyunko-lab-4:django .]

[docker images]

[docker push 1995610/nyunko-lab-4:django]


====[Посилання на Docker Hub репозиторій;](https://hub.docker.com/repository/docker/1995755/nyunko-lab-4)=====

6. Для запуску веб-сайту потрібно виконати команду: docker run -it --name=django --rm -p 8000:8000 1995755/nyunko-lab-4:django

7. Виконую ті самі дії для створення репозиторію з моніторингом та паралельно з сайтом. Зробив та запустив контейнер з моніторингом та перенаправив логи у server.log

