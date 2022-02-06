FROM python:3.8
WORKDIR /usr/src/fast_socket
COPY ./requirements.txt /usr/src/fast_socket/requirements.txt
RUN pip install -r requirements.txt
COPY . /usr/src/fast_socket
# CMD [ "python" , "main.py"]
# CMD ["hypercorn", "main:app", "--host", "0.0.0.0", "--port", "5002","--reload"]
# ENTRYPOINT ["hypercorn", "main:app", "-b", "0.0.0.0:5002", "--reload" , "--debug"]
ENTRYPOINT ["uvicorn", "main:app", "--reload","--host", "0.0.0.0", "--port", "5002" , "--ws-ping-timeout" , "10000"]
# CMD ["watchmedo", "auto-restart", "--pattern" , "*.py" ,"--recursive", "--signal", "SIGTERM", "python" ,"run.py"]