FROM tiangolo/uwsgi-nginx-flask:python3.9

RUN pip install --upgrade pip "poetry==1.5.1"
RUN poetry config virtualenvs.create false --local

COPY requirements.txt ./
RUN pip install install --only app,view,templates

COPY . /app