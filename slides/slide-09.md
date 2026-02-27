# Aula 09 – Fluxo de Trabalho: GitHub Flow

---

## O Acordo de Cavalheiros

- Um **Workflow** (fluxo) é o conjunto de regras do time.
- Sem regras, o repositório vira um caos de códigos quebrados.
- **Regra de Ouro**: A branch `main` deve estar sempre estável.

---

## Os 6 Passos do GitHub Flow

1. **Branch**: Crie a partir da `main`.
2. **Commit**: Trabalhe e salve localmente.
3. **Pull Request**: Abra para revisão.
4. **Discussão**: Melhore o código com feedback.
5. **Deploy**: Teste em ambiente temporário.
6. **Merge**: Envie o código final para a `main`.

---

## GitHub Flow vs. Git Flow

| GitHub Flow | Git Flow |
| :--- | :--- |
| **Simples** e ágil. | **Complexo** e burocrático. |
| Entrega contínua (Web). | Lançamentos agendados. |
| Poucas branches. | Muitas branches paralelas. |

---

## Vantagens da Rapidez

- Menor tempo para o código ir ao ar.
- Feedback rápido dos usuários.
- Facilidade em ensinar novos membros do time.

---

## Executando o Fluxo

```bash
# Sincronize antes de começar
git switch main
git pull

# Crie sua "bolha" de trabalho
git switch -c feature-nova-funcao
```
