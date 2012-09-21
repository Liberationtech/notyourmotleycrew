scriptname=$1
home="/home/oivvio"
activate="/home/oivvio/.virtualenvs/notyourmotleycrew/bin/activate"
root="/home/oivvio/notyourmotleycrew"
/bin/bash -c "source $activate && cd $root && ./manage.py runscript $scriptname"
