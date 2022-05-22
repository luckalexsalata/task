FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /task
WORKDIR /task

COPY requirements.txt .
COPY . /task/

RUN pip install -r requirements.txt

ADD . /task/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
