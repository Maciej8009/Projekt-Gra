FROM python:3.12-slim
COPY . .
RUN apt-get update && apt-get install -y libxrender-dev libx11-6 libxext-dev libxinerama-dev libxi-dev libxrandr-dev libxcursor-dev libxtst-dev tk-dev && rm -rf /var/lib/apt/lists/*
RUN pip install mysql-connector-python
RUN pip install pygame

CMD ["python", "main.py"]