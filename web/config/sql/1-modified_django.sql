use django;
CREATE ALGORITHM=UNDEFINED DEFINER=`django`@`%` SQL SECURITY DEFINER VIEW `zabbix_temp_for_issue_trigger_name`
AS SELECT
   `zabbix_trigger_status`.`rowcreatedatetime` AS `rowcreatedatetime`,
   `zabbix_trigger_status`.`rowoperatedatetime` AS `rowoperatedatetime`,
   `zabbix_trigger_status`.`triggerid` AS `triggerid`,
   `zabbix_trigger_status`.`triggervalue` AS `triggervalue`,
   `zabbix_trigger_status`.`triggername` AS `triggername`,
   `zabbix_trigger_status`.`itemid` AS `itemid`,
   `zabbix_trigger_status`.`applicationname` AS `applicationname`,
   `zabbix_trigger_status`.`hostname` AS `hostname`
FROM `zabbix_trigger_status` where ((`zabbix_trigger_status`.`applicationname` <> 'HOST') and (`zabbix_trigger_status`.`triggervalue` = '1')) order by `zabbix_trigger_status`.`rowoperatedatetime`;
CREATE ALGORITHM=UNDEFINED DEFINER=`django`@`%` SQL SECURITY DEFINER VIEW `zabbix_issue_trigger_name`
AS SELECT
   `zabbix_temp_for_issue_trigger_name`.`applicationname` AS `applicationname`,
   `zabbix_temp_for_issue_trigger_name`.`triggername` AS `triggername`
FROM `zabbix_temp_for_issue_trigger_name` group by `zabbix_temp_for_issue_trigger_name`.`applicationname`;
CREATE ALGORITHM=UNDEFINED DEFINER=`django`@`%` SQL SECURITY DEFINER VIEW `zabbix_subsystemname`
AS SELECT
   `a`.`applicationname` AS `applicationname`,sum(`a`.`triggervalue`) AS `triggervalue`,
   `b`.`triggername` AS `triggername`
FROM (`zabbix_trigger_status` `a` left join `zabbix_issue_trigger_name` `b` on((`a`.`applicationname` = `b`.`applicationname`))) where (`a`.`applicationname` <> 'HOST') group by `a`.`applicationname`;