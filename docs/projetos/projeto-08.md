# Projeto 08 - O Fluxo Profissional (PR)

---

## 🚀 Objetivo
Praticar o ciclo completo de colaboração: Branch, Push, Pull Request e Merge no servidor.

### 📋 Passo a Passo

#### 1. O Desenvolvedor em Ação
1. Crie a branch: `git switch -c feat-planos-futuros`.
2. Crie um arquivo `planos.txt` com uma lista de tecnologias que deseja aprender.
3. Commite: `git commit -am "feat: adiciona plano de estudos"`.
4. Envie para o GitHub: `git push -u origin feat-planos-futuros`.

#### 2. O Pedido de Inclusão
1. No Site do GitHub, aparecerá um aviso amarelo: "Compare & pull request". Clique nele.
2. Escreva uma descrição curta do que você está adicionando.
3. Clique em **Create pull request**.

#### 3. O Merge (Fusão)
1. Finja que você revisou o próprio código (em empresas, um colega faria isso).
2. Clique no botão verde **Merge pull request**.
3. Confirme o Merge.

#### 4. Sincronia Final
No seu terminal:
1. Volte para a main: `git switch main`.
2. Observe que o arquivo `planos.txt` não está lá! Baixe a atualização que você fez no site:
   ```bash
   git pull origin main
   ```

### 🏆 Conquista
Você acaba de completar o ciclo de vida de um software profissional. É exatamente assim que grandes empresas como Google e Microsoft trabalham.
