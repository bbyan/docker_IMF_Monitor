create database django character set utf8 collate utf8_bin;
use mysql;
grant all privileges on *.* to 'django'@'%' identified by 'django' with grant option;
grant all privileges on *.* to 'django'@'localhost' identified by 'django' with grant option;
flush privileges;
exit
