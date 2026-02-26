# Quiz 03 - Repositórios, Commits e Histórico

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Qual comando transforma uma pasta comum em um repositório Git?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'new' não é um comando do Git para essa função.">git new</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! git init cria a pasta oculta .git e inicia o rastreamento.">git init</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'start' não inicia o repositório.">git start</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'create' não é o comando de inicialização.">git create</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Para onde o comando `git add` envia os arquivos antes de serem salvos permanentemente?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O GitHub é o destino remoto, não o local do próximo passo.">Para o GitHub</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Repositório Local (.git) é o destino do comando 'commit'.">Para o Repositório Local (.git)</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! A Staging Area é a área de preparação/palco.">Para a Staging Area (Área de Preparação)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Git add não deleta arquivos.">Para a Lixeira</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual a principal função do comando `git commit`?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O commit tira o 'snapshot' da Staging Area e salva no banco de dados local.">Salvar definitivamente as alterações da Staging Area no Repositório Local</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O envio para a nuvem é feito pelo comando 'push'.">Enviar os arquivos para a nuvem</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Git não deleta arquivos durante o commit.">Deletar arquivos temporários</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O projeto já deve ter um nome; o commit salva versões.">Renomear o projeto</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. O que o comando `git status` informa ao desenvolvedor?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Git não monitora largura de banda da internet.">A velocidade de download do repositório</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O histórico é visto com o comando 'log'.">O histórico detalhado de todas as versões anteriores</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Git local não abre o navegador automaticamente.">Abre o site do GitHub no navegador</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Ele mostra arquivos rastreados, não rastreados e modificados.">O estado atual dos arquivos (preparados, não preparados, modificados)</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Qual comando é utilizado para visualizar a lista cronológica de commits?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Esse comando não existe nativamente no Git.">git history</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! git log mostra o autor, data, hash e mensagem do commit.">git log</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Comando inválido.">git show history</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A flag --log não existe para o comando status.">git status --log</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Qual o objetivo da mensagem de commit (-m)?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Uma mensagem clara ajuda a entender por que a mudança foi feita meses depois.">Explicar brevemente o que foi alterado naquele commit</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A mensagem é um requisito técnico para organização.">Cumprir uma exigência estética do terminal</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O commit salva o conteúdo, não o hardware.">Aumentar a segurança contra falhas no disco rígido</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A mensagem não substitui o código funcional.">Substituir a necessidade de escrever código real</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. O que acontece se você rodar `git commit` sem a flag `-m`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O commit ainda pode ser realizado.">O commit é cancelado automaticamente</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Git abre o editor padrão (geralmente o Vim) para você escrever a mensagem.">O Git abre o editor de texto padrão para você digitar a mensagem</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Git exige uma mensagem válida.">O commit recebe uma mensagem aleatória do sistema</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O computador continuará funcionando normalmente.">O computador trava e precisa ser reiniciado</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Qual a função da pasta oculta `.git`?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Ela é o 'cérebro' do projeto, guardando todo o banco de dados do versionamento.">Armazenar todo o histórico de versões e metadados do repositório</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O .git guarda versões passadas, não backups remotos de hardware.">Servir como backup na nuvem para os seus documentos pessoais</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Ela deve ser mantida para o versionamento funcionar.">Guardar arquivos temporários que devem ser deletados semanalmente</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Git gerencia o histórico de arquivos fornecidos.">Instalar extensões automaticamente no Visual Studio Code</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Qual comando resumido mostra o histórico em uma única linha por commit?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! git log --oneline é ideal para visões gerais rápidas.">git log --oneline</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O comando correto usa '--' para flags.">git log short</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Flag inexistente para log.">git log --summary</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Compact não é uma flag padrão do git log.">git log -compact</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. O que é um 'Untracked File' (Arquivo não rastreado)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O arquivo está físicamente lá, mas o Git o 'ignora' por enquanto.">Um arquivo que foi deletado do computador</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O arquivo existe na pasta, mas ainda não foi adicionado ao Git ('git add').">Um arquivo novo que o Git ainda não começou a monitorar</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Todo arquivo monitorado tem sua versão no .git.">Um arquivo que está corrompido e não pode ser aberto</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Isso seria um arquivo no Staging Area.">Um arquivo que já foi salvo em um commit anterior</div>
  <div class="quiz-feedback"></div>
</div>
