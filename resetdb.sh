WORK_DIR=$(
    cd $(dirname $0)
    pwd
)

cd $WORK_DIR

rm db.sqlite3
rm -rf device/migrations
rm -rf automation/migrations

./initdb.sh
