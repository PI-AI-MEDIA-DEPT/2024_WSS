#!/bin/bash
gunicorn --bind 0.0.0.0:8686 manageServer.wsgi:application --daemon &
#service nginx start &

  
# Exit with status of process that exited first
read var

