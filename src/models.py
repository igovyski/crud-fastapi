from sqlalchemy import Column, Integer, String

from database import Base

class Aluno(Base):
    __tablename__ = 'alunos'
    id: int = Column(Integer, primary_key=True, index=True)
    nome: str = Column(String(100), nullable=False)
    idade: int = Column(Integer, nullable=False)
    rg: int = Column(Integer, nullable=False)
    curso: str = Column(String(100), nullable=False)
    semestre: int = Column(Integer, nullable=False)