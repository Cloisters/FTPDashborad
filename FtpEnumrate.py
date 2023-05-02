import ftplib

# connect to the FTP server on port 21
ftp = ftplib.FTP()
ip = input("your ftp server ip : ")  
username = input("your ftp username: ")
password = input("your ftp password: ")
port = int(input("your port : "))
ftp.connect(ip, port=port)
ftp.login(username, password)

# set a file for download


# list files in the current directory
ftp.cwd('/')
print(ftp.dir())

filename = input("input file name: ")
with open(filename, 'wb') as f:
      ftp.retrbinary('RETR ' + filename, f.write)

# close the FTP connection
ftp.quit()