db=$1
pw=$2
user=$db
echo $db $user $pw
tmpfile=$(mktemp)

echo "" > $tmpfile
echo "CREATE DATABASE $db CHARACTER SET utf8;" >> $tmpfile
echo "CREATE USER '$user'@'localhost' IDENTIFIED BY '$pw';" >> $tmpfile
echo "GRANT ALL PRIVILEGES ON $db.* TO '$user'@'localhost' WITH GRANT OPTION;" >> $tmpfile

mysql < $tmpfile
rm -f $tmpfile
