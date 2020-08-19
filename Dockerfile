FROM python:3.8-slim
COPY ./service /carshare
WORKDIR /carshare
RUN pip install -r requirements.txt
CMD ["python","carshare.py"]