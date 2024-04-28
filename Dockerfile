# Use the official Python image as a parent image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container at /code
COPY requirements.txt /code/

# Install dependencies
RUN pip install -r requirements.txt

# Copy the run script into the container
COPY run.sh /code/run.sh

# Grant execute permissions to the run script
RUN chmod +x /code/run.sh

# Copy the current directory contents into the container at /code
COPY . /code/

# Set the run to the custom script
ENTRYPOINT ["/code/run.sh"]

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
