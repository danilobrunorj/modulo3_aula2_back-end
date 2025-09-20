# Lista de funcionários para cadastrar
funcionariosParaCadastrar = [
    {"nome": "Pablo", "sobrenome": "Araujo", "idade": 34, "altura": 1.71, "temHabilitacao": True},
    {"nome": "Ana", "sobrenome": "Silva", "idade": 28, "altura": 1.65, "temHabilitacao": False},
    {"nome": "Carlos", "sobrenome": "Souza", "idade": 40, "altura": 1.80, "temHabilitacao": True}
]

# Lista onde os objetos serão armazenados
cadastrosParaEnviarParaOBanco = []

# Classe Pessoa
class Pessoa:
    def __init__(self, nome, sobrenome, idade, altura, temHabilitacao):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.altura = altura
        self.temHabilitacao = temHabilitacao

# Função de cadastro
def cadastrar_funcionarios(lista_dicionarios, lista_objetos):
    for dados in lista_dicionarios:
        pessoa = Pessoa(
            nome=dados["nome"],
            sobrenome=dados["sobrenome"],
            idade=dados["idade"],
            altura=dados["altura"],
            temHabilitacao=dados["temHabilitacao"]
        )
        lista_objetos.append(pessoa)

# Função de salvar
def salvar_cadastros(lista_objetos):
    for pessoa in lista_objetos:
        print(f"O usuário {pessoa.nome} {pessoa.sobrenome} foi salvo com sucesso.")

# Executando as funções
cadastrar_funcionarios(funcionariosParaCadastrar, cadastrosParaEnviarParaOBanco)
salvar_cadastros(cadastrosParaEnviarParaOBanco)
