FROM python:3.9.15-slim-buster

WORKDIR /src

COPY src/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY src .

CMD [ "python", "-m", "main"]