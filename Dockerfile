FROM  python:3.8-alpine

COPY . app/

WORKDIR app

RUN apk update && apk upgrade
RUN apk add --no-cache postgresql-dev build-base  \
                       pkgconfig \
                       git \
                       gcc \
                       libcurl \
                       python3-dev \
                       gpgme-dev \
                       libc-dev \
    && rm -rf /var/cache/apk/*

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 5001

CMD [ "python", "run.py" ]
