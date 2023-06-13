#!/bin/bash
/usr/bin/python3 /home/kiwi/project/plots/dailyplot.py >> /home/kiwi/logs/plots_log.txt 2>&1

cp /home/kiwi/project/plots/daily0.png /var/www/html/proto/graphs/daily0.png
