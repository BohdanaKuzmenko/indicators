import configparser
import os


class ConfigLoader:
    _APP_ENV_PATH = 'db.ini'
    config = configparser.ConfigParser()
    conf_dir = os.path.dirname(os.path.abspath(__file__))
    config.read( os.path.join(conf_dir, 'db.ini'))

    def load_maria_db_config(self):
        return self.config['db']