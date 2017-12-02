#!/bin/bash
echo "------------------------------------IMF Monitor V0.1 Status ----------------------------------"
printf "\n"
echo "----------Docker Status-----------"
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Command}}\t{{.Ports}}"
printf "\n"
echo "---------Service Status-----------"
printf "\n"
printf "Zabbix-Service\t:\t" 
systemctl is-failed zabbix-server
printf "Zabbix-Agent\t:\t"
systemctl is-failed zabbix-agent 
printf "Docker-Service\t:\t"
systemctl is-failed docker 
printf "\n"
echo "---------Crontab Info-----------"
tail -n4 /var/log/cron.log | grep zabbix
echo "---------------------------------------------------------------------------------------------"
