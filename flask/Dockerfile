FROM python:3.8
WORKDIR /usr/src/flask
COPY ./requirements.txt /usr/src/flask/requirements.txt
RUN pip install -r requirements.txt
COPY . /usr/src/flask
CMD [ "python" , "run.py"]