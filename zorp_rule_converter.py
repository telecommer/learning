#!/usr/bin/env python3
import os
import re
with open("Public.txt" , "r") as fP1:
    zorp_rules = fP1.read()
fP1.close()
listed_zorpr=list(zorp_rules.split(" "))
#print(listed_zorpr)
rule = []
for info in listed_zorpr:
    in_ipv4=info.replace("DirectedRouter(SockAddrInet('", "inside_ip : ").replace("'","").replace(" ","").replace(",", "")
    out_ipv4=info.replace("Dispatcher(DBSockAddr(SockAddrInet('" , "outside_ip : ").replace("'","").replace("forge_addr=TRUE))", "").replace(" ", "").replace("\n","").replace(",", "") 
    #print(in_ipv4)
    #print(out_ipv4)
    exp = re.search("inside_ip" , in_ipv4)
    if exp:
        rule_prip = in_ipv4.replace("inside_ip:" , "").replace(",", "")
        rule.append(rule_prip)
    exp = re.search("outside_ip", out_ipv4)
    if exp:
       rule_puip = out_ipv4.replace("outside_ip:", "").replace(",", "")
       rule.append(rule_puip)
    exp = re.search(r"\d" , info)
    if exp:
        #print(info)
        port = info.replace(")", " : port").replace(",","")
        #print(port)
        if re.search(r"\d : port", port):
            rule_ports = port.replace(" : port", "")
            rule.append(rule_ports)
    
    tag = info.replace("')\n", " : tag").replace("'","")
    #print(tag)
    if re.search(" : tag", tag):
        rule_tag = tag.replace(" : tag", "\n")
        #print(rule_tag)
        rule.append(rule_tag)

    #if exp:
    #   print(info)
print(rule)

    