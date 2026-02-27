# Aula 11 – A Arte do Commit

---

## Histórico para Humanos

- O Git não liga para a mensagem que você escreve.
- Mas seus colegas (e seu "eu do futuro") ligam muito!
- Evite: `ajuste`, `teste`, `arrumando`.

---

## Commits Atômicos

- **1 Commit = 1 Única Ação.**
- Facilita o Code Review.
- Torna a reversão de erros cirúrgica.
- Se você fez 10 coisas, faça 10 commits.

---

## Conventional Commits

Padrão de mercado para mensagens profissionais:
- **`feat:`**: Nova funcionalidade.
- **`fix:`**: Correção de bug.
- **`docs:`**: Documentação.
- **`style:`**: Formatação de código.
- **`refactor:`**: Melhoria técnica sem mudar o resultado.

---

## A Regra do Imperativo

- Escreva como se estivesse dando uma ordem ao código:
  - `Adiciona botão de busca` ✅
  - `Adicionado botão de busca` ❌ (Passado)

---

## Errei a mensagem! E agora?

- Se você **ainda não deu push**:
  ```bash
  git commit --amend -m "Nova mensagem correta"
  ```
- **Aviso**: Nunca use `--amend` em commits que já estão no GitHub.
