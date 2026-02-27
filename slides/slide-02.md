# Aula 02 – Instalando e Configurando o Git

---

## Onde baixar?

- **[git-scm.com](https://git-scm.com)**
- Versões para:
  - Windows (Git Bash incluído)
  - macOS (brew install git)
  - Linux (apt-get install git)

---

## Configuração Obrigatória

- O Git precisa de uma **Identidade**.
- Sem ela, os commits são bloqueados.
- Comandos:
  ```bash
  # Nome Profissional
  git config --global user.name "Seu Nome"

  # Email (mesmo do GitHub)
  git config --global user.email "seu@email.com"
  ```

---

## Onde fica salvo?

- No arquivo `.gitconfig` (pasta HOME).
- Você pode ver as configurações com:
  ```bash
  git config --list
  ```

---

## Dica: Editor Padrão

- O Git usa o **Vim** por padrão (difícil para iniciantes).
- Se preferir o VS Code:
  ```bash
  git config --global core.editor "code --wait"
  ```

---

## Validando!

Se `git config user.name` retornar seu nome, você está oficialmente pronto para versionar!
