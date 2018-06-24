import tornado.ioloop
import tornado.web
import yaml
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

from crud_playground.impl.handlers.catalog_handler import CatalogHandler


class CrudConfig(object):
    def __init__(self, db_url, port, env):
        self.session_maker = self.CreateSession(db_url)
        self.port = port
        self.env = env
        self.app = self.CreateApp()

    @staticmethod
    def CreateSession(db_url):
        engine = create_engine(db_url, echo=False)
        return sessionmaker(engine, autocommit=False, autoflush=False)

    @staticmethod
    def FromFile(file_name):
        with open(file_name, 'r') as f:
            config = yaml.load(f)
            return CrudConfig(db_url=config['DB_URL'],
                              port=config['PORT'],
                              env=config['ENV'])

    def CreateApp(self):
        return tornado.web.Application([
            (r"/", tornado.web.RequestHandler),
            (r"/catalog", CatalogHandler, dict(session_maker=self.session_maker))
        ])

    def GetTornadoApp(self):
        return self.app

    def GetPort(self):
        return self.port
