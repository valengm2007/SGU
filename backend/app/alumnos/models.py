from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Alumno(Base):
	__tablename__ = "alumnos"

	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String, nullable=False)
	email = Column(String, unique=True, nullable=False)
	edad = Column(Integer, nullable=False)
	legajo = Column(Integer, unique=True, nullable=True)
	legajo_provisorio = Column(Boolean, default=False)
