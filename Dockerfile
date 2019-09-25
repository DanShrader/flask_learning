FROM python:3

RUN apt-get update -y
    
RUN apt-get install nano -y

WORKDIR /app

RUN pip install flask psycopg2 flask_sqlalchemy flask_wtf

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]

