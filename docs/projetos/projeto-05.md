# Projeto da Aula 05

## 🚀 Projeto da Aula: Conflito no Portfólio

Vamos criar um conflito controlado para perder o medo.

### Passo 1: O Cenário
1. No seu `meu-portfolio-git`, certifique-se de estar na `main` e sem pendências (`git status` limpo).
2. Crie uma branch `melhoria-texto`: `git switch -c melhoria-texto`.
3. Abra o `sobre.txt`. Mude a linha do seu nome para: "Nome: [Seu Nome] - Desenvolvedor Full Stack".
4. Salve e commite: `git commit -am "Melhora descrição na branch"`.

### Passo 2: A Divergência
1. Volte para a `main`: `git switch main`.
2. Abra o `sobre.txt`. Note que a mudança acima não está lá.
3. Mude a linha do seu nome para: "Nome: [Seu Nome] - Especialista em Git".
4. Salve e commite: `git commit -am "Muda descrição na main"`.

### Passo 3: O Conflito
1. Tente unir as branches: `git merge melhoria-texto`.
2. **BOOM!** `Merge conflict in sobre.txt`.

### Passo 4: A Resolução
1. Abra `sobre.txt`. Veja a confusão.
2. Decida como você quer se apresentar. Talvez unir os dois?
   "Nome: [Seu Nome] - Desenvolvedor Full Stack e Especialista em Git".
3. Apague as linhas de controle (`<<<`, `===`, `>>>`).
4. Salve.
5. No terminal: `git add sobre.txt`.
6. `git commit`. (Pode deixar a mensagem padrão).
7. Pronto! Histórico unificado e paz restaurada.
