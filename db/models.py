from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Text, Table
from .base import metadata
from datetime import datetime


users = Table("user", metadata,
              Column("id", Integer, primary_key=True, autoincrement=True, unique=True),
              Column("username", String, nullable=False, unique=True),
              Column("name", String, nullable=False),
              Column("lastname", String, nullable=False),
              Column("hashed_password", String, nullable=False),
              Column("created_at", DateTime, default=datetime.now()),
              Column("updated_at", DateTime, default=datetime.now()),
              )

# class User(Base):
#     __tablename__ = "user"
#     id = Column(Integer, primary_key=True)
#     username = Column(String, nullable=False, unique=True)
#     name = Column(String, nullable=False)
#     lastname = Column(String, nullable=False)
#     hashed_password = Column(String, nullable=False)
#     created_at = Column(DateTime, default=datetime.now())
#     updated_at = Column(DateTime, default=datetime.now())

# jobs_accepted = relationship("Job", back_populates="users", uselist=True)


# class Company(Base):
#     __tablename__ = "company"
#     id = Column(Integer, primary_key=True)
#     title = Column(String, nullable=False, unique=True)
#
#     company_jobs = relationship("Job", back_populates="company", uselist=True)
#
#
# class Job(Base):
#     __tablename__ = "job"
#     id = Column(Integer, primary_key=True)
#     title = Column(String, nullable=False)
#     company_id = Column(Integer, ForeignKey("company.id"))
#     users_id = Column(Integer, ForeignKey('user.id'))
#     description = Column(Text)
#     is_active = Column(Boolean, default=True)
#     created_at = Column(DateTime, default=datetime.now())
#     updated_at = Column(DateTime, default=datetime.now())
#
#     users = relationship(
#         User,
#         primaryjoin=foreign(users_id) == remote(User.id),
#         uselist=True
#     )
#     company = relationship(
#         Company,
#         primaryjoin=foreign(company_id) == remote(Company.id),
#         uselist=False
#     )
