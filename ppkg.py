import json
import os
import argparse
import sys


home = os.path.expanduser("~")
command = "export PATH=$PATH':$HOME/bin'"

parser = argparse.ArgumentParser(description="Package manager for BASH")

parser.add_argument('JSONpath', metavar="path of JSON file", type=str, help="path of the JSON file");

args = parser.parse_args();
pkg = json.load(open(args.JSONpath));

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

