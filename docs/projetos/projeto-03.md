# Projeto da Aula 03

## 🚀 Projeto da Aula: Primeiro Commit no Portfólio

Agora vamos oficializar nosso projeto.

### Passo 1: Inicializar
1. No terminal, dentro da pasta `meu-portfolio-git`.
2. Execute:
   ```bash
   git init
   ```
   *Terminal deve responder*: `Initialized empty Git repository in...`

### Passo 2: Verificar Estado
1. Execute:
   ```bash
   git status
   ```
   *Terminal*: Mostrará `sobre.txt` em vermelho (Untracked files).

### Passo 3: Preparar (Staging)
1. Execute:
   ```bash
   git add sobre.txt
   ```
2. Execute `git status` novamente.
   *Terminal*: Mostrará `sobre.txt` em verde (Changes to be committed).

### Passo 4: Commitar (Salvar)
1. Execute:
   ```bash
   git commit -m "Cria arquivo inicial sobre mim"
   ```
   *Terminal*: `[master (root-commit)...] 1 file changed...`

### Passo 5: Conferir
1. Execute:
   ```bash
   git log
   ```
   Você verá seu nome, email, data e a mensagem do commit. Parabéns, seu projeto está versionado!
