# Aula 03 – Repositórios, commits e histórico

## 🎯 Objetivos de Aprendizagem
- Iniciar um repositório Git (`git init`).
- Entender as três áreas do Git: Working Directory, Staging Area e Repository.
- Realizar o primeiro commit (`git commit`).
- Visualizar o histórico de mudanças (`git log`).
- Verificar o estado dos arquivos (`git status`).

## 📚 Conteúdo

### 1. Inicializando um Repositório
Para transformar uma pasta comum em um projeto rastreado pelo Git:
```bash
git init
```
Isso cria uma pasta oculta `.git` onde toda a mágica acontece.

### 2. O Ciclo de Vida dos Arquivos (As 3 Áreas)
Entender isso é fundamental:
1. **Working Directory (Área de Trabalho)**: Onde você edita e cria arquivos.
2. **Staging Area (Área de Preparação)**: Uma área intermediária onde você escolhe o que vai entrar no próximo pacote (commit).
3. **Repository (Repositório/.git)**: Onde as versões confirmadas são salvas permamentemente.

### 3. Comandos Essenciais
- **`git status`**: O comando mais importante. Mostra em que estado seus arquivos estão (modificados, preparados ou commitados).
- **`git add <arquivo>`**: Move o arquivo do Working Directory para a Staging Area.
- **`git commit -m "mensagem"`**: Move o que está na Staging Area para o Repositório, criando uma "foto" definitiva daquela versão.

### 4. Git Log
Para ver a história do que aconteceu:
```bash
git log
```
Ele mostra o ID do commit (hash), o autor, a data e a mensagem.

## 📽 Roteiro de Slides
- O comando `git init`: Onde tudo começa.
- As 3 Áreas:
  - Working Directory (Sua mesa bagunçada)
  - Staging Area (A caixa pronta para envio)
  - Repository (O arquivo morto organizado)
- O fluxo básico: `Edit -> Add -> Commit`.
- Por que mensagens de commit importam?
- `git status`: Seu melhor amigo.
- `git log`: Olhando para o passado.

## 📝 Quiz
1. Qual comando transforma uma pasta em um repositório Git?
2. Para onde o comando `git add` envia os arquivos?
3. Qual a função do `git commit`?
4. O que o `git status` faz?
5. Qual comando mostra o histórico de commits?

## Gabarito
1: B
2: C
3: A
4: D
5: B

## 🛠 Exercícios
1. **Init**: Crie uma pasta `teste-git`, entre nela e rode `git init`.
2. **Status**: Rode `git status` e veja o que acontece.
3. **Criar e Adicionar**: Crie um arquivo `oi.txt`, rode `git add oi.txt`.
4. **Commitar**: Rode `git commit -m "Primeiro commit"`.
5. **Log**: Rode `git log` para ver seu feito registrado.

## 🚀 Projeto da Aula
Voltando ao nosso `meu-portfolio-git`:
1. Abra o terminal na pasta.
2. Digite: `git init`. (Agora é oficial!)
3. Digite: `git status`. (Veja o `sobre.txt` em vermelho/untracked).
4. Digite: `git add sobre.txt`.
5. Digite: `git status`. (Veja o arquivo verde/staged).
6. Digite: `git commit -m "Adiciona arquivo sobre mim"`.
7. Digite: `git log`. (Veja seu nome eternizado no histórico).
