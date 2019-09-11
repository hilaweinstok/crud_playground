import tornado.ioloop
import tornado.web

from crud_playground.impl.crud_config import CrudConfig


def Main():
    conf_file = "crud_playground/config/env_config.yaml"
    configurator = CrudConfig.from_file(conf_file)
    app = configurator.create_app()
    app.listen(configurator.get_port())
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    Main()
