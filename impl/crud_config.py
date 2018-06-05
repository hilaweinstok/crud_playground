import tornado.ioloop
import tornado.web
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

from impl.handlers.catalog_handler import CatalogHandler


class CrudConfig(object):
    def __init__(self, db_url):
        self.session_maker = self.CreateSession(db_url)
        self.app = self.CreateApp()

    @staticmethod
    def CreateSession(db_url):
        engine = create_engine(db_url, echo=False)
        return sessionmaker(engine, autocommit=False, autoflush=False)

    def CreateApp(self):
        return tornado.web.Application([
            (r"/", tornado.web.RequestHandler),
            (r"/main_handler", CatalogHandler, dict(session_maker=self.session_maker))
        ])

    def GetTornadoApp(self):
        return self.app
