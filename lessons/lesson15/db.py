# from sqlalchemy import create_engine, MetaData, Table, Column, insert
# from sqlalchemy.types import Integer, Unicode, UnicodeText
# from sqlalchemy.schema import ForeignKey
#
# engine = create_engine("sqlite:///foo.db")
#
# metadata = MetaData()
# countries_table = Table("countries",
#                         metadata,
#                         Column('id', Integer, primary_key=True),
#                         Column('name', Unicode(255)),
#                         Column('code', Unicode(255)),
#                         Column('code2', Unicode(255)))
# indicators_table = Table("indicators",
#                          metadata,
#                          Column('id', Unicode(255), primary_key=True),
#                          Column('name', Unicode(255)))
# data_table = Table("data",
#                    metadata,
#                    Column('country_id', ForeignKey("countries.id")),
#                    Column('indicator', ForeignKey("indicators.id")),
#                    Column('data', UnicodeText))
# # metadata.create_all(engine)
# # OR
# countries_table.create(engine)
# # indicators_table.create(engine)
# # data_table.create(engine)
#
#
# conn = engine.connect()
# new_country = {'name': 'Canada', 'code': 'CAN'}
# country = insert(countries_table).values(new_country)
# print(country)
# conn.execute(country)
# conn.commit()
#
# # conn.execute("INSERT INTO countries (name, code) VALUES ('Ukraina', 'UKR')")
import random

from sqlalchemy import create_engine, Column, Integer, Unicode, UnicodeText, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///foo.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255))
    code = Column(Unicode(255))
    data = relationship("Data", back_populates="country")
    def __str__(self):
        return f"{self.id} {self.name} {self.code}"


class Indicator(Base):
    __tablename__ = 'indicators'
    id = Column(Unicode(255), primary_key=True)
    name = Column(Unicode(255))
    data = relationship("Data", back_populates="indicator")


class Data(Base):
    __tablename__ = 'data'
    country_id = Column(Integer, ForeignKey('countries.id'), primary_key=True)
    indicator_id = Column(Unicode(255), ForeignKey('indicators.id'), primary_key=True)
    data = Column(UnicodeText)
    country = relationship("Country", back_populates="data")
    indicator = relationship("Indicator", back_populates="data")


# Base.metadata.create_all(engine)


session = Session()
new_country = Country(name='Canada', code='CAN')
session.add(new_country)
print(new_country)
session.commit()

query = session.query(Country)
result = query.all()
import random
for row in result:
    row.name += str(random.randint(0,55))
    print(row)

session.commit()