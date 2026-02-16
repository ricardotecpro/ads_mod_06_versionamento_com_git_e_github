# Projeto da Aula 13

## 🚀 Projeto da Aula: Protegendo o Forte

Já que estamos simulando um ambiente profissional, vamos blindar nosso projeto.

### Passo 1: Regras de Branch (Projetos Públicos)
Se seu repositório `portfolio-dev` for público (gratuito), você pode criar regras de proteção.
1. Vá em **Settings > Branches**.
2. Clique em **Add branch protection rule**.
3. Em "Branch name pattern", digite `main`.
4. Marque **"Require a pull request before merging"**.
5. Marque **"Do not allow bypassing the above settings"**.
6. Clique em **Create**.

### Passo 2: O Teste
1. Tente alterar algo no seu README localmente.
2. Tente dar `git push origin main`.
3. Se funcionou, você verá um erro dizendo que é proibido dar push na branch protegida!
4. **Vitória!** Agora você é obrigado a criar uma branch e abrir um PR, como num time de elite.

(Nota: Se seu repo for privado e conta free, o GitHub pode bloquear essa feature. Nesse caso, apenas entenda o conceito).
