#set base image
FROM python:latest

# Set working directory
WORKDIR /app

#install pyhton dependencies
RUN pip install --upgrade pip

#copy python script to the /app folder
COPY finished_auto_file_sorter.py .

#set commands for docker to run when image is started in a container
CMD [ "python" , "finished_auto_file_sorter.py"]