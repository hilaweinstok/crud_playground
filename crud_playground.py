import tornado.ioloop
import tornado.web

from crud_playground.impl.crud_config import CrudConfig


def Main():
    conf_file = "crud_playground/config/env_config.yaml"
    configurator = CrudConfig.FromFile(conf_file)
    app = configurator.CreateApp()
    app.listen(configurator.GetPort())
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    Main()
