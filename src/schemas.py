from pydantic import BaseModel

class AlunoBase(BaseModel):
    nome: str
    idade: int
    rg: int
    curso: str
    semestre: int

class AlunoRequest(AlunoBase):
    ...

class AlunoResponse(AlunoBase):
    id: int

    class Config:
        orm_mode = True