# Quiz 07

<script src="../../assets/js/quiz.js" defer></script>

<style>
@import url("../../assets/css/quiz.css");
</style>

<div class="quiz-container">
  <div class="quiz-item" id="q1">
    <div class="quiz-question">1. Qual comando envia os commits do seu computador para o GitHub?</div>
    <div class="quiz-options">
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">A)</span> `git send`
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">B)</span> `git upload`
      </div>
      <div class="quiz-option" data-correct="true" data-feedback="Correto!">
        <span class="option-letter">C)</span> `git push`
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">D)</span> `git commit`
      </div>
    </div>
    <div class="quiz-feedback"></div>
  </div>
  <div class="quiz-item" id="q2">
    <div class="quiz-question">2. O que é "origin" no comando `git remote add origin URL`?</div>
    <div class="quiz-options">
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">A)</span> É um comando do sistema operacional.
      </div>
      <div class="quiz-option" data-correct="true" data-feedback="Correto!">
        <span class="option-letter">B)</span> É um apelido (alias) padrão para o endereço do repositório remoto.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">C)</span> É o nome da branch principal.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">D)</span> É o servidor do Google.
      </div>
    </div>
    <div class="quiz-feedback"></div>
  </div>
  <div class="quiz-item" id="q3">
    <div class="quiz-question">3. Qual comando baixa uma cópia completa de um repositório remoto para sua máquina?</div>
    <div class="quiz-options">
      <div class="quiz-option" data-correct="true" data-feedback="Correto!">
        <span class="option-letter">A)</span> `git clone`
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">B)</span> `git download`
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">C)</span> `git pull`
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">D)</span> `git fork`
      </div>
    </div>
    <div class="quiz-feedback"></div>
  </div>
  <div class="quiz-item" id="q4">
    <div class="quiz-question">4. Para que serve o arquivo `.gitignore`?</div>
    <div class="quiz-options">
      <div class="quiz-option" data-correct="true" data-feedback="Correto!">
        <span class="option-letter">A)</span> Para listar arquivos que o Git deve ignorar e não rastrear.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">B)</span> Para limpar a lixeira do computador.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">C)</span> Para bloquear usuários indesejados.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">D)</span> Para ignorar commits errados.
      </div>
    </div>
    <div class="quiz-feedback"></div>
  </div>
  <div class="quiz-item" id="q5">
    <div class="quiz-question">5. Se eu quiser baixar apenas as atualizações recentes de um repo que já clonei, devo usar `git clone` novamente?</div>
    <div class="quiz-options">
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">A)</span> Sim, sempre.
      </div>
      <div class="quiz-option" data-correct="true" data-feedback="Correto!">
        <span class="option-letter">B)</span> Não, usar `clone` de novo vai criar uma pasta duplicada ou dar erro. (O correto seria `git pull`).
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">C)</span> Sim, mas com a opção `--update`.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">D)</span> Não, devo apagar a pasta e clonar de novo.
      </div>
    </div>
    <div class="quiz-feedback"></div>
  </div>
</div>
