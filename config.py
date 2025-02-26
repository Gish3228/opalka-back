class DatabaseParams:
    """
    Параметры подключения к бд
    """
    user = 'postgres'
    password = 'postgres'
    ip = 'localhost'
    port = 5432
    db_name = 'pig_db'
    sqlalchemy_uri = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}'.format(
        user=user,
        password=password,
        host=ip,
        port=port,
        db_name=db_name
    )


class MiscParams:
    """
    Разнообразные параметры
    """
    default_page = 1
