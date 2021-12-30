

Objective:  Get TLOG and BIN logs to generate MAP files


1) Install pymavlink - for TLOG treatment

git clone --recursive https://github.com/ArduPilot/pymavlink.git

sudo apt-get update

sudo apt-get install -y gcc python3-dev libxml2-dev libxslt-dev python3-numpy python3-pip gpsbabel zip

sudo DISABLE_MAVNATIVE=True python -m pip install --upgrade pymavlink

2) Install Mavproxy - for BIN treatment

sudo apt-get install python3-dev python3-opencv python3-wxgtk4.0 python3-pip python3-matplotlib python3-lxml python3-pygame
pip3 install PyYAML mavproxy --user
echo "export PATH=$PATH:$HOME/.local/bin" >> ~/.bashrc

