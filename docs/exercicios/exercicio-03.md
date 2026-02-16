# Exercícios da Aula 03

## 🛠 Exercícios

1. **Prática de Fluxo Básico**:
   - Crie uma pasta nova chamada `exercicio-03`.
   - Inicie o Git nela.
   - Crie 3 arquivos: `a.txt`, `b.txt`, `c.txt`.
   - Adicione APENAS o `a.txt` (`git add a.txt`).
   - Faça um commit (`git commit -m "Adiciona A"`).
   - Veja o status (`git status`). O que aconteceu com b e c?

2. **Entendendo o Staging**:
   - Adicione `b.txt` (`git add b.txt`).
   - Tente fazer `git commit` SEM a opção `-m`. O que acontece? (Dica: ele abre um editor de texto. Se for o Vim e você ficar preso, digite `:q!` e enter para sair, ou tente configurar o VS Code como editor padrão).
   - Se conseguiu sair, faça o commit normalmente com `-m`.

3. **Git Log**:
   - Use `git log` no repositório acima.
   - Tente usar `git log --oneline` para ver uma versão resumida.

## Explicação Extra
- Seus arquivos `b.txt` e `c.txt` continuaram como "Untracked" (não rastreados) no passo 1. Isso mostra que o Git só commita o que você explicitamente adiciona com `git add`.
