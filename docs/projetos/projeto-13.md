# Projeto 13 - Blindando o Repositório

---

## 🚀 Objetivo
Simular um ambiente corporativo de alta segurança, proibindo alterações diretas na versão de produção.

### 📋 Passo a Passo

#### 1. Configuração de Bloqueio (Branch Protection)
No GitHub:
1. Vá em **Settings > Branches**.
2. Clique em **Add branch protection rule**.
3. Em "Branch name pattern", digite `main`.
4. Ative as opções:
   - `Require a pull request before merging`.
   - `Require approvals` (se possível).
   - `Do not allow bypassing` (aplica a regra até para você, o dono).

#### 2. O Teste de Intrusão
1. No seu computador, tente fazer uma alteração no README direto na main.
2. Tente dar `git push origin main`.
3. **Resultado Esperado**: O Git deve rejeitar seu push com uma mensagem de erro ("protected branch").

#### 3. O Caminho Correto
1. Crie uma branch: `git switch -c fix-protecao`.
2. Realize a alteração, envie para o servidor e abra um **Pull Request**.

### 🏆 Conquista
Você acaba de implementar o padrão de segurança das Big Techs. Agora, nenhum código entra na `main` sem passar por uma revisão oficial.
