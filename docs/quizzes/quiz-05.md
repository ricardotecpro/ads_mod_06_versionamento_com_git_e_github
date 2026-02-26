# Quiz 05 - Resolução de Conflitos

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Em qual situação o Git gera um conflito de merge automaticamente?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Git lida com a falta de internet através da natureza distribuída, não gerando conflitos.">Quando o Git não tem conexão estável com o servidor</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O conflito ocorre quando a mesma linha foi alterada de formas diferentes em ramificações distintas.">Quando a mesma linha de um arquivo foi alterada de formas diferentes em dois locais</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Esquecer do 'git add' impede o commit, mas não gera conflito de merge.">Quando você esquece de usar o git add antes do commit</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Merges costumam ser automáticos (fast-forward) se as alterações não colidirem.">Sempre que você tenta unir duas branches diferentes</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Como o Git resolve conflitos de conteúdo na mesma linha?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Git não possui inteligência artificial para escolher o código 'melhor'.">Ele escolhe a versão que parece estar mais correta tecnicamente</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Priorizar o mais antigo poderia apagar correções importantes.">Ele sempre escolhe o commit que foi realizado primeiro</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Priorizar o mais novo poderia causar regressões.">Ele sempre escolhe o commit que foi realizado por último</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Git pausa o processo e marca os arquivos para que o humano decida.">Ele não resolve; ele pausa o merge e pede intervenção humana</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Dentro de um arquivo com conflito, o que significam as linhas entre `<<<<<<<` e `=======`?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Representa o conteúdo da branch onde você está posicionado (HEAD).">As alterações que existem na sua branch atual (local)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Essa parte fica entre '====' e '>>>>'.">As alterações que estão vindo da branch que você quer incorporar</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Estes marcadores não indicam comentários do sistema.">Sugestões de comentários geradas automaticamente pelo Git</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. São ferramentas de versionamento, não bugs do Windows.">Erros de registro de memória do sistema operacional</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Qual comando o desenvolvedor deve usar após resolver o conflito no arquivo para marcá-lo como "pronto"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Este comando não existe no Git.">git resolved</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Não é um comando padrão do Git cli.">git fix</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O git add move o arquivo resolvido para a Staging Area, confirmando a resolução.">git add [nome-do-arquivo]</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O commit deve vir após o add.">git commit --fixed</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. O que deve ser feito com os marcadores `<<<<`, `====` e `>>>>` no código final?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Eles devem ser removidos, caso contrário, causarão erros de sintaxe no código.">Devem ser removidos manualmente após a decisão do código final</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Manter os marcadores impede a execução correta da maioria dos programas.">Devem ser mantidos como documentação de que houve conflito</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A cor não altera a natureza do marcador.">Devem ser transformados em blocos de comentários cinzas</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Git remove os marcadores apenas se você usar ferramentas visuais automáticas.">Eles desaparecem sozinhos quando você dá o git commit</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Qual o comando para CANCELAR um merge que deu muito conflito e voltar ao estado original?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Stop não é um subcomando de merge.">git merge --stop</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! git merge --abort limpa o estado de conflito e restaura o repositório.">git merge --abort</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Undo não é um comando Git.">git merge --undo</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Reset volta o histórico, mas --abort é específico para merges em conflito.">git reset --hard</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Ferramentas visuais (como o VS Code) podem ajudar na resolução de conflitos?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Editores modernos possuem interfaces amigáveis para escolher entre 'Accept Current' ou 'Accept Incoming'.">Sim, facilitando a escolha entre as versões com botões clicáveis</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Elas são amplamente utilizadas por profissionais.">Não, a resolução deve ser feita obrigatoriamente via terminal puro</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. As ferramentas apenas auxiliam o desenvolvedor.">Sim, mas elas costumam deletar o histórico de commits.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O VS Code é um editor, não um Sistema de Controle de Versão Centralizado.">Não, o VS Code só funciona com SVN, não com Git.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Em qual seção do `git status` aparecem os arquivos em conflito?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Eles já estão sob rastreio, mas em um estado problemático.">Untracked files</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Eles precisam de intervenção antes de voltarem para o stage.">Changes to be committed</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Aparecem sob o cabeçalho 'Unmerged paths'.">Unmerged paths</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Essa seção não existe no Git.">Clean files</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Qual o risco de realizar um `git add .` (ponto) durante uma resolução de conflito?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Você pode acidentalmente marcar um arquivo como 'resolvido' sem ter removido os marcadores de erro dele.">Marcar um arquivo como resolvido sem ter deletado os marcadores de conflito</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O add apenas prepara o commit.">Deletar permanentemente o servidor remoto</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O add não afeta o histórico de branches.">Trocar automaticamente a branch principal de lugar</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Git add não tem relação com privilégios de administrador.">Perder os direitos de administrador no repositório</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. O que significa 'Accept Both Changes' em um editor de conflito?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Ele mantém o código, não deleta.">Deletar o arquivo do projeto</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Ele aceita as duas, não escolhe uma.">Escolher apenas a versão que está vindo do servidor</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Ele combina o código das duas ramificações no arquivo final.">Keep (manter) o código das duas branches, uma abaixo da outra</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Não causa reinicialização.">Reiniciar o Git do zero</div>
  <div class="quiz-feedback"></div>
</div>
