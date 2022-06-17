#!/usr/bin/python3
"""This script is used to add a user, create directories inside the home directory
   and then add files to those directories across three separate servers from a JSON file"""

import paramiko
import os
import json
import datetime

def main():
    """Our runtime code that calls other functions"""
    # list of servers pulled in from JSON file
    with open("server_list.json") as server_list:
        servers = json.load(server_list)

    # new directories being pulled in from JSON file and set as a variable
    new_dirs = servers["new_dirs"]

    # new files being pulled in from JSON file and set as a variable
    new_docs = servers["new_docs"]

    # harvest private key for all 3 servers
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    # input for any new users to be created
    new_users = input("What user(s) would you like to add?\n>").split(" ")

    # loop across the collection servers as it is pulled it from JSON and set as a variable
    for server in servers["servers"]:
        ## create a session object
        sshsession = paramiko.SSHClient()

        ## add host key policy
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ## display our connections
        print("Connecting to... " + server.get("un") + "@" + server.get("ip"))

        ## make a connection
        sshsession.connect(hostname=server.get("ip"), username=server.get("un"), pkey=mykey)

        # loops through the new_dirs list
        for dirs in new_dirs:
            # makes a directory in /etc/skel/ for each of the items in the list
            sshsession.exec_command(f"sudo mkdir /etc/skel/{dirs}/")
            # loops through the new_docs list
            for doc in new_docs:
                # adds each file from new_docs into each of the directories in new_dirs
                sshsession.exec_command(f"sudo touch /etc/skel/{dirs}/{doc}")
                # modifies authorities on each of the new files to rwxr-xr-x
                sshsession.exec_command(f"sudo chmod 0755 /etc/skel/{dirs}/{doc}")

        # for every new user that was input, adding that user to all three servers
        for user in new_users:
            sshsession.exec_command("sudo useradd -m " + user)

        ## list the contents of each home directory
        sessin, sessout, sesserr = sshsession.exec_command("ls /home/")

        # converts datetime into a string for later use
        x = str(datetime.datetime.now())

        ## display output to a file, log.txt
        with open("log.txt", "a") as log:
            # loops through new_users
            for user in new_users:
                # runs ls for the home directory of all new users
                sessin, sessout, sesserr = sshsession.exec_command(f"ls /home/{user}")
                # writes the current datetime
                log.write(x)
                # writes username
                log.write(f"\n{user}: \n")
                #writes the results from the ls command
                log.write(sessout.read().decode('utf-8'))

        ## close/cleanup SSH connection
        sshsession.close()


if __name__ == "__main__":
    main()
