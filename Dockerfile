FROM python:latest

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN python dtServer/data/db_init.py
EXPOSE 5000

CMD ["python", "dtServer/main.py", "0.0.0.0", "5000"]

