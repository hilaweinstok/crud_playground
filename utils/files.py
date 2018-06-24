import csv
from crud_playground.models import Catalog
from crud_playground.impl.erorrs import InvalidData, NoSuchFileError


def FromCSV(file_path):
    try:
        product = []
        with open(file_path) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                product.append(Catalog(idx=row['idx'],
                                       product_name=row['product_name'],
                                       photo_url=row['photo_url'],
                                       barcode=row['barcode'],
                                       price_cents=row['price_cents'],
                                       producer=row['producer']))
    except InvalidData:
        raise InvalidData
    except NoSuchFileError:
        raise NoSuchFileError
