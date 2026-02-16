# Exercícios da Aula 11

## 🛠 Exercícios

1. **O Detetive de Commits**:
   - Vá no histórico de um projeto Open Source (ex: `facebook/react`).
   - Leia os títulos dos commits recentes.
   - Veja como eles usam tags como `[DevTools]`, `Fix`, etc.
   - Tente encontrar um commit ruim (é difícil em projetos grandes, mas acontece).

2. **Reescrevendo a História (Local)**:
   - Crie um arquivo `provisorio.txt`. Commite com mensagem "teste".
   - Crie um arquivo `esquece.txt`. Commite com mensagem "outro teste".
   - Use `git rebase -i HEAD~2` (Avançado, cuidado!).
   - Tente mudar a mensagem "teste" para "chore: adiciona arquivo provisório".
   - Se achar muito complexo, use apenas o `--amend` no último commit.

3. **Atomicidade na Prática**:
   - Edite 3 arquivos ao mesmo tempo.
   - Use `git add -p` (patch).
   - O Git vai perguntar pedaço por pedaço (hunk) se você quer adicionar.
   - Responda `y` (sim) ou `n` (não) para separar as mudanças em commits diferentes.

## Dica
Commits bem escritos são uma carta de amor para o seu "eu do futuro" (que vai precisar ler isso daqui a 6 meses).
