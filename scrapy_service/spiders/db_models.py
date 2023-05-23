from sqlalchemy import Column, Integer, Date, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CommonColumnsMixin:
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    value = Column(Float)


class TgeBase(Base, CommonColumnsMixin):
    __tablename__ = 'tge_base'


class TgePeak(Base, CommonColumnsMixin):
    __tablename__ = 'tge_peak'


class TgeOffPeak(Base, CommonColumnsMixin):
    __tablename__ = 'tge_off_peak'


class Tge24(Base, CommonColumnsMixin):
    __tablename__ = 'tge_24'


class Tge15(Base, CommonColumnsMixin):
    __tablename__ = 'tge_15'


class Tge9(Base, CommonColumnsMixin):
    __tablename__ = 'tge_9'
