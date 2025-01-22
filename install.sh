#!/bin/bash

sudo curl -L -o awake "https://github.com/dertfin0/awake-linux/releases/download/1.2/awake-linux"
sudo chmod +x awake
sudo mv -f awake /usr/local/bin/

echo "Installation was successful!"
echo "Restart terminal & run 'awake' command to run program"
