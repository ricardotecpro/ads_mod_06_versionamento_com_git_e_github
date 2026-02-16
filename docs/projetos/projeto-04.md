# Projeto da Aula 04

## 🚀 Projeto da Aula: Trabalhando com Branches

Vamos simular um fluxo real de trabalho no nosso portfólio.

### Passo 1: Nova Funcionalidade
Você quer adicionar seu email, mas não tem certeza se vai ficar bom. Vamos fazer em uma branch segura.
1. No terminal do `meu-portfolio-git`:
   ```bash
   git branch contato
   git switch contato
   ```
   (Ou use apenas `git switch -c contato`).

### Passo 2: A Alteração
1. Crie um novo arquivo chamado `contato.txt`.
2. Escreva seu email dentro dele.
3. Salve.
4. Adicione e commite:
   ```bash
   git add contato.txt
   git commit -m "Adiciona email de contato"
   ```

### Passo 3: A Validação
1. Troque de volta para a branch principal (pode se chamar `master` ou `main`, verifique com `git branch` para saber qual é a correta):
   ```bash
   git switch master
   ```
   (Use `main` se for o caso).
2. Olhe a pasta. O arquivo `contato.txt` **sumiu**. Isso prova que o trabalho estava isolado.

### Passo 4: O Merge
Você decidiu que a funcionalidade está boa e quer incorporá-la.
1. Estando na branch principal, digite:
   ```bash
   git merge contato
   ```
2. O arquivo `contato.txt` reaparece magicamente. Agora ele faz parte da versão oficial do seu projeto!
