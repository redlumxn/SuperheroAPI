FROM python:3


RUN pip install flask flask-jsonpify flask-restful

# add the script to the Dockerfile:
ADD server.py /
ADD data/superheroes.json /data/
ADD requirements.txt /

# install pip dependecies
RUN pip install -r requirements.txt
# execute the script
CMD [ "python", "./server.py" ]
EXPOSE 5002