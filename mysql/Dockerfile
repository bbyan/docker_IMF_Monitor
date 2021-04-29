FROM mysql:5.6

ENV AUTO_RUN_DIR /docker-entrypoint-initdb.d/

ENV FILE_O 0-create_django.sql

COPY ./mysqld.cnf /etc/mysql/mysql.conf.d/
COPY ./config/sql/${FILE_0} ${AUTO_RUN_DIR}




