# Pull base image
FROM python:3.7

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy project
COPY . .

CMD ["python3","manage.py","runserver","0.0.0.0:8000"]