import subprocess
import os


#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# Edit the below variables
driver0_name = "Captain Chris0" #Put Driver 0 name here"
driver0_email = "captain.chris0.18@cnu.edu" # Driver 0 Email

driver1_name = "Captain Chris1" #Put Driver 1 name here"
driver1_email = "captain.chris1.18@cnu.edu" # Driver 1 Email
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


# Do not edit below this Line
# Find out the current email, convert to string, and strip whitespace (newline)
try:
    result_name = subprocess.check_output("git config --global user.name", shell=True).decode("utf-8").rstrip()
    result_email = subprocess.check_output("git config --global user.email", shell=True).decode("utf-8").rstrip()

    print()
    print("Current Git Configuration: "+result_name+" ("+result_email+")")
    if (result_email == driver0_email):
        print("Switch to Driver 1: "+driver1_name+" ("+driver1_email+")")
        os.system("git config --global user.name \""+driver1_name+"\"")
        os.system("git config --global user.email "+driver1_email)
    else:
        print("Switch to Driver 0: "+driver0_name+" ("+driver0_email+")")
        os.system("git config --global user.name \""+driver0_name+"\"")
        os.system("git config --global user.email "+driver0_email)
except Exception as e:
    print("Error: ", e)
    print()
    print("Current Git Config:")
    os.system("git config -l")

    print("\n\nResetting git config to {}".format(driver0_name))
    os.system("git config --global user.name \""+driver0_name+"\"")
    os.system("git config --global user.email "+driver0_email)
    os.system("git config -l")
    
