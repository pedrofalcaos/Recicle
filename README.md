# Sistema Recicle

Sistema Recicle é uma aplicação de coleta e distribuição de materiais recicláveis. O sistema permite que doadores registrem doações de materiais recicláveis e fornecedores possam visualizá-las e aceitá-las.

## Índice
- [Funcionalidades](#funcionalidades)
- [Pré-requisitos](#pré-requisitos)
- [Como Executar](#como-executar)
- [Uso](#uso)
- [Estrutura do Código](#estrutura-do-código)
- [Contribuição](#contribuição)

## Funcionalidades

- **Cadastro de usuário**: Permite que tanto doadores quanto fornecedores se registrem como pessoa física ou jurídica.
- **Login**: Autenticação de usuários por meio de email e senha.
- **Cadastro de doação**: Doador pode cadastrar doações especificando o tipo de material, quantidade, endereço de coleta e data/hora disponíveis para retirada.
- **Visualização de doações**:
  - **Doador**: Visualiza as doações que cadastrou.
  - **Fornecedor**: Visualiza doações disponíveis e pode aceitá-las.
- **Aceitar doação**: Fornecedor pode aceitar doações disponíveis e registrar a aceitação no sistema.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter o seguinte instalado:

- Python 3.7 ou superior
- Pip (gerenciador de pacotes do Python)

### Instalação de Dependências

Você pode instalar as dependências necessárias executando o seguinte comando no terminal:

```bash
pip install -r requirements.txt
No momento, não há bibliotecas externas utilizadas no projeto, então o arquivo requirements.txt pode estar vazio.

Como Executar
Clone o repositório ou baixe os arquivos diretamente.

Abra o terminal e navegue até o diretório onde o projeto está localizado.

Execute o sistema com o seguinte comando:

bash
Copiar código
python recicle_system.py
O sistema será iniciado e apresentará o menu principal no terminal.
Uso
Ao executar o sistema, você verá um menu principal com as seguintes opções:

Menu Principal
1. Login: Permite que usuários existentes façam login.
2. Cadastrar Usuário: Permite que novos usuários se cadastrem.
3. Sair: Fecha o sistema.
Cadastro de Usuário
No cadastro de usuário, você deverá escolher:

Se o usuário é um Doador ou Fornecedor.
Se é Pessoa Física (CPF) ou Pessoa Jurídica (CNPJ).
Após inserir as informações pessoais, como nome, email, senha, telefone e endereço, o usuário será cadastrado com sucesso.
Login
Usuários devem inserir um email e senha válidos para acessar o sistema.
Após o login, o menu exibido dependerá do tipo de usuário:
Doador:
Cadastrar doação
Visualizar doações cadastradas
Fornecedor:
Visualizar e aceitar doações disponíveis
Visualizar doações já aceitas
Cadastro de Doação
O doador pode cadastrar uma nova doação, especificando:
Tipo de material
Quantidade em kg
Endereço de coleta
Data e hora disponíveis para retirada
Aceitar Doação
O fornecedor pode visualizar as doações disponíveis e escolher aceitar aquelas que lhe interessam. Uma vez aceita, a doação é marcada como "Aceito" e o nome do fornecedor é registrado.
Estrutura do Código
A estrutura do código é dividida em uma classe principal chamada SistemaRecicle, que contém as funções para manipular o fluxo de dados e interações dos usuários. Abaixo estão as principais seções:

Funções de Cadastro e Login: Gerenciam o registro e a autenticação dos usuários.
Funções de Doação: Permitem o registro, visualização e aceitação de doações.
Funções de Validação: Garantem que os dados inseridos, como email, CPF/CNPJ, telefone e CEP, sejam válidos.
Persistência de Dados: Os dados são armazenados em um arquivo JSON (dados_recicle.json), que é carregado no início do programa e atualizado conforme as alterações no sistema.
Contribuição
Contribuições são bem-vindas! Para contribuir com o projeto:

Faça um fork do repositório.
Crie uma nova branch (git checkout -b feature/sua-feature).
Faça as alterações desejadas e commit (git commit -m 'Adiciona nova funcionalidade').
Faça um push para a branch criada (git push origin feature/sua-feature).
Abra um Pull Request no repositório original.
