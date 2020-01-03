import json
import os

pkg = json.load(open("neofetch.json"));
home = os.path.expanduser("~")
command = "export PATH=$PATH':$HOME/bin'"
if(os.path.isdir(home + "/bin")):
    os.system(command)
    os.system("echo " + command + " >> ~/.bash_profile")
    os.system("echo " + command + " >> ~/.bashrc")

else:
    os.mkdir(home + "/bin")
    os.system(command);
    os.system("echo " + command + " >> ~/.bash_profile")
    os.system("echo " + command + " >> ~/.bashrc")

os.system("wget -P ~/bin/ " + pkg["url"]);
os.system("chmod +x ~/bin/" + pkg["package_name"])

