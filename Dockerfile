FROM python:3.9

RUN mkdir /reservation

WORKDIR /reservation

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /reservation/docker/*.sh
