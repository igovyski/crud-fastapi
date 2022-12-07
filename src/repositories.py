from sqlalchemy.orm import Session

from models import Aluno

class AlunoRepository:
    @staticmethod
    def find_all(db: Session) -> list[Aluno]:
        return db.query(Aluno).all()

    @staticmethod
    def save(db: Session, aluno: Aluno) -> Aluno:
        if aluno.id:
            db.merge(aluno)
        else:
            db.add(aluno)
        db.commit()
        return aluno
    
    @staticmethod
    def find_by_id(db: Session, id: int) -> Aluno:
        return db.query(Aluno).filter(Aluno.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Aluno).filter(Aluno.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        aluno = db.query(Aluno).filter(Aluno.id == id).first()
        if aluno is not None:
            db.delete(aluno)
            db.commit()