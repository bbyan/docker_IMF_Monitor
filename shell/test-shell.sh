#/bin/bash


[ -z ${1} ] && echo "Must have one parameter" && exit 1
#ENV Log-File PATH
log_path=/opt/ueasib/logs/sonic
log_file=${log_path}/PVGSIDomain.CA01-AFDS${1}.log

#Variable Error-Message
error_message="$(date) [JMS Session Delivery Thread - SonicESB/esb/PVGSIDomain/CA01-AFDSACDM/EC-AFDSACDM/Msg_Connection$SESSION$SV-AFDSACDMCombined_0$219:-2941905142633861815] WARN  PVGSIDomain.CA01-AFDSACDM:ID=SV-AFDSACDMCombined [AFDS] - AFDSFlightData received but no subscription from this client - ignoring message"
#Variable Recovery-Message
recovery_message="$(date) 2016-07-28 02:00:00,934 [JMS Session Delivery Thread - SonicESB/esb/PVGSIDomain/CA01-AFDSACDM/EC-AFDSACDM/Msg_Connection$SESSION$SV-AFDSACDMRequest_0$227:6808187299556879689] INFO  com.ultra_as.gxi.GxiProcessor [AFDS] - SQL printing SYSTEM_ID = 0 AND STD <= to_date('20160729235959','yyyymmddhh24miss') and STD >= to_date('20160729000000','yyyymmddhh24miss') and BAL = 'PVG'"
#Loop Insert Error-Message to Log-File after 3 min insert  past Recovery-Message

while [ "1" == "1" ]
do
 echo ${error_message} >> ${log_file}
 sleep 3m
 echo ${recovery_message} >> ${log_file}
done


