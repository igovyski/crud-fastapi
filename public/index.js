async function carregarAlunos(){
    const response = await axios.get('http://localhost:8000/api/alunos')
    
    const animais = response.data

    const lista = document.getElementById('tabela-alunos')

    lista.innerHTML = ''

    animais.forEach(aluno => {
        const item = document.createElement('li')
        const linha = `ID: ${aluno.id} | Nome: ${aluno.nome} | Idade: ${aluno.idade} | RG: ${aluno.rg} | Curso: ${aluno.curso} | Semestre: ${aluno.semestre}`
        item.innerText = linha
        lista.appendChild(item)
    });
}

function manipularFormulario(){
    const form_aluno = document.getElementById('form-aluno')
    const input_nome = document.getElementById('nome')
    const input_idade = document.getElementById('idade')
    const input_rg = document.getElementById('rg')
    const input_curso = document.getElementById('curso')
    const input_semestre = document.getElementById('semestre')

    form_aluno.onsubmit = async (event) => {
        event.preventDefault()

        await axios.post('http://localhost:8000/api/alunos', {
            nome: input_nome.value,
            idade: Number(input_idade.value),
            rg: input_rg.value,
            curso: input_curso.value,
            semestre: input_semestre.value
        })
        
        carregarAlunos()
        alert('Aluno Cadastrado')
    }
}

function updateAlunos(){
    const form_update = document.getElementById('form-update')
    const input_id = document.getElementById('id-update')
    const input_nome = document.getElementById('nome-update')
    const input_idade = document.getElementById('idade-update')
    const input_rg = document.getElementById('rg-update')
    const input_curso = document.getElementById('curso-update')
    const input_semestre = document.getElementById('semestre-update')

    form_update.onsubmit = async (event) => {
        event.preventDefault()

        await axios.put(`http://localhost:8000/api/alunos/${input_id.value}`, {
            id: Number(input_id.value),
            nome: input_nome.value,
            idade: Number(input_idade.value),
            rg: input_rg.value,
            curso: input_curso.value,
            semestre: input_semestre.value
        })
        
        carregarAlunos()
        alert('Aluno Atualizado')
    }
}

function deletarAluno(){
    const form_delete = document.getElementById('form-delete')
    const input_id = document.getElementById('delete_id')
    
    form_delete.onsubmit = async (event) => {
        event.preventDefault()

        await axios.delete(`http://localhost:8000/api/alunos/${input_id.value}`)
        
        carregarAlunos()
        alert('Aluno Deletado')
    }
}

function app(){
    console.log('App iniciado')
    carregarAlunos()
    manipularFormulario()
    updateAlunos()
    deletarAluno()
}

app()