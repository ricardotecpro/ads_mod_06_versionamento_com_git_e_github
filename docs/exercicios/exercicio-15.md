# Exercícios da Aula 15

## 🛠 Exercícios

1. **Git Reflog (O Salvador)**:
   - Digite `git reflog`.
   - Você verá uma lista de tudo o que fez, mesmo os commits deletados ou perdidos em resets.
   - Se você fez um `git reset --hard` e se arrependeu, pode achar o hash anterior no reflog e voltar para ele.
   - Pratique: `git reset --hard <HASH-ANTERIOR-DO-REFLOG>`.

2. **Amend (Correção Rápida)**:
   - Commite um arquivo.
   - Lembre que esqueceu de adicionar outro arquivo nesse mesmo commit.
   - Dê `git add arquivo-esquecido`.
   - Dê `git commit --amend --no-edit` (o `--no-edit` mantém a mensagem original).
   - Agora o commit tem os dois arquivos.

3. **Stash (A Gaveta)**:
   - Você está trabalhando na branch `feature`, arquivo todo bagunçado.
   - Chefe pede: "Corrige um bug na main AGORA".
   - Você não quer commitar código quebrado.
   - Use `git stash`. O `git status` fica limpo.
   - Vá na main, corrija, volte.
   - Use `git stash pop` para trazer sua bagunça de volta.

## Dica
Aprender `reset`, `reflog` e `stash` te coloca no Top 10% dos usuários de Git. A maioria só sabe `add`, `commit` e `push`.
