WORK_DIR=$(
    cd $(dirname $0)
    pwd
)

cd $WORK_DIR

python manage.py makemigrations device automation
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'email@example.com', 'cits5506')" | python manage.py shell
