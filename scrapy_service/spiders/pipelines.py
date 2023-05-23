from datetime import datetime
from spiders.items import TGeElectricity
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session
from .db_engine import engine
from .db_models import (
    TgeBase,
    TgePeak,
    TgeOffPeak,
    Tge24,
    Tge15,
    Tge9
)


class TgePipeline:
    @classmethod
    def __init__(self):
        self.engine = engine
        self.session = Session(bind=self.engine)

    def process_item(self, item, spider):
        tge_electricity = TGeElectricity(item)

        table_mapping = {
            TgeBase.__tablename__: TgeBase,
            TgePeak.__tablename__: TgePeak,
            TgeOffPeak.__tablename__: TgeOffPeak,
            Tge24.__tablename__: Tge24,
            Tge15.__tablename__: Tge15,
            Tge9.__tablename__: Tge9,
        }

        try:
            TgeBase.metadata.create_all(bind=engine)
            TgePeak.metadata.create_all(bind=engine)
            TgeOffPeak.metadata.create_all(bind=engine)
            Tge24.metadata.create_all(bind=engine)
            Tge15.metadata.create_all(bind=engine)
            Tge9.metadata.create_all(bind=engine)

            with self.engine.connect() as connection:
                if connection.closed:
                    raise OperationalError(
                        "Connection error: connection was closed")

                for name, values in tge_electricity.items():
                    if name in table_mapping:
                        TableClass = table_mapping[name]
                        for date_string, value in values:
                            obj = TableClass()

                            current_year = datetime.now().year
                            day, month = map(int, date_string.split('-'))
                            obj.date = datetime(current_year, month,
                                                day).date()
                            obj.value = value

                            self.session.add(obj)
                            self.session.commit()
                    else:
                        raise ValueError("Unsupported type")

        except OperationalError as e:
            raise OperationalError("Connection error", + str(e))

    def close_spider(self, spider):
        self.client.close()
