class LoginAluno:
  def __init__ (self, id_usuario, senha):
    self.id_usuario = id_usuario
    self.senha = senha

print("====================TELA DE LOGIN DO ALUNO====================\n")

id_usuario = input("Aluno, Insira seu email ou nome do usuário: ")
senha = input("Agora, digite sua senha: ")

print("==============================================================\n")

class Forum:
  def __init__(self, titulo, descricao):
    self.titulo = titulo
    self.descricao = descricao

print("======================TELA DO FÓRUM======================\n")

titulo = input("Informe o título: ")
descricao = input("Sobre o que você deseja falar: ")

print("==========================================================\n")

class CadastroAluno:
  def __init__ (self, nomealuno, data_nascimentoaluno, sexoaluno, emailaluno, id_usuarioaluno):
    self.nomealuno = nomealuno
    self.data_nascimentoaluno = data_nascimentoaluno
    self.sexoaluno = sexoaluno
    self.id_usuarioaluno = id_usuarioaluno
    self.senhaaluno = senhaaluno
    self.emailaluno = emailaluno

print("====================TELA DO CADASTRO DO ALUNO====================\n")

nome = input("Aluno, Informe o seu nome: ")
data_nascimento = int(input("Digite sua Data de Nascimento: "))
sexo = input("Informe o sexo: ")
id_usuarioaluno = input("Aluno, Digite um nome para o usuário: ")
senha = input("Crie uma senha: ")
email = input("Informe o seu email: ")

print("=================================================================\n")

class LoginProf:
    def __init__(self, id_prof, senhap):
      self.id_prof = id_prof
      self.senhap = senhap

print("====================TELA DE LOGIN PARA PROFESSOR====================\n")

id_prof = input("Professor, Insira seu email ou nome do usuário: ")
senhap = int(input("Agora, digite sua senha: "))

print("====================================================================\n")

class CadastroProf:
  def __init__ (self, nomeprof, data_nascimentoprof, sexoprof, emailprof, id_usuarioprof, senhaprof):
    self.nomeprof = nomeprof
    self.data_nascimentoprof = data_nascimentoprof
    self.sexoprof = sexoprof
    self.id_usuarioprof = id_usuarioprof
    self.senhaprof = senhaprof
    self.emailprof = emailprof

print("====================TELA DE CADASTRO PARA PROFESSOR====================\n")

nomeprof = input("Professor, Informe o seu nome: ")
data_nascimentoprof = int(input("Digite sua Data de Nascimento: "))
sexoprof = input("Informe o sexo: ")
id_usuarioprof = input("Digite um nome para o usuário: ")
senhaprof = input("Crie uma senha: ")
emailprof = input("Informe o seu email: ")

print("=======================================================================\n")