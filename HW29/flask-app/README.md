
Это простое Flask-приложение, которое отображает рандомного кота при каждой загрузке страницы.  
Приложение контейнеризовано с использованием Docker.

Структура проекта:

flask-app
├── app.py
├── Dockerfile
├── requirements.txt
└── templates/index.html

Как запустить проект:
1. Установить Docker: https://www.docker.com/
2. Откройте в терминале папку проекта cd ../../../flask-app
3. Постройте Docker-образ: docker build -t flask_cat_app .
4. Запустите контейнер: docker run -p 8866:5001 --name flask_cat_app flask_cat_app
5. Откройте в браузере адресную ссылку: http://localhost:8866
6. Готово. При каждом открытии ссылки у вас будет рандомная картинка с котиком
