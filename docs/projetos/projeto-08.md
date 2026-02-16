# Projeto da Aula 08

## 🚀 Projeto da Aula: O Ciclo Completo

Hoje você vai agir como Gerente e Desenvolvedor ao mesmo tempo.

### Passo 1: O Desenvolvedor
1. No terminal: `git switch -c funcionalidade-nova`.
2. Crie um arquivo `futuro.txt` com suas metas para o ano que vem.
3. `git add .` e `git commit -m "Minhas metas"`.
4. `git push -u origin funcionalidade-nova`.

### Passo 2: O Gerente (GitHub)
1. Vá ao GitHub. Abra o PR.
2. Na descrição, escreva: "Adiciona metas ambiciosas para 2026".
3. Crie o PR.
4. Finja ser um colega chato: Vá em "Files changed" e comente na linha 1: "Tem certeza dessa meta?".
5. Volte para "Conversation" e aprove o PR (se o GitHub deixar aprovar o próprio PR, senão apenas faça o Merge).
6. Clique em **Merge pull request**.
7. Clique em **Delete branch** (limpeza é bom).

### Passo 3: Sincronia
1. Volte ao terminal.
2. Mude para a main: `git switch main`.
3. Tente ver o arquivo: `cat futuro.txt` (ou dir no windows). Ele não deve existir ainda!
4. Baixe a atualização:
   ```bash
   git pull
   ```
5. Agora sim, o arquivo apareceu.

**Conceito chave**: O GitHub virou a "Verdade Absoluta" do projeto. Seu computador apenas envia e recebe atualizações dele.
