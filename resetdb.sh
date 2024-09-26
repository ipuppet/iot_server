WORK_DIR=$(
    cd $(dirname $0)
    pwd
)

cd $WORK_DIR

rm db.sqlite3
rm -rf device/migrations
rm -rf automation/migrations

python manage.py makemigrations device automation
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'email@example.com', 'cits5506')" | python manage.py shell
