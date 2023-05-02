import ftplib
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

ftp = ftplib.FTP()
ip = input(colored("[!] Your Ftp Server Ip : ", 'green'))
username = input(colored("[!] Your Ftp Username: ", 'green'))
password = input(colored("[!] Your Ftp Password: ", 'green'))
port = int(input(colored("[!] Enter Ftp Port: ", "green")))
ftp.connect(ip, port=port)
ftp.login(username, password)
ftp.cwd('/')
print(ftp.dir())

filename = input(colored("[+] input file name: ", 'blue'))
with open(filename, 'wb') as f:
      ftp.retrbinary('RETR ' + filename, f.write)
ftp.quit()
