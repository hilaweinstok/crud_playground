from sqlalchemy.orm.exc import NoResultFound
from tornado.web import RequestHandler, MissingArgumentError
from crud_playground.impl.erorrs import NoSuchFileError, NoSuchIdx
from crud_playground.models.catalog import Catalog
from crud_playground.utils.files import FromCSV


class CatalogHandler(RequestHandler):
    session_maker = None

    def initialize(self, *args, **kwargs):
        self.session_maker = kwargs["session_maker"]

    def get(self):
        session = self.session_maker()
        idx = self.get_argument("idx")

        try:
            product = Catalog.get_by_idx(session, idx)
            self.write(
                {
                    "status": 202,
                    "message": "data corresponding the idx you enter: {!s}".format(
                        product
                    ),
                }
            )
        except NoSuchIdx:
            self.write({"status": 404})
        finally:
            session.close()

    def post(self):
        session = self.session_maker()

        try:
            file_path = self.get_argument("file_path")
            product_obj = FromCSV(file_path)
            session.add(product_obj)
            session.commit()

        except MissingArgumentError:
            self.write({"status": 400, "message": "No such argument"})
        except NoSuchFileError:
            self.write({"status": 404, "message": "Are you sure the file exists?"})
        finally:
            session.close()

    def delete(self):
        session = self.session_maker()
        idx = self.get_argument("idx")
        try:
            product = Catalog.get_by_idx(session, idx)
            if product:
                session.delete(product)
                self.write(
                    {
                        "status": 204,
                        "message": "Product with idx {!s} has been deleted".format(idx),
                    }
                )
            session.commit()
        except NoSuchIdx:
            self.write({"status": 404})
        except NoResultFound:
            raise NoResultFound
        finally:
            session.close()
