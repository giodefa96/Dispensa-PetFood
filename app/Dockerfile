FROM python:3.8

# Set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1  
ENV PYTHONUNBUFFERED 1  

WORKDIR ./app

COPY . .

# Install dependencies  
RUN pip install --upgrade pip  
RUN pip install -r requirements.txt  

CMD ["gunicorn", "-w", "3", "-b", ":8000", "-t", "360", "--reload", "wsgi:app"]


