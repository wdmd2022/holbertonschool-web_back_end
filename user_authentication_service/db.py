#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ method to add a User to our DB database"""
        user_to_add = User(email=email, hashed_password=hashed_password)
        self._session.add(user_to_add)
        self._session.commit()
        return user_to_add

    def find_user_by(self, **kwargs) -> User:
        """ returns the first user found by input arguments"""
        try:
            found_user = self._session.query(User).filter_by(**kwargs).first()
            if found_user is None:
                raise NoResultFound  # b/c no result returns None otherwise
        except InvalidRequestError:
            raise
        return found_user

    def update_user(self, user_id: int, **kwargs) -> None:
        """ updates a user in the DB"""
        user_to_update = self.find_user_by(id=user_id)
        for k, v in kwargs.items():
            if hasattr(user_to_update, k):
                setattr(user_to_update, k, v)
            else:
                raise ValueError
        self._session.commit()  # don't forget to save those changes!
