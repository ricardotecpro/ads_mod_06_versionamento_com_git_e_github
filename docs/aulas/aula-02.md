# Aula 02 – Instalando e configurando o Git

## 🎯 Objetivos de Aprendizagem
- Instalar o Git no seu sistema operacional (Windows, Mac ou Linux).
- Configurar sua identidade (nome e email) no Git.
- Verificar se a instalação e configuração foram bem-sucedidas.
- Entender onde essas configurações ficam salvas.

## 📚 Conteúdo

### 1. Instalação

#### Windows
- Acesse [git-scm.com](https://git-scm.com).
- Baixe a versão para Windows.
- Execute o instalador.
- **Importante**: Na tela de escolha de editor, pode manter o padrão (Vim) ou mudar para VS Code se já tiver instalado. Nas outras opções, "Next" (Avançar) é seguro para iniciantes.
- Após instalar, procure por "Git Bash" no menu Iniciar. Esse será seu terminal principal.

#### macOS
- Se você tem o Homebrew instalado: `brew install git`.
- Ou baixe o instalador em [git-scm.com](https://git-scm.com).

#### Linux (Ubuntu/Debian)
- Abra o terminal e rode: `sudo apt-get update` e depois `sudo apt-get install git-all`.

### 2. Configuração Inicial (Obrigatória)
O Git precisa saber quem você é para atribuir a autoria das mudanças.

Abra o terminal (Git Bash no Windows) e execute:

```bash
git config --global user.name "Seu Nome Completo"
git config --global user.email "seu.email@exemplo.com"
```

> **Dica**: Use o mesmo email da sua conta GitHub.

### 3. Verificando as Configurações
Para ver se deu certo, digite:

```bash
git config --list
```

Você deve ver seu nome e email na lista que aparecerá. Pressione `Q` para sair da lista se ela for longa.

## 📽 Roteiro de Slides
- Download do Git (site oficial git-scm.com)
- Passo a passo da instalação (Windows: Next, Next, Next...)
- O Terminal: Git Bash (Windows) vs Terminal (Mac/Linux)
- Configuração de Identidade:
  - `git config --global user.name`
  - `git config --global user.email`
- Por que configurar? (Autoria e Segurança)
- Verificando tudo: `git config --list`

## 📝 Quiz
1. Qual o site oficial para baixar o Git?
2. Qual comando define seu nome de usuário no Git?
3. O que a opção `--global` faz nas configurações?
4. Qual terminal é instalado junto com o Git no Windows?
5. Como verificar as configurações atuais?

## Gabarito
1: B
2: A
3: C
4: D
5: B

## 🛠 Exercícios
1. **Instalação**: Baixe e instale o Git no seu computador.
2. **Setup de Identidade**: Configure seu nome e email corretamente.
3. **Validação**: Use o comando `git config --list` e tire um print ou anote o resultado para garantir que está correto.

## 🚀 Projeto da Aula
Voltando à pasta `meu-portfolio-git`:
1. Clique com o botão direito dentro da pasta.
2. Selecione "Open Git Bash here" (se estiver no Windows).
3. Digite `git --version` para confirmar que o Git está rodando DENTRO da sua pasta de projeto.
4. Ainda não vamos iniciar o repositório, apenas garantir que o terminal funciona no lugar certo.
