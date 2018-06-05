import tornado.ioloop
import tornado.web

from impl.crud_config import CrudConfig


def Main():
    db_url = 'mysql://user:password@port:8888'
    configurator = CrudConfig(db_url)
    app = configurator.CreateApp()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    Main()
