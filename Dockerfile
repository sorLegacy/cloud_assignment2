# Use the official Python 3.9 image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY cloud_assignment2.py /app/

# Install the dependencies
COPY requirments.txt /app/
COPY paragraphs.txt /app/
RUN pip install --no-cache-dir -r requirments.txt
RUN python -m spacy download en_core_web_sm 

# Command to run the Python script
CMD ["python", "cloud_assignment2.py"]

