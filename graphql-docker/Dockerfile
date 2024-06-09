# # Use the official Python image.
# FROM python:3.9

# # Set the working directory in the container
# WORKDIR /usr/src/app

# # Copy the requirements file into the container
# COPY requirements.txt ./

# # Install the required dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the application code into the container
# COPY . .

# # Run the web service on container startup.
# CMD [ "python", "./app.py" ]

# # Expose the port the app runs on
# EXPOSE 5000
# Dockerfile
# FROM python:3.9

# WORKDIR /app

# # Copy the requirements file and install dependencies
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# # Copy the entire application directory into the container
# COPY . .

# # Specify the command to run the application
# CMD ["python", "app.py"]
FROM python:3.9

WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Install requests module
RUN pip install requests

# Copy the application code into the container
COPY . .

# Specify the command to run the application
CMD ["python", "app.py"]

