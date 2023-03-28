from PyQt5 import uic, QtWidgets
import sqlite3


def chama_segunda_tela():
    primeira_tela.label_4.setText("")
    nome_usuario = primeira_tela.lineEdit.text()
    senha = primeira_tela.lineEdit_2.text()
    banco = sqlite3.connect('banco_cadastro.db')
    cursor = banco.cursor()
    try:
        cursor.execute(f"SELECT senha FROM cadastro WHERE login = '{nome_usuario}'")
        senha_bd = cursor.fetchall()
        print(senha_bd[0][0])
        banco.close()
    except:
        print("Usuário ou senha inválidos")
    if senha == senha_bd[0][0]:
        primeira_tela.close()
        segunda_tela.show()
    else:
        primeira_tela.label.setText("Dados de login incorretos!")


def logout():
    segunda_tela.close()
    primeira_tela.show()


def abre_tela_cadastro():
    tela_cadastro.show()


def voltar_segunda_tela():
    tela_cadastro.close()
    segunda_tela.show()


def cadastrar():
    nome = tela_cadastro.lineEdit_2.text()
    email = tela_cadastro.lineEdit_6.text()
    login = tela_cadastro.lineEdit_3.text()
    senha = tela_cadastro.lineEdit_4.text()
    c_senha = tela_cadastro.lineEdit_5.text()

    if (senha == c_senha):
        try:
            banco = sqlite3.connect('banco_cadastro.db')
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text,email text, login text,senha text)")
            cursor.execute("INSERT INTO cadastro VALUES ('"+nome+"','"+email+"','"+login+"','"+senha+"')")

            banco.commit()
            tela_cadastro.label.setText("Usuário cadastrado com sucesso")
            banco.close()
        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ",erro)
    else:
        tela_cadastro.label.setText("As senhas digitadas estão diferentes")

app = QtWidgets.QApplication([])
primeira_tela = uic.loadUi("primeira_tela.ui")
segunda_tela = uic.loadUi("segunda_tela.ui")
tela_cadastro = uic.loadUi("tela_cadastro.ui")
primeira_tela.pushButton.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(logout)
primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
segunda_tela.pushButton_2.clicked.connect(abre_tela_cadastro)
tela_cadastro.pushButton.clicked.connect(cadastrar)
tela_cadastro.pushButton_2.clicked.connect(voltar_segunda_tela)

primeira_tela.show()
app.exec()