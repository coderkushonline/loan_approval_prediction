# base image
FROM python:3.12.10

# working directory 
WORKDIR /app

# Copy 
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port for flask
EXPOSE 5000

# Command to run the flask app
CMD ["python3", "./app.py"]
