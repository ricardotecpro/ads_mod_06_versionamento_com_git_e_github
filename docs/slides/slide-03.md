# Aula 03 – Repositórios, Commits e Histórico

---

## git init

- Transforma uma pasta comum em um **Repositório Git**.
- Cria a pasta oculta `.git`.
- **Aviso**: Nunca delete a pasta `.git` manualmente!

---

## As 3 Áreas Fundamentais

1. **Working Directory**: Seus arquivos (onde você edita).
2. **Staging Area**: O "palco" (onde você prepara).
3. **Repository**: O banco de dados (onde você grava).

---

## O Ciclo da Versão

- **git status**: Diagnóstico constante.
- **git add**: "Põe no palco" (prepara).
- **git commit**: "Tira a foto" (grava).

---

## O Commit

- Uma **foto (snapshot)** do projeto.
- Possui um **ID (Hash)** único.
- Exige uma mensagem explicativa.
  - *Dica*: `git commit -m "Explicação"`

---

## Consultando o Passado

- **git log**: Mostra a lista cronológica.
- **Quem** fez? **Quando**? **O que** foi dito?

---

## Resumo Visual

`Arquivo` -> `git add` -> `Staging` -> `git commit` -> `Histórico`
