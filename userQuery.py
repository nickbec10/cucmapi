from cucmapi import axl, ris, ccs, log, cdr, pfm
import pandas as pd
import os

username = "adminuser"
password = "somecrazypw"
cucm = "44.12.44.12" #or IP address
cucm_version = "12.5"
AXL = axl(username=username, password=password, cucm=cucm, cucm_version=cucm_version) # for SOAP AXL
RIS = ris(username=username, password=password, cucm=cucm, cucm_version=cucm_version) # for RisPort70
CCS = ccs(username=username, password=password, cucm=cucm, cucm_version=cucm_version) # for Control Center Services
LOG = log(username=username, password=password, cucm=cucm, cucm_version=cucm_version) # for Log Collection
CDR = cdr(username=username, password=password, cucm=cucm, cucm_version=cucm_version) # for CDRonDemand
PFM = pfm(username=username, password=password, cucm=cucm, cucm_version=cucm_version) # for PerfMon
full = os.path.abspath(__file__ + "/../../../")
xls = pd.read_excel('file://'+full+'/users.xlsx', sheet_name='users')

# # test getting a single user
# user = AXL.getUser(userid="user1@org.com")
# print(user)

# Loops through a xls list of users and prints a message if user is not valid in CUCM
for _, row in xls.iterrows():
    user = AXL.getUser(userid=row.Users)
    try:  
        user.userid
    except:
        print(row.Users + " not valid")
