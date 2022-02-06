import os

config = {
    'user': os.environ["MARIADB_USER"],
    'password': os.environ["MARIADB_ROOT_PASSWORD"],
    'host': os.environ["MARIADB_HOST"],
    'port': int(os.environ["MARIADB_PORT"]),
    'database': os.environ["MARIADB_DATABASE"]
}

URL = f"mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}?charset=utf8"
