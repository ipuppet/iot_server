# CITS5506 IoT Project: Server

## Install Dependencies

Clone the repository and navigate to the `iot_server` directory.

```shell
git clone https://github.com/ipuppet/iot_server
cd iot_server
```

### Use Pip

```shell
pip install -r requirements.txt
```

### Use Docker

This will create a docker container named `cits5506-server`.

**Note:** The `build.sh` script will first remove any existing containers with the same name.

```shell
bash ./build.sh
docker exec -it cits5506-server bash
```

## Init Database

```shell
python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'email@example.com', 'cits5506')" | python manage.py shell
```

## Run Server

```shell
python manage.py runserver
```
