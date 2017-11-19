FROM mysql

ENV WORK_PATH /tmp/

ENV AUTO_RUN_DIR /docker-entrypoint-initdb.d/

ENV FILE_O 0-create_django.sql

COPY ./mysqld.cnf /etc/mysql/mysql.conf.d/
COPY ./${FILE_0} ${AUTO_RUN_DIR}




