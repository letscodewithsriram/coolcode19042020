
#!/bin/bash

cd /home/tools/network-assess/coolcode19042020

git config --global user.email "sriram"
git config --global user.name "sriram.researcher@gmail.com"

git add *

git commit -m "`date`"

git push
