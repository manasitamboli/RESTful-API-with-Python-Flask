FROM ubuntu:latest
MAINTAINER 	Manasi Tamboli "manasi3101@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python2.7 python-pip python-dev build-essential
RUN apt-get install -y gunicorn
RUN apt-get install -y python-gevent
RUN pip install Flask
RUN pip install Flask_cors
RUN pip install Flask
RUN pip install requests
RUN apt-get install -y gunicorn
RUN apt-get install net-tools -y

#add source files
WORKDIR /usr/src/app

COPY app /usr/src/app

COPY app/init.sh /usr/src/app/
RUN bash /usr/src/app/init.sh

WORKDIR /usr/src/app/src
RUN chmod a+x server.py
ENTRYPOINT "./server.py" && /bin/bash

EXPOSE 8080

#CMD ["gunicorn", "--config", "./conf/gunicorn_config.py", "src:app"]
#CMD ["/usr/src/app/src/server.py"]
