FROM painelsaudefiocruz/instalador-base:1.0

COPY . app/

WORKDIR app

EXPOSE 5001

CMD [ "python", "run.py" ]
