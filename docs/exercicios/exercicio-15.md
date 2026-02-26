# Exercícios da Aula 15

## 🛠 Troubleshooting: Resolvendo Problemas com Calma

### Nível: Básico

1.  **Recuperação Imediata**:
    - Delete propositalmente o arquivo `index.html` da sua pasta de projeto (deletar fisicamente, não via `git rm`).
    - Use o comando `git status` para confirmar que o Git percebeu a ausência.
    - Qual comando você deve usar para restaurar o arquivo exatamente como ele estava no último commit?

2.  **Corrigindo a Mensagem**:
    - Realize um commit com a mensagem "errado". 
    - Utilize o comando de emenda (`amend`) para trocar a mensagem para "feat: adiciona estrutura inicial".

### Nível: Intermediário

3.  **O Poder do Reset Suave**:
    - Realize um commit qualquer.
    - Utilize o comando `git reset --soft HEAD~1`. 
    - Após o comando, o que aconteceu com as suas alterações? Elas foram apagadas ou continuam na Staging Area (verde)?

4.  **Saindo do Limbo (Detached HEAD)**:
    - Utilize o `git log --oneline` e copie o hash de um commit anterior.
    - Faça um `checkout` para esse hash. O Git avisará que você está em "detached HEAD".
    - Qual o comando mais simples para sair desse estado e voltar para a sua branch principal (`main`)?

### Nível: Desafio

5.  **A Gaveta de Emergência (Stash)**:
    - Imagine que você está no meio de uma alteração complexa, mas precisa mudar de branch para corrigir um bug urgente e não quer commitar o código incompleto.
    - Pesquise e utilize o comando `git stash` para "guardar" suas mudanças temporariamente. Como você faz para "recuperar" essas mudanças depois de voltar para a branch original?

---

[:octicons-arrow-right-24: Ver Solução](solutions/solucao-15.md)
