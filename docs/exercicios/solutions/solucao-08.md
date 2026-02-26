# Solução – Exercícios da Aula 08

Aqui você encontra as respostas sugeridas para os exercícios de Pull Requests da Aula 08.

### 1. Enviando para Revisão
O primeiro passo é clicar no botão **"Create pull request"**. Isso abrirá um formulário onde você deve preencher o título e a descrição das mudanças propostas.

### 2. Identificando Mudanças
Na interface de Diff do GitHub:
- **Vermelho**: Representa linhas removidas ou alteradas.
- **Verde**: Representa linhas adicionadas ou o novo estado da linha alterada.

### 3. A Arte do Review
Para aprovar um PR, deve-se clicar no botão **"Review changes"** (canto superior direito da aba de Diff), selecionar a opção **"Approve"** e enviar o comentário.

### 4. Integração Final
Após o merge, os commits da branch `ajuste-readme` passam a fazer parte do histórico da branch `main`. A branch original no GitHub pode ser deletada com segurança através do botão "Delete branch" que aparece logo após o merge.

### 5. Rejeitando com Elegância
Se você fechar um PR sem o merge, os commits continuam existindo na branch original, mas o código **não** é incorporado à `main`. O PR fica com o status cinza ("Closed") e pode ser reaberto no futuro se necessário.
