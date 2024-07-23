FROM python:3.9
WORKDIR	 /app
COPY requirements.txt ./
COPY . api.py ./
RUN pip install -r requirements.txt
CMD ["python3","api.py"]

