# Solução – Exercícios da Aula 04

Aqui você encontra as respostas sugeridas para os exercícios de Branches e Merges da Aula 04.

### 1. Explorando as Ramificações
O comando para listar as branches é:
```bash
git branch
```
A branch atual estará marcada com um asterisco (`*`) e geralmente em uma cor diferente (verde no Git Bash).

### 2. Criando uma Nova Realidade
Para criar:
```bash
git branch feature-teste
```
Para trocar:
```bash
git switch feature-teste
```

### 3. Trabalho Isolado
Ao voltar para a `main`, o arquivo `segredo.txt` **não** aparece. Isso ocorre porque os arquivos no Git estão vinculados à branch atual. Como o commit do arquivo foi feito apenas na linha do tempo `feature-teste`, a branch `main` ainda não conhece essa alteração.

### 4. A Fusão (Merge)
Para unir as branches:
```bash
git merge feature-teste
```
Após o comando, o Git traz os commits da `feature-teste` para a `main`, e o arquivo `segredo.txt` passa a existir fisicamente na sua pasta enquanto você estiver na `main`.

### 5. Atalho Eficiente
O comando "tudo em um" é:
```bash
git switch -c ajuste-rapido
```
(O `-c` vem de *create*).
