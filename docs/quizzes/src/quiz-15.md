# Quiz 15

1. O que significa estar no estado "Detached HEAD"?

    - [ ] Que você perdeu sua conta do GitHub
    - [ ] Que o servidor caiu
    - [x] Que você não está em nenhuma branch, mas visitando um commit específico no histórico
    - [ ] Que o Git foi desinstalado

2. Qual comando desfaz o último commit, mas mantém seus arquivos modificados prontos para commitar de novo?

    - [x] git reset --soft HEAD~1
    - [ ] git reset --hard HEAD~1
    - [ ] git delete commit
    - [ ] git undo

3. Se o `git push` for rejeitado por erro "non-fast-forward", qual a primeira coisa a fazer?

    - [ ] Deltar a pasta .git
    - [x] Executar um `git pull` para sincronizar as mudanças remotas
    - [ ] Reiniciar o computador
    - [ ] Criar um novo repositório

4. O comando `git reset --hard` é seguro para usar a qualquer momento?

    - [ ] Sim, ele é muito útil
    - [ ] Não, ele apaga apenas o README
    - [ ] Sim, ele limpa o cache da internet
    - [x] NÃO! Ele apaga permanentemente mudanças que não foram commitadas. Use com cautela!

5. Qual comando mostra um histórico completo de TUDO o que você fez (resets, switches, commits)?

    - [ ] git log --all
    - [ ] git history --full
    - [x] git reflog
    - [ ] git status --verbose
