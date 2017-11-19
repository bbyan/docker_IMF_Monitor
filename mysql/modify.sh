#/bin/bash
mysql -uroot -p$MY_ROOT_PASSWORD < /tmp/${FILE_0}
sleep 60
mysql -uroot -p$MY_ROOT_PASSWORD < /tmp/${FILE_1}
