"""
User model
"""
from sqlalchemy import Column, Integer, String
from db_config import Base


class User(Base):
    """
    User model
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True)
    full_name = Column(String)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    @classmethod
    def create_user(cls, session, username, email):
        """
        # Public method to create a new user
        :param session:
        :param username:
        :param email:
        :return:
        """
        user = cls(username=username, email=email)
        session.add(user)
        session.commit()
        return user

    @classmethod
    def get_user_by_username(cls, session, username):
        """
        Public method to get a user by their username
        :param session:
        :param username:
        :return:
        """
        return session.query(cls).filter(cls.username == username).first()

    def update_email(self, session, new_email):
        """
        Public method to update a user's email
        :param session:
        :param new_email:
        :return:
        """
        self.email = new_email
        session.commit()
