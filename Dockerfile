FROM python:alpine
RUN adduser -D arty
RUN mkdir -p /home/arty/app
USER arty
WORKDIR /home/arty/app
COPY requirements.txt .
ENV PATH=$PATH:/home/arty/.local/bin
RUN pip install --user --upgrade pip
RUN pip install --user -r requirements.txt
COPY . .
CMD ["python", "app.py"]