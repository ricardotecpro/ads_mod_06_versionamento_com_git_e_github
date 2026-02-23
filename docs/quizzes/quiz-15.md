# Quiz 15 - Introdução

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. O que significa estar no estado "Detached HEAD"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Que você perdeu sua conta do GitHub</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Que o servidor caiu</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Que você não está em nenhuma branch, mas visitando um commit específico no histórico">Que você não está em nenhuma branch, mas visitando um commit específico no histórico</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Que o Git foi desinstalado</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Qual comando desfaz o último commit, mas mantém seus arquivos modificados prontos para commitar de novo?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! git reset --soft HEAD~1">git reset --soft HEAD~1</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">git reset --hard HEAD~1</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">git delete commit</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">git undo</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Se o `git push` for rejeitado por erro "non-fast-forward", qual a primeira coisa a fazer?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Deltar a pasta .git</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Executar um `git pull` para sincronizar as mudanças remotas">Executar um `git pull` para sincronizar as mudanças remotas</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Reiniciar o computador</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Criar um novo repositório</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. O comando `git reset --hard` é seguro para usar a qualquer momento?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Sim, ele é muito útil</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Não, ele apaga apenas o README</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Sim, ele limpa o cache da internet</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! NÃO! Ele apaga permanentemente mudanças que não foram commitadas. Use com cautela!">NÃO! Ele apaga permanentemente mudanças que não foram commitadas. Use com cautela!</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Qual comando mostra um histórico completo de TUDO o que você fez (resets, switches, commits)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">git log --all</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">git history --full</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! git reflog">git reflog</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">git status --verbose</div>
  <div class="quiz-feedback"></div>
</div>

