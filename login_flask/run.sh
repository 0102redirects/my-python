#!/bin/bash
if [ ! -n "$1" ]
then
    echo "Usages: sh uwsgiserver.sh [start|stop|restart]"
    exit 0
fi

if [ $1 = start ]
then
    psid=$(ps aux | grep -e "login_flask/uwsgi.ini" | grep -v grep | grep -v vim | grep -e "`whoami`\|`id -u`" | wc -l)
    if [ $psid -gt 4 ]
    then
        echo "uwsgi is running!"
        exit 0
    else
        nohup uwsgi /home/wjh/mysrc/my-python/login_flask/uwsgi.ini &
        echo "Start uwsgi service [OK]"
    fi
    

elif [ $1 = stop ];then
    killall -9 uwsgi
    echo "Stop uwsgi service [OK]"
elif [ $1 = restart ];then
    ps -ef | grep -e 'login_flask/uwsgi.ini' | grep -v grep | grep -v vim | grep -e "`whoami`\|`id -u`" | awk '{print $2}' | xargs -i kill -9 {}
    nohup uwsgi /home/wjh/mysrc/my-python/login_flask/uwsgi.ini &
    echo "Restart uwsgi service [OK]"

else
    echo "Usages: sh uwsgiserver.sh [start|stop|restart]"
fi
