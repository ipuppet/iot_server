WORK_DIR=$(
    cd $(dirname $0)
    pwd
)

cd $WORK_DIR

image_name=cits5506-server
db_file=$WORK_DIR/db.sqlite3

docker container stop $image_name
docker container rm $image_name
docker build -t $image_name .
if [ ! -f $db_file ]; then
    touch $db_file
fi
docker run -d -p 8090:8000 -v $db_file:/app/db.sqlite3 --name $image_name $image_name
docker exec -t $image_name bash -c "/app/resetdb.sh"
