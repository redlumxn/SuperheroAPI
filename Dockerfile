FROM python:3

# install pip dependecies
RUN pip install flask flask-jsonpify flask-restful

# add the script to the Dockerfile:
ADD server.py /
ADD data/superheroes.json /data/

# execute the script
CMD [ "python", "./server.py" ]
EXPOSE 5002