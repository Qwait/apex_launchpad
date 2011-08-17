from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from sqlalchemy import Unicode
from sqlalchemy import types
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import synonym
from sqlalchemy.sql import functions

from pyramid_apex.models import Base
from pyramid_apex.models import AuthUser

class ForeignKeyProfile(Base):
    __tablename__ = 'auth_user_profile'

    id = Column(types.BigInteger, primary_key=True)
    user_id = Column(types.BigInteger, ForeignKey(AuthUser.id), index=True)
    #parent_id = Column(types.BigInteger, ForeignKey(AuthUser.id))
    parent_id = Column(types.BigInteger)

    created = Column(types.DateTime(), default=functions.current_date())
    score = Column(types.BigInteger, default=0)

    user = relationship('AuthUser', backref=backref('profile', uselist=False))

