import paramiko #install to be able to connect via ssh: pip install paramiko
from colorama import Fore, Style #install for colored output: pip install colorama
from var import * #import variables
 
def add_user():
   #open session
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname[i],port,username,password)
    client.get_transport()
    #run linux one line commands
    linux_command =  f'sudo useradd {new_user} ; sudo usermod -aG {group_name} {new_user} && echo -e "{new_user_password}\n{new_user_password}" | sudo passwd {new_user}'
    stdin, stdout, stderr = client.exec_command(command=linux_command,get_pty=True)
    stdin.write(f"{password}\n")
    stdin.flush()

    if stderr.channel.recv_exit_status() != 0:
        print(f"{Fore.RED}Error occured on {hostname[i]}!")
    else:
        print(f"Host: {Fore.GREEN}{hostname[i]}{Style.RESET_ALL}\nCreated user: {Fore.GREEN}{new_user}{Style.RESET_ALL}\npassword: {Fore.GREEN}{new_user_password}{Style.RESET_ALL}\nadded to group: {Fore.GREEN}{group_name}{Style.RESET_ALL}\n/---------------------/")
    #close session
    client.close()
    
for i in range(len(hostname)):
    add_user()
    
