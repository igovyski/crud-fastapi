from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from models import Aluno
from database import engine, Base, get_db
from repositories import AlunoRepository
from schemas import AlunoRequest, AlunoResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ['http://127.0.0.1:5501']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Cadastrar alunos
@app.post('/api/alunos', response_model=AlunoResponse, status_code=status.HTTP_201_CREATED)
def create(request: AlunoRequest, db: Session = Depends(get_db)):
    aluno = AlunoRepository.save(db, Aluno(**request.dict()))
    return AlunoResponse.from_orm(aluno)

# Exibir todos os alunos cadastrados
@app.get('/api/alunos', response_model=list[AlunoResponse])
def find_all(db: Session = Depends(get_db)):
    alunos = AlunoRepository.find_all(db)
    return [AlunoResponse.from_orm(aluno) for aluno in alunos]

# Localizar aluno pelo id
@app.get('/api/alunos/{id}', response_model=AlunoResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    aluno = AlunoRepository.find_by_id(db, id)
    if not aluno:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Aluno não encontrado'
        )
    return AlunoResponse.from_orm(aluno)

# Excluir um aluno
@app.delete('/api/alunos/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not AlunoRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Aluno não encontrado'
        )
    AlunoRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Atualizar dados do aluno
@app.put('/api/alunos/{id}', response_model=AlunoResponse)
def update(id: int, request: AlunoRequest, db: Session = Depends(get_db)):
    if not AlunoRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Aluno não encontrado'
        )
    aluno = AlunoRepository.save(db, Aluno(id=id, **request.dict()))
    return AlunoResponse.from_orm(aluno)
