import os, sys

print ("\033[1;32mMasukin Password Sama Username Dulu Woy:)")
print ("\033[1;31;1mKalo Gak Tau Pm Gua 087788405277")
username = 'SYNT4X16'
password = 'LaguTermuxID'

def restart():
        ngulang = sys.executable
        os.execl(ngulang, ngulang, *sys.argv)

def main():
        uname = raw_input("username : ")
        if uname == username:
                pwd = raw_input("password : ")

                if pwd == password:
                        print "\n\033[1;34mHello Welcome To Tools-Valen"
                        sys.exit()

                else:
                        print "\n\033[1;36mSalah Goblok  !!!\033[00m"
                        print "Back Login\n"
                        restart()

        else:
                print "\n\033[1;36mSalah Bego  !!!\033[00m"
                print "Back Login\n"
                restart()

try:
        main()
except KeyboardInterrupt:
        os.system('clear')
        restart()
