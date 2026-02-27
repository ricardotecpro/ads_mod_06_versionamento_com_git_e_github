# Aula 07 – Repositórios Remotos

---

## Codar Local, Compartilhar Global

- Até agora, o código vivia apenas no seu HD.
- O **Remote** permite:
  - Backup seguro na nuvem.
  - Colaboração com outros devs.
  - Portfólio público acessível.

---

## Conectando os Pontos

- **git remote add origin [URL]**: Cria a ponte entre o seu PC e o GitHub.
- `origin` é o apelido padrão para o servidor remoto.

---

## Empurrando código: git push

- `git push -u origin main`
- Envia seus commits para a nuvem.
- O `-u` vincula as branches para o futuro.

---

## Baixando código: git clone

- `git clone [URL]`
- Cria uma cópia local completa de um projeto existente.
- Útil para começar a trabalhar em um projeto já iniciado.

---

## O arquivo .gitignore

- **Regra de Ouro**: Nem tudo vai para o Git!
- O que ignorar?
  - Senhas/Tokens (`.env`).
  - Pastas gigantes (`node_modules`).
  - Arquivos de sistema (`.DS_Store`).
  - Compilados (`.exe`, `.pyc`).
