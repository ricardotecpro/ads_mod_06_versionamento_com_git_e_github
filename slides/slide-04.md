# Aula 04 – Branches e Merges

---

## O "Multiverso" do Código

- **Branch**: Uma linha do tempo paralela.
- Permite fazer experimentos sem quebrar a versão principal.
- Branch padrão: `main`.

---

## Por que ramificar?

- Novas funcionalidades (features).
- Correção de bugs.
- Testes arriscados.

---

## Comandos de Navegação

- `git branch`: Lista as ramificações.
- `git branch [nome]`: Cria uma nova.
- `git switch [nome]`: Muda de linha do tempo.

---

## Unindo Mundos: Merge

- Traz as mudanças da branch de teste para a `main`.
- **Passos**:
  1. `git switch main`
  2. `git merge feature-contato`

---

## Regra de Ouro

- **Mantenha a `main` sagrada.**
- Sempre trabalhe em branches auxiliares.
- Faça o merge apenas quando o código estiver estável.
