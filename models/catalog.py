from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import Table, Column, Integer, String, MetaData


class Catalog(object):
    def __init__(self, idx, product_name, photo_url, barcode, price_cents, producer):
        self.idx = idx
        self.product_name = product_name
        self.photo_url = photo_url
        self.barcode = barcode
        self.price_cents = price_cents
        self.producer = producer

    """
    Attributes:
        idx - Integer, unique identifier
        product_name - String, product name
        photo_url - String, url to product photo
        barcode - Integer, barcode number
        price_cents - Integer, price in cents
        producer - String, producer name
    """

    metadata = MetaData()
    catalog = Table('catalog', MetaData(bind=None),
                    Column('idx', Integer, nullable=False, index=True, unique=True),
                    Column('product_name', String(100), nullable=False),
                    Column('photo_url', String(100), nullable=True),
                    Column('barcode', Integer, nullable=False),
                    Column('price_cents', Integer, nullable=False),
                    Column('producer', String, nullable=True)
                    )

    @classmethod
    def GetByIdx(cls, session, idx):
        """
        Get all catalog data by idx
        session:  SQLAlchemy session object
        idx:  Unique id

        :return: Catalog model
        """
        try:
            return session.query(cls).filter(cls.idx == idx).one()
        except NoResultFound:
            raise NoResultFound

    @staticmethod
    def DeleteData(session, idx):
        try:
            product = Catalog.GetByIdx(session, idx)
            if product:
                session.delete(product)
        except NoResultFound:
            raise NoResultFound
