#!/bin/bash
#SMS with gnokii

PATH=/bin:/sbin/:/usr/bin:/usr/sbin:/usr/local/bin/
export LANG=en_US.UTF-8
LOGFILE='/tmp/zabbix_sms.log'
DT=$(date +%F' '%T)

echo "***************************START:$DT************************************" >> $LOGFILE
echo 'Recipient='$1'' >> $LOGFILE
echo 'Subject='$2'' >> $LOGFILE
echo 'Message='$3'' >> $LOGFILE
echo `` >> $LOGFILE
MOBILE_NUMBER=`echo "$1"`

# Log it
echo 'Send Command:' >> $LOGFILE
echo 'echo $3 | gnokii --sendsms $MOBILE_NUMBER ' >> $LOGFILE
echo `` >> $LOGFILE

# Send it
echo 'Sending Process:' >> $LOGFILE
echo "$3" | gnokii --sendsms "$MOBILE_NUMBER" 1>>$LOGFILE 2>&1

#EOF
DT=$(date +%F' '%T)
echo "***************************STOP:$DT************************************" >> $LOGFILE
echo -e '\n' >> $LOGFILE