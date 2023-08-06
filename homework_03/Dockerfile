# Билдим это приложение с помощью команды docker build homework_03 -t app(обязательно запустить Docker Engine!),
# Затем запускаем приложение с помощью команды docker run -p 8080:8000 -it app(порты можно любые приписать, но чтобы они были разными!),
# Потом заходим в Docker Desktop и проходим в Containers и в колонке Ports нажимаем на ваши порты(в примере это 8080:8000) и все готово!
FROM python:3.9-buster

WORKDIR /app

RUN pip install --upgrade pip setuptools "poetry==1.5.1"
RUN poetry config virtualenvs.create false
RUN pip install fastapi
RUN pip install uvicorn[standart]

COPY requirements.txt ./
RUN pip install install --only main,view

COPY . . 

CMD uvicorn view:app --host 0.0.0.0 --port 8000
