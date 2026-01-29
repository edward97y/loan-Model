FROM python:3.12.3 

WORKDIR /app

COPY requirements.txt . 
COPY pipeline_model.pkl . 
COPY main.py . 

RUN pip install -r requirements.txt

EXPOSE 10000

ENTRYPOINT [ "python","main.py" ]