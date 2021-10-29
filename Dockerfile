FROM python:3.9.7-alpine3.14


# We copy just the requirements.txt first to leverage Docker cache
# COPY ./requirements.txt /app/requirements.txt

COPY . .


RUN pip install --upgrade pip
RUN echo ls
RUN echo PWD
RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]