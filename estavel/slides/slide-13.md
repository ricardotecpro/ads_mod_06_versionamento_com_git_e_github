# Aula 13 – Trabalho em Equipe

---

## Níveis de Permissão

- **Read**: Apenas leitura e Issues.
- **Write**: Pode dar `push` direto (Colaborador).
- **Admin**: Gerencia tudo (Membros, Configurações).
- **Owner**: Dono supremo do projeto.

---

## Colaborador vs. Contribuidor

- **Colaborador (Interno)**:
  - Tem permissão de escrita.
  - Dá `push` direto na branch do projeto.
- **Contribuidor (Externo)**:
  - Não tem permissão direta.
  - Precisa fazer **Fork** e enviar um **Pull Request**.

---

## A Regra: Pull antes do Push

- Se o servidor tem novidades, seu `push` será rejeitado.
- O Git faz isso para você não apagar o histórico alheio.
- **Solução**: `git pull origin main` -> Resolva conflitos -> `git push`.

---

## Gestão de Membros

- Vá em `Settings > Collaborators`.
- Convide pelo usuário ou e-mail.
- **Dica**: Escolha sempre o nível mínimo de acesso necessário por segurança.

---

## Branch Protection

- Em empresas, ninguém dá `push` na `main`.
- A branch é protegida e exige:
  - Pull Request.
  - Aprovação de revisores.
  - Testes passando.
