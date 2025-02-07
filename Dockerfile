FROM  python:3.9

#set the directory in contrainer, all the files will be done in "app" file
WORKDIR /app 

# copy requirements.txt from local to contrainer, in app directory
COPY requirements.txt .

# RUN is the Shell command, install all the dependencies in requirements.txt, --no-cache-dir means don't 
# keep cache for unnecessary package
RUN pip install --no-cache-dir -r requirements.txt

# copy all the files from local to container
COPY . .

# the command needed to run after container is started: python app.py 
# CMD ["python", "app.py"]
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
