# -*- coding: utf-8 -*-
"""
Author: Lu Bin
Contact:blu@cm-topsci.com
Reference Link: http://www.cnblogs.com/justbio/p/6293279.html
"""

# This python shellscript only used in python 2.7
# Import the Django runtime environment and initialize it
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard.settings')
django.setup()

# Import zabbix module
from zabbix_api import ZabbixAPI
from zabbix.models import Trigger_status

# Import configuration module
import ConfigParser
import ast

import time


# Get the host_id of hostname
def get_host_id(host_name):
    return zapi.host.get({"filter": {"host": host_name}})[0]["hostid"]


# According to host_id to get the trigger id, state and explain and get the item value of the item
def get_trigger_list_info(hostid):
    trigger_list = []
    trigger_value = []
    trigger_description = []
    trigger_itemid_row = []
    trigger_itemid_list = []
    trigger_itemid = []
    #trigger_eventid_row = []
    trigger_priority = []
    trigger_comment = []
    #trigger_eventid = []
    trigger_lastchange = []
    application_row = []
    application_name = []

    # Handle the trigger information
    temp = zapi.trigger.get({"filter": {"hostid": hostid}, "selectItems": "short"})
    for k in range(len(temp)):
        trigger_list.append(temp[k]["triggerid"])
        trigger_value.append(temp[k]["value"])
        trigger_description.append(temp[k]["description"])
        trigger_itemid_row.append(temp[k]["items"])
        trigger_priority.append(temp[k]["priority"])
        trigger_comment.append(temp[k]['comments'])
        trigger_lastchange.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(temp[k]["lastchange"]))))

    for k in range(len(trigger_itemid_row)):
        trigger_itemid_list.append([tempid['itemid'] for tempid in trigger_itemid_row[k]])
    for k in range(len(trigger_itemid_list)):
        trigger_itemid.append(trigger_itemid_list[k][0])
    # Get the application information
    for k in range(len(trigger_itemid)):
        application_row.append(zapi.application.get({"itemids": trigger_itemid[k]}))
        application_name.append([tempname['name'] for tempname in application_row[k]])

    # Get the event information
    # for k in range(len(trigger_list)):
    #     trigger_eventid_row.append(zapi.event.get(
    #         {"objectids": trigger_list[k], "sortorder": "DESC", "sortfield": ["clock", "eventid"], "value": "1"})[0])
    #     trigger_eventid.append(trigger_eventid_row[k]['eventid'])
    # trigger_list_info = zip(trigger_list, trigger_value, trigger_description, trigger_itemid, application_name,
    #                         trigger_eventid, trigger_priority, trigger_comment, trigger_lastchange)

    trigger_list_info = zip(trigger_list, trigger_value, trigger_description, trigger_itemid, application_name,
                            trigger_priority, trigger_comment, trigger_lastchange)

    return trigger_list_info


def update_mysql(triggerid, triggervalue, triggername, triggerapplicationname, triggeritemid, host_name,
                 priority, comment, lastchange):
    Trigger_status.objects.update_or_create(triggerid=triggerid,
                                            defaults={"triggervalue": triggervalue, "triggername": triggername,
                                                      "applicationname": triggerapplicationname, "hostname": host_name,
                                                      "itemid": triggeritemid,
                                                      "triggerpriority": priority, "triggercomment": comment,
                                                      "triggerlastchange": lastchange},
                                            )


if __name__ == '__main__':

    # Initialize external parameters
    cf = ConfigParser.ConfigParser()
    cf.read("get_zabbix_info.conf")
    hostnames = ast.literal_eval(cf.get("host", "hostnames"))
    zapi = ZabbixAPI(server=cf.get("server", "serveraddress"))
    zapi.login(cf.get("userconfig", "user"), cf.get("userconfig", "password"))

    for hostname in hostnames:
        hostid = get_host_id(hostname)
        triggerinfos = get_trigger_list_info(hostid)

        for triggerinfo in triggerinfos:
            update_mysql(triggerinfo[0], triggerinfo[1], triggerinfo[2], triggerinfo[4][0],
                         triggerinfo[3], hostname, triggerinfo[5], triggerinfo[6],
                         triggerinfo[7])
