# Quiz 11 - Boas Práticas: A Arte do Commit

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Qual é a convenção gramatical recomendada para o título das mensagens de commit?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O tempo passado ('Adicionei') é comum, mas não é a melhor prática recomendada globalmente.">Usar o tempo passado (ex: 'Adicionei função de busca')</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Modo Imperativo ('Adiciona') deve ser lido como se estivesse completando a frase: 'Se aplicado, este commit irá...'.">Usar o modo imperativo (ex: 'Adiciona função de busca')</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O gerúndio ('Adicionando') torna o histórico passivo e menos direto.">Usar o gerúndio (ex: 'Adicionando função de busca')</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O futuro indica algo que ainda vai acontecer, e o commit é o registro do que foi feito.">Usar o tempo futuro (ex: 'Irei adicionar função de busca')</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. O que se entende por um "Commit Atômico"?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Commits atômicos facilitam a reversão de erros e tornam o Code Review muito mais simples.">Um commit que resolve apenas uma única tarefa pequena e específica</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Agrupar muitas mudanças dificulta o entendimento do que foi feito.">Um commit gigante que contém todas as mudanças realizadas no dia</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A intenção deve ser sempre positiva e construtiva.">Um commit que deleta partes do código sem avisar o time</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Refere-se à organização das mudanças, não à ferramenta de escrita.">Um commit escrito obrigatoriamente por uma inteligência artificial</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual destes prefixos é utilizado para indicar uma NOVA funcionalidade no padrão 'Conventional Commits'?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'fix:' é usado para correções de bugs.">fix:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'docs:' é para documentação (README, etc).">docs:</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! 'feat:' vem de 'feature' (funcionalidade).">feat:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'refactor:' é para melhorias de código sem mudar o comportamento.">refactor:</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Por que é considerado uma 'má prática' misturar correções de lógica e alterações de estilo (cores/espaços) no mesmo commit?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Git lida bem com arquivos pesados.">Porque o arquivo final do Git ficaria muito pesado e lento</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O GitHub aceita qualquer commit válido tecnicamente.">Porque o GitHub bloqueia commits que mexem em muitos arquivos ao mesmo tempo</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Se você precisar reverter a cor, acabará revertendo a correção do bug por acidente.">Dificulta a revisão e a possibilidade de reverter apenas uma das mudanças</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. É uma questão de fluxo de trabalho humano, não de limite do terminal.">Porque o terminal do Git não suporta mais de duas alterações simultâneas</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Considerando as boas práticas, qual destas mensagens de commit é a MAIS PROFISSIONAL?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Mensagens genéricas são inúteis para o histórico futuro.">"vários ajustes e correções"</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Falta o prefixo e o uso do imperativo.">"consertando o problema do botão que não clicava"</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Curta, prefixada e no imperativo.">"fix: corrige o posicionamento do botão de login"</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Expressar frustração no histórico de código não é profissional.">"ESTAVA TUDO QUEBRADO MAS CONSEGUI ARRUMAR AGORA"</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. O que o prefixo `chore:` indica no padrão Conventional Commits?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! 'chore' refere-se a tarefas rotineiras que não mudam o código ou a documentação.">Tarefas de manutenção, como atualizar dependências ou build</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Isso seria 'refactor:'.">Uma melhoria drástica na performance do banco de dados</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Isso seria 'fix:'.">A descoberta de um bug crítico que foi resolvido</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'chore' não é para novos recursos.">O lançamento oficial da versão 1.0 do produto</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Qual a utilidade da "descrição extendida" (o corpo da mensagem) de um commit?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O histórico deve ser apenas técnico.">Para contar detalhes da vida pessoal do desenvolvedor</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O corpo da mensagem explica o 'PORQUÊ' da mudança quando o 'O QUE' não é suficiente.">Fornecer contexto e explicar a motivação técnica por trás da mudança</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Commits não devem armazenar chaves de acesso.">Para salvar as senhas de banco de dados de forma segura</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Git não é uma ferramenta de log de horas trabalhadas.">Para listar as horas exatas que o desenvolvedor levou na tarefa</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. No terminal, qual comando permite emendar (corrigir) a mensagem do ÚLTIMO commit realizado?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'fix' não é um comando para histórico.">git fix last message</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'change' não é comando Git cli.">git commit --change</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O '--amend' serve para 'remendar' o último commit, seja no texto ou nos arquivos.">git commit --amend</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Reset altera o ponteiro, mas 'amend' é mais direto para correções de mensagem.">git reset --hard</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Qual o limite de caracteres recomendado pela comunidade para o TÍTULO (primeira linha) de um commit?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Muito curto para ser descritivo.">Até 10 caracteres</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Títulos de 50 a 72 caracteres garantem legibilidade em qualquer interface (como celular ou terminal).">Entre 50 e 72 caracteres</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Títulos muito longos ficam truncados (...) em muitas interfaces.">Até 500 caracteres, para não faltar informação</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Git não impõe limite técnico, mas a boa prática sim.">Não existe limite; pode-se escrever um parágrafo inteiro no título</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. O que significa realizar o 'Squash' (Esmagar) de commits antes de um merge?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Transformar 10 commits de 'ajuste' em 1 único commit limpo chamado 'feat: finaliza busca'.">Combinar vários commits pequenos em um único commit consolidado</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Squash foca em organização, não em espaço.">Apagar o histórico para economizar memória no servidor</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. É um termo universal do Git.">Uma gíria usada apenas em projetos de São Paulo</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Ele agrupa, não divide.">Dividir um commit em vários commits menores automaticamente</div>
  <div class="quiz-feedback"></div>
</div>
