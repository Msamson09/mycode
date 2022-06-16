    #!/usr/bin/python3
"""This script is used to add a user, create directories inside the home directory
   and then add files to those directories across three separate servers"""

import paramiko
import os
import json

def main():
    """Our runtime code that calls other functions"""
    # list of servers
    servers = [
             {"un": "bender", "ip": "10.10.2.3"}, 
             {"un": "zoidberg", "ip": "10.10.2.5"},
             {"un": "fry", "ip": "10.10.2.4"}
            ]

    # new directories to be added
    new_dirs = ["lions", "tigers", "bears", "oh_my"]

    # new files to be put into each directory
    new_docs = ["dorothy.txt", "scarecrow.txt", "lion.txt", "tin_man.txt"]

    # harvest private key for all 3 servers
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    # input for any new users to be created
    new_users = input("What user(s) would you like to add?\n>").split(" ")

    # loop across the collection credz
    for server in servers:
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
            sshsession.exec_command("sudo useradd " + user)

        ## list the contents of each home directory
        sessin, sessout, sesserr = sshsession.exec_command("ls /home/" + server.get("un"))

        ## display output
        print(sessout.read().decode('utf-8'))

        ## close/cleanup SSH connection
        sshsession.close()


if __name__ == "__main__":
    main()
