# Solução – Exercícios da Aula 15

Aqui você encontra as respostas sugeridas para os exercícios de Troubleshooting da Aula 15.

### 1. Recuperação Imediata
O comando para restaurar o arquivo é:
```bash
git restore index.html
```

### 2. Corrigindo a Mensagem
O comando é:
```bash
git commit --amend -m "feat: adiciona estrutura inicial"
```

### 3. O Poder do Reset Suave
As alterações **continuam na Staging Area (verde)**. O `reset --soft` apenas "desfaz" o ato do commit, mas mantém todo o seu trabalho pronto para ser commitado novamente (útil para mudar a mensagem ou agrupar arquivos).

### 4. Saindo do Limbo (Detached HEAD)
Para voltar ao estado normal, basta alternar novamente para uma branch nomeada:
```bash
git switch main
```

### 5. A Gaveta de Emergência (Stash)
- Para guardar: `git stash`
- Para listar o que está guardado: `git stash list`
- Para recuperar e remover da gaveta: `git stash pop`
- Para recuperar mantendo uma cópia na gaveta: `git stash apply`
