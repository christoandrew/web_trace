FROM python:3

ENV PYTHONUNBUFFERED 1

#RUN MKDIR /opt/app

WORKDIR /opt/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

RUN ls

EXPOSE 8000


#RUN ["python", "./manage.py", "migrate"]

CMD ["python", "./manage.py", "runserver"]
