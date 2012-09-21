#!/bin/bash
set -e
LOGFILE=/var/log/gunicorn/notyourmotleycrew.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
# user/group to run as
USER=oivvio
GROUP=oivvio
cd /home/oivvio/notyourmotleycrew
source /home/oivvio/.virtualenvs/notyourmotleycrew/bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec /home/oivvio/.virtualenvs/notyourmotleycrew/bin/gunicorn_django -w $NUM_WORKERS  --user=$USER --group=$GROUP --log-level=debug  --log-file=$LOGFILE 2>>$LOGFILE
