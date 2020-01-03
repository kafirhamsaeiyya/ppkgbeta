#! /bin/bash

mkdir ~/bin/
export PATH=$PATH':$HOME/bin'
echo "export PATH=$PATH':$HOME/bin'" >> ~/.bashprofile
echo "export PATH=$PATH':$HOME/bin'" >> ~/.bashrc
cp ppkg ~/bin/
chmod +x ~/bin/ppkg
