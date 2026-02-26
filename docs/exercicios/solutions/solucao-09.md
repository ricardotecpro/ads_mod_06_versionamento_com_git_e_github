# Solução – Exercícios da Aula 09

Aqui você encontra as respostas sugeridas para os exercícios de GitHub Flow da Aula 09.

### 1. Sincronização Inicial
A sequência de comandos é:
```bash
git switch main
git pull origin main
```

### 2. Criação Expressa
O comando de atalho é:
```bash
git switch -c ajuste-texto
```

### 3. O Ciclo Completo
Após o merge bem-sucedido, a boa prática é **deletar a branch** no GitHub utilizando o botão "Delete branch" que aparece na página do Pull Request.

### 4. Faxina de Branches
Para deletar a branch local:
```bash
git branch -d ajuste-texto
```
*Dica*: Use `-D` (maiúsculo) se quiser forçar a deleção mesmo que o Git ache que o trabalho não foi totalmente integrado.

### 5. Limpando Rastros Remotos
O comando para sincronizar a lista de branches remotas e remover as que já foram deletadas no servidor é:
```bash
git fetch --prune
```
Ou, se quiser ser ainda mais específico: `git fetch origin --prune`.
