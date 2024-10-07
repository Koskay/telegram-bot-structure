import databases
import ormar
import sqlalchemy


engine = sqlalchemy.create_engine('db connect')

base_ormar_config = ormar.OrmarConfig(
    metadata=sqlalchemy.MetaData(),
    database=databases.Database('db connect'),
    engine=engine,
)


# Подключение к бд
async def db_connect() -> bool:
    base_ormar_config.metadata.create_all(engine)
    if not base_ormar_config.database.is_connected:
        await base_ormar_config.database.connect()
    return base_ormar_config.database.is_connected
