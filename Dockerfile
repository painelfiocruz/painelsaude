FROM  painelsaudefiocruz/public-dashboard:0.1

RUN pip install tqdm xlrd==1.2.0 pillow openpyxl 
COPY . app/

WORKDIR app

EXPOSE 5001

CMD [ "python", "run.py" ]

