FROM python:3.9.7-alpine3.14

COPY . .


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python -m unittest 

ENTRYPOINT [ "python" ]

CMD [ "app/main.py" ]