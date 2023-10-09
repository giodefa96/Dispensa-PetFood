# Fetching official base image for python    
FROM python:3.9-alpine as web    
    
# Setting up the work directory    
WORKDIR /app    
    
# Preventing python from writing pyc to docker container    
ENV PYTHONDONTWRITEBYTECODE 1    
    
# Flushing out python buffer    
ENV PYTHONUNBUFFERED 1    
    
# Updating the os and installing dependencies    
RUN apk update && \    
    apk add --no-cache gcc musl-dev && \    
    pip install --upgrade pip
    
# Copying requirement file    
COPY ./requirements.txt ./    
    
# Installing dependencies    
RUN pip install -r ./requirements.txt    
    
# Copying all the files in our project    
COPY . .    
  
# Starting Gunicorn    
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "--reload", "app.wsgi:application"]  
