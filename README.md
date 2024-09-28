# CITS5506 IoT Project: Server

## Install Dependencies

Clone the repository and navigate to the `iot_server` directory.

```shell
git clone https://github.com/ipuppet/iot_server
cd iot_server
```

There are two ways to install the dependencies: using `pip` or using `docker`.

### Use Pip

```shell
pip install -r requirements.txt
```

#### Init Database

```shell
./initdb.sh
```

#### Reset Database

```shell
./resetdb.sh
```

#### Run Server

```shell
python manage.py runserver
```

### Use Docker

This will create a docker container named `cits5506-server`.

**Note:** The `build.sh` script will first remove any existing containers with the same name.

```shell
bash ./build.sh
```

This will automatically initialize the database if it does not exist.

#### Reset Database

```shell
bash ./build.sh reset
