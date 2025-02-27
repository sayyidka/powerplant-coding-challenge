FROM python:3.9-slim-buster

WORKDIR /powerplant

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python", "app.py" ]