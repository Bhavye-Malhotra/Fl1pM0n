#!/usr/bin/python3
from os import popen
import re
import requests as r
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.HEADER+
"""
'########:'##::::::::::'##:::'########::'##::::'##:::'#####:::'##::: ##:
 ##.....:: ##::::::::'####::: ##.... ##: ###::'###::'##.. ##:: ###:: ##:
 ##::::::: ##::::::::.. ##::: ##:::: ##: ####'####:'##:::: ##: ####: ##:
 ######::: ##:::::::::: ##::: ########:: ## ### ##: ##:::: ##: ## ## ##:
 ##...:::: ##:::::::::: ##::: ##.....::: ##. #: ##: ##:::: ##: ##. ####:
 ##::::::: ##:::::::::: ##::: ##:::::::: ##:.:: ##:. ##:: ##:: ##:. ###:
 ##::::::: ########::'######: ##:::::::: ##:::: ##::. #####::: ##::. ##:
..::::::::........:::......::..:::::::::..:::::..::::.....::::..::::..::
"""+bcolors.ENDC)

def basic_info(ip):
	print(bcolors.OKCYAN +"[+]"+bcolors.ENDC+"Processing output")

	data = {"Type": "undefined","Last Seen":"undefined", "Hostname":"undefined","MAC":"undefined","IP":"undefined" ,"OS":"undefined" }

	output = popen("sudo nmap -A -p- "+ip).read().split('\n')

	if ip.split('.')[0] == '10' or ip.split('.')[0] == '192':
		data["Type"] = 'Local'
	else:
		data["Type"] = 'Remote'

	data["Last Seen"]= time.ctime()

	print(bcolors.OKGREEN +"[+]"+ bcolors.ENDC +"Connection Type discovered")

	for line in output:
		if "Nmap scan report for" in line:
			data["hostname"] = line.split("for ")[-1].split(' ')[0]
			print(bcolors.OKBLUE+"[+]"+bcolors.ENDC +"Hostname found")
			data ["ip"] = line.split("for ")[-1].split(' ')[1].replace("(","").replace(")","")

		elif "Service Info: OS:" in line:
			#print(line.split(' '))
			if line.split(' ')[3]:
				#print(line.split(' ')[3])
				data["Operating System"] = line.split(' ')[3].replace(";","")
				print(bcolors.WARNING+"[+]"+bcolors.ENDC +"Operating System found")

		elif "MAC Address:" in line:
			if line.split(" ")[2]:
				data["MAC-Address"] = line.split(' ')[2]
				print(bcolors.WARNING+"[+]"+bcolors.ENDC +"MAC-Address found")
	return data


data = (basic_info('10.0.0.5'))

d = {"Type": data["Type"],"Last Seen":data["Last Seen"], "Hostname": data["hostname"],"MAC":data["MAC-Address"],"IP":data["ip"] ,"OS":data["Operating System"] }
#print(d)
response = r.post("http://20.198.79.186/users",data=d)
print(response.text)
