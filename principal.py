import re
import json
import os
from datetime import datetime


class SistemaRecicle:
    def __init__(self):
        self.usuarios = {}
        self.materiais = {
            1: "Plástico",
            2: "Papel",
            3: "Vidro",
            4: "Metal",
            5: "Outros"
        }
        self.descricoes_materiais = {
            "Plástico": "Materiais plásticos recicláveis.",
            "Papel": "Papéis e papelões recicláveis.",
            "Vidro": "Garrafas e outros itens de vidro.",
            "Metal": "Latas e outros metais recicláveis.",
            "Outros": "Outros tipos de materiais recicláveis."
        }
        self.proximo_id = 1
        self.arquivo_dados = "dados_recicle.json"

    def salvar_dados(self):
        try:
            with open(self.arquivo_dados, "w") as f:
                json.dump(self.usuarios, f, indent=4, default=str)
            print("Dados salvos com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")

    def carregar_dados(self):
        if os.path.exists(self.arquivo_dados):
            try:
                with open(self.arquivo_dados, "r") as f:
                    self.usuarios = json.load(f)
                print("Dados carregados com sucesso!")
            except Exception as e:
                print(f"Erro ao carregar dados: {e}")
        else:
            print("Arquivo de dados não encontrado. Iniciando com dados vazios.")

    def cadastrar_usuario(self):
        print("\nEscolha o tipo de cadastro:")
        print("1. Doador")
        print("2. Fornecedor")
        tipo_usuario = input("Digite o número correspondente ao tipo de usuário (1 ou 2): ").strip()

        if tipo_usuario == '1':
            tipo_usuario = "doador"
        elif tipo_usuario == '2':
            tipo_usuario = "fornecedor"
        else:
            print("Opção inválida. Tente novamente.")
            return

        print("\nVocê é:")
        print("1. Pessoa Física")
        print("2. Pessoa Jurídica")
        tipo_pessoa = input("Digite o número correspondente ao tipo de pessoa (1 ou 2): ").strip()

        if tipo_pessoa == '1':
            tipo_documento = "CPF"
        elif tipo_pessoa == '2':
            tipo_documento = "CNPJ"
        else:
            print("Opção inválida. Tente novamente.")
            return

        cpf_cnpj = self.solicitar_documento(tipo_documento)
        nome = input("Digite o nome completo (ou razão social): ").strip()

        email = self.solicitar_email()
        senha = self.criar_senha()
        telefone = self.solicitar_telefone()
        cep = self.solicitar_cep()
        logradouro = input("Digite o logradouro: ").strip()

        self.usuarios[email] = {
            "nome": nome,
            "email": email,
            "cpf_cnpj": cpf_cnpj,
            "tipo_usuario": tipo_usuario,
            "tipo_pessoa": "Pessoa Física" if tipo_pessoa == '1' else "Pessoa Jurídica",
            "telefone": telefone,
            "logradouro": logradouro,
            "cep": cep,
            "senha": senha,
            "doacoes": {}
        }
        self.salvar_dados()
        print("Usuário cadastrado com sucesso!")

    def login(self):
        email = input("Digite seu email: ").strip()
        senha = input("Digite sua senha: ").strip()

        usuario = self.usuarios.get(email)
        if usuario and usuario['senha'] == senha:
            print("Login efetuado com sucesso!")
            if usuario['tipo_usuario'] == "doador":
                self.menu_doador(email)
            else:
                self.menu_fornecedor(email)
        else:
            print("Email ou senha inválidos.")

    def menu_doador(self, email):
        while True:
            print("\nMenu do Doador:")
            print("1. Cadastrar Doação")
            print("2. Visualizar Doações")
            print("3. Sair")
            escolha = input("Escolha uma opção: ").strip()

            if escolha == '1':
                self.cadastrar_doacao(email)
            elif escolha == '2':
                self.visualizar_doacoes_doador(email)
            elif escolha == '3':
                break
            else:
                print("Opção inválida.")

    def menu_fornecedor(self, email):
        while True:
            print("\nMenu do Fornecedor:")
            print("1. Visualizar e Aceitar Doações Disponíveis")
            print("2. Visualizar Doações Aceitas")
            print("3. Sair")
            escolha = input("Escolha uma opção: ").strip()

            if escolha == '1':
                self.visualizar_e_aceitar_doacoes_disponiveis(email)
            elif escolha == '2':
                self.visualizar_doacoes_aceitas(email)
            elif escolha == '3':
                break
            else:
                print("Opção inválida.")

    def cadastrar_doacao(self, email):
        print("\nCadastrar Nova Doação:")
        for num, material in self.materiais.items():
            print(f"{num}. {material} - {self.descricoes_materiais.get(material, 'Outros')}")

        escolha_material = self.solicitar_material()
        quantidade = input("Digite a quantidade estimada do material (em kg): ").strip()
        endereco_coleta = input("Digite o endereço de coleta do material: ").strip()

        # Adicionando a data e hora para retirada da doação
        data_hora_retirada = input(
            "Digite a data e hora disponíveis para retirada (formato: dd/mm/yyyy hh:mm): ").strip()
        try:
            data_hora_retirada = datetime.strptime(data_hora_retirada, "%d/%m/%Y %H:%M")
        except ValueError:
            print("Formato de data e hora inválido. Tente novamente.")
            return

        doacao_id = self.proximo_id
        self.proximo_id += 1

        self.usuarios[email]['doacoes'][doacao_id] = {
            "tipo_material": escolha_material,
            "quantidade": quantidade,
            "endereco_coleta": endereco_coleta,
            "data_hora_retirada": data_hora_retirada.strftime("%d/%m/%Y %H:%M"),
            "status": "Disponível",
            "fornecedor": ""
        }
        self.salvar_dados()
        print("Doação cadastrada com sucesso!")

    def visualizar_doacoes_doador(self, email):
        """Visualizar doações cadastradas pelo doador."""
        doacoes = self.usuarios[email].get('doacoes', {})
        if doacoes:
            print("\nSuas Doações:")
            for doacao_id, doacao in doacoes.items():
                print(f"ID da Doação: {doacao_id}")
                print(f"Tipo de Material: {doacao['tipo_material']}")
                print(f"Quantidade: {doacao['quantidade']} kg")
                print(f"Endereço de Coleta: {doacao['endereco_coleta']}")
                print(f"Data e Hora para Retirada: {doacao['data_hora_retirada']}")
                print(f"Status: {doacao['status']}")
                if doacao['fornecedor']:
                    print(f"Fornecedor: {doacao['fornecedor']}")
                print("-" * 20)
        else:
            print("Você não possui doações cadastradas.")

    def visualizar_e_aceitar_doacoes_disponiveis(self, email):
        print("\nDoações Disponíveis para Aceitação:")
        doacoes_disponiveis = False
        for email_doador, dados_usuario in self.usuarios.items():
            for doacao_id, doacao in dados_usuario.get('doacoes', {}).items():
                if doacao['status'] == 'Disponível':
                    doacoes_disponiveis = True
                    print(f"ID da Doação: {doacao_id}")
                    print(f"Tipo de Material: {doacao['tipo_material']}")
                    print(f"Quantidade: {doacao['quantidade']} kg")
                    print(f"Endereço de Coleta: {doacao['endereco_coleta']}")
                    print(f"Data e Hora para Retirada: {doacao['data_hora_retirada']}")
                    print("-" * 20)

                    # Opção de aceitar a doação
                    aceitar = input(f"Deseja aceitar esta doação (ID {doacao_id})? (s/n): ").strip().lower()
                    if aceitar == 's':
                        doacao['status'] = 'Aceito'
                        doacao['fornecedor'] = self.usuarios[email]['nome']
                        self.salvar_dados()
                        print("Doação aceita com sucesso!")

        if not doacoes_disponiveis:
            print("Nenhuma doação disponível no momento.")

    def visualizar_doacoes_aceitas(self, email):
        print("\nDoações Aceitas:")
        doacoes_aceitas = False
        for email_doador, dados_usuario in self.usuarios.items():
            for doacao_id, doacao in dados_usuario.get('doacoes', {}).items():
                if doacao['status'] == 'Aceito' and doacao['fornecedor'] == self.usuarios[email]['nome']:
                    doacoes_aceitas = True
                    print(f"ID da Doação: {doacao_id}")
                    print(f"Tipo de Material: {doacao['tipo_material']}")
                    print(f"Quantidade: {doacao['quantidade']} kg")
                    print(f"Endereço de Coleta: {doacao['endereco_coleta']}")
                    print(f"Data e Hora para Retirada: {doacao['data_hora_retirada']}")
                    print("-" * 20)

        if not doacoes_aceitas:
            print("Nenhuma doação aceita.")

    def solicitar_material(self):
        while True:
            try:
                escolha_material = int(input("Digite o número correspondente ao tipo de material: ").strip())
                if escolha_material in self.materiais:
                    return self.materiais[escolha_material]
                else:
                    print("Material inválido. Por favor, escolha uma opção válida.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número correspondente.")

    def solicitar_documento(self, tipo):
        while True:
            cpf_cnpj = input(f"Digite o {tipo}: ").strip()
            if tipo == "CPF" and self.validar_cpf(cpf_cnpj):
                if not self.cpf_cnpj_existente(cpf_cnpj):
                    return cpf_cnpj
                else:
                    print(f"Já existe um usuário cadastrado com este {tipo}.")
            elif tipo == "CNPJ" and self.validar_cnpj(cpf_cnpj):
                if not self.cpf_cnpj_existente(cpf_cnpj):
                    return cpf_cnpj
                else:
                    print(f"Já existe um usuário cadastrado com este {tipo}.")
            else:
                print(f"{tipo} inválido. Por favor, digite um {tipo} válido.")

    def solicitar_email(self):
        while True:
            email = input("Digite o email: ").strip()
            if self.validar_email(email) and email not in self.usuarios:
                return email
            else:
                print("Email inválido ou já cadastrado.")

    def criar_senha(self):
        while True:
            senha = input("Crie uma senha: ").strip()
            if len(senha) > 5 and re.search(r'[0-9]', senha) and re.search(r'[A-Z]', senha):
                return senha
            else:
                print("Senha fraca. A senha deve ter mais de 5 caracteres, conter um número e uma letra maiúscula.")

    def solicitar_telefone(self):
        while True:
            telefone = input("Digite o telefone (com DDD): ").strip()
            if self.validar_telefone(telefone):
                return telefone
            else:
                print("Telefone inválido.")

    def solicitar_cep(self):
        while True:
            cep = input("Digite o CEP: ").strip()
            if self.validar_cep(cep):
                return cep
            else:
                print("CEP inválido.")

    def validar_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def validar_telefone(self, telefone):
        return re.match(r"^\d{2}\d{8,9}$", telefone) is not None

    def validar_cpf(self, cpf):
        cpf = ''.join(re.findall(r'\d', cpf))
        return len(cpf) == 11

    def validar_cnpj(self, cnpj):
        cnpj = ''.join(re.findall(r'\d', cnpj))
        return len(cnpj) == 14

    def validar_cep(self, cep):
        return re.match(r"^\d{5}-?\d{3}$", cep) is not None

    def cpf_cnpj_existente(self, cpf_cnpj):
        return any(usuario['cpf_cnpj'] == cpf_cnpj for usuario in self.usuarios.values())


# Função principal
def main_menu(sistema):
    sistema.carregar_dados()
    while True:
        print("\nBem-vindo ao Sistema Recicle")
        print("1. Login")
        print("2. Cadastrar Usuário")
        print("3. Sair")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            sistema.login()
        elif escolha == '2':
            sistema.cadastrar_usuario()
        elif escolha == '3':
            sistema.salvar_dados()
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    sistema = SistemaRecicle()
    main_menu(sistema)
