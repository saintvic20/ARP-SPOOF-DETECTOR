import os
import time

data=""
ldata=[]
fdata=[]
logs =[]
rerun = "yes"
#----------------------------------------------------------------------------------------------------------------------
#defined functions below:

#Function that extracts data from the arp -a command
def extract():
    global data, ldata

    with os.popen('arp -a') as f:
        data = f.read()

    with os.popen('arp -a') as a_file:
        for line in a_file:
            ldata.append (line.strip())
    del ldata[0:3]

#checks for duplicate MACs in the arp
def dictMACdup():
    global logs
    add_log = False
    logs=[]
    checkingDict = {}
    for key, value in addresses.items():
        checkingDict.setdefault(value, set()).add(key)

    global duplicate_mac_check
    duplicate_mac = [key for key, values in checkingDict.items() if len(values) > 1]

    for i in duplicate_mac:
        check = i in duplicate_mac_check
        if check == False:
            duplicate_mac_check.append(i)
            add_log =True

    log1 = f"Duplicate MACs: {duplicate_mac}"
    print(log1)

#will parse through duplicate_mac and convert to a string
    for i in duplicate_mac_check:
        duplicate_mac_string = str(i)
#will check if that specific string has a match in the checkingDict dictironary and pull out the values (the IPS that have that MAC dupplicated)
        if duplicate_mac_string in checkingDict.keys():
            mac_ips = checkingDict[duplicate_mac_string]
            print(duplicate_mac_string,"was duplicated in these IPs: ", mac_ips)
            if add_log == True:
                log2 =f"{duplicate_mac_string} was duplicated in these IPS: {mac_ips}"
                logs.append(log2)
                print("Log record was added to log.txt in current directory!")

def logfunction():
    for i in logs:
        logs_time = f"{current_time} {i}\n"
        print(logs_time)
        f = open("logs.txt", "a")
        f.write(logs_time)
        f.close

#-----------------------------------------------------------------------------------------------------------------------
#Code begins
duplicate_mac_check = []

while True:

    # current time
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    if rerun =="yes":
        extract()

        #this will check for any item in the list that starts with "I"
        check = 'I'
        res = [idx for idx in ldata if idx.lower().startswith(check.lower())]

        #this removes "Interface 192.168.56.1 --- 0xa internet physical type" from ldata list
        for i in ldata:
            if i in res:
                for i in res:
                    ldata.remove(i)

        #making ldata list into a string and adding a space (so strings aren't merged)
        ldata_str=""
        for elm in ldata:
            ldata_str += elm + " "

        #splitting the string into seprate words and putting the words in a list
        ldata_str =ldata_str.split()

        #removes "static" and "dynamic" from list
        while "static" in ldata_str:
            ldata_str.remove("static")

        while "dynamic" in ldata_str:
            ldata_str.remove("dynamic")

        print("ARP table: ",data)
        ip_list =[]
        mac_list=[]

        for i in range(0, len(ldata_str)):
            if i % 2:
                mac_list.append(ldata_str[i])
            else:
                ip_list.append((ldata_str[i]))

        addresses = dict(zip(ip_list, mac_list))
        dictMACdup()
        print("-------------------------------------------------------------------------------------------------------")
        print("Log(s): ")
        logfunction()

        print("(If no log entry shown but duplicate MACs were found, check log.txt in current directory for more info.)")
        print("(Logs already written, won't show in terminal...)")
        print("-------------------------------------------------------------------------------------------------------")

        print("\n")
        print("Enter 'yes' or 'no' to run program again.")
        rerun=input("Would you like to rerun?: ")
        rerun =rerun.lower()
        if rerun =="no":
            break
        elif rerun =="yes":
            pass
        else:
            print("Sorry must be 'yes' or 'no")
            while rerun != "yes" or rerun != "no":
                print("Enter 'yes' or 'no' to run program again.")
                rerun = input("Would you like to rerun?: ")
                rerun = rerun.lower()
                if rerun == "no":
                    break
                    rerun ="no"
                elif rerun == "yes":
                    break
                    rerun ="yes"
        if rerun =="no":
            break
        elif rerun =="yes":
            pass