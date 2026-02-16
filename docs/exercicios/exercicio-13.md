# Exercícios da Aula 13

## 🛠 Exercícios

1. **GitHub Flow em Equipe**:
   - Se tiver um colega estudando com você:
   - Adicione-o ao repo.
   - Peça para ele criar uma branch, commitar e abrir PR.
   - Você revisa e aprova.
   - Depois inverta os papéis.

2. **Simulando Conflito de Equipe**:
   - Crie um arquivo `agenda.txt` no GitHub com: "Reunião 10h".
   - Localmente, crie `agenda.txt` com: "Reunião 11h".
   - Tente dar `git add`, `commit` e `push`.
   - Veja a mensagem de erro. **Leia a mensagem**, ela te diz exatamente o que fazer (`git pull ...`).
   - Faça o pull, resolva o conflito, e dê o push.

3. **Revisão de Permissões**:
   - Vá nas configurações do repo.
   - Tente achar onde se protege a branch `main` ("Branch protection rules").
   - Isso exige repositório Pro em contas privadas, ou é grátis em repos públicos.
   - Tente criar uma regra que exige "Require a pull request before merging".

## Dica
Em empresas, a branch `main` é SEMPRE bloqueada. Ninguém consegue dar push nela, nem o dono. Só via Pull Request aprovado.
