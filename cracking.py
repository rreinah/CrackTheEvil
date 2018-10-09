from zipfile import ZipFile
from time import sleep
import sys
import colorama
zip_file_name = ["evil_plan_A.zip","evil_plan_B.zip","evil_plan_C.zip"]
password_files = ["0to1000.txt","1000to2000.txt","2000to3000.txt","3000to4000.txt","4000to5000.txt"]
passwords = []
item = 0

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

def getpasswords(password_files):
        for filep in password_files:
            with open(filep) as password_file:
                a = password_file.read().splitlines()
                passwords.extend(a) 

getpasswords(password_files)
for zip_file in zip_file_name:    
            for item, password in enumerate(passwords):
                    try: 
                        with ZipFile(zip_file) as zf:
                            zf.extractall(pwd=bytes(password,'utf-8'))
                            print("Trying " + zip_file + " with password #" + str(item) + " : " + password )
                            prGreen("#######################################")
                            prGreen("                 WIN!! :-)           ")
                            prGreen("                 " + password + "    ")
                            prGreen("#######################################")
                            sleep(5)
                            break
                    except:
                        prRed("Trying " + zip_file + " with password #" + str(item) + " : " + password + " : FAIL!")
                        pass


