#!/usr/bin/python3
"""storage engine and use SQLAlchemy"""
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.exc import InvalidRequestError
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place


class DBStorage:

    """Data base storage"""

    __engine = None
    __session = None

    def __init__(self) -> None:
        username = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database_name = getenv("HBNB_MYSQL_DB")
        database_url = "mysql+mysqldb://{}:{}@{}/{}".format(username,
                                                            password,
                                                            host,
                                                            database_name)
        self.__engine = create_engine(database_url, pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ all"""
        zerz = []
        if cls:
            if isinstance(cls, str):
                try:
                    cls = globals()[cls]
                except KeyError:
                    pass
            if issubclass(cls, Base):
                zerz = self.__session.query(cls).all()
        else:
            for subclass in Base.__subclasses__():
                zerz.extend(self.__session.query(subclass).all())
        mezge = {}
        for obj in zerz:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            mezge[key] = obj
        return mezge

    def new(self, obj):
        """This for new"""
        self.__session.add(obj)
        self.__session.commit()

    def save(self):
        """This for save"""
        self.__session.commit()

    def delete(self, obj=None):
        """This for delet"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """This for reload"""
        Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        mabaza = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(mabaza)
        self.__session = Session()
