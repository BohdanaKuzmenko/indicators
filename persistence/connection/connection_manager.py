from sqlalchemy.engine import create_engine, Engine
from sqlalchemy.engine.url import URL

from configuration.configuration_loader import ConfigLoader


class ConnectionManager:
    @staticmethod
    def create_db_engine() -> Engine:
        db_url = ConnectionManager._create_url()
        return create_engine(db_url, encoding="utf8", convert_unicode=True, pool_size=15, max_overflow=200)

    @staticmethod
    def _create_url():
        db_config = ConfigLoader().load_maria_db_config()
        return URL("postgresql",
                   db_config['username'],
                   db_config['password'],
                   db_config['host'],
                   db_config['port'],
                   db_config['dbname'])
