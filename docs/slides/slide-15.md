# Aula 15 – Troubleshooting: Erros Comuns

---

## Não Entre em Pânico!

- Errar no Git é normal.
- Quase tudo é reversível, desde que esteja no `.git`.
- O Git tem uma "memória de elefante".

---

## O Poder do Reset

- **`--soft`**: Rebobina o commit, mas mantém os arquivos prontos no Stage.
- **`--hard`**: **Cuidado!** Apaga tudo e volta ao estado anterior limpo.
- Use para consertar commits feitos na branch errada.

---

## Detached HEAD (Cabeça Desprendida)

- Acontece quando você viaja para um commit específico (hash).
- Você está no passado, mas sem trilhas (branches).
- **Como sair?**
  - Voltar ao presente: `git switch main`.
  - Criar branch nova: `git switch -c nova-branch`.

---

## Recuperei! (git restore)

- Deletou um arquivo sem querer?
- Se ele estava no último commit:
  ```bash
  git restore arquivo.txt
  ```
- O Git traz ele de volta instantaneamente.

---

## reflog: O Plano de Emergência

- `git reflog`
- Mostra o diário secreto de todos os seus movimentos.
- Se você "deletou" um commit com reset hard, o hash dele ainda estará aqui por algum tempo.
