# Solução – Exercícios da Aula 13

Aqui você encontra as respostas sugeridas para os exercícios de Trabalho em Equipe da Aula 13.

### 1. Convidando o Time
Resposta prática. O colaborador convidado deve aceitar o convite (via e-mail ou notificação no GitHub) para ter acesso de escrita ao projeto.

### 2. Verificando Permissões
Um colaborador com acesso **Read** consegue ver o código, baixar o repositório e abrir issues, mas **não consegue dar push** diretamente para nenhuma branch. Ele precisaria fazer um Fork para contribuir.

### 3. Sincronização Forçada (Pull)
O Git rejeita o envio porque o histórico local e remoto divergem (o remoto tem commits que o local não tem). É o erro de **non-fast-forward**.
**Solução**:
```bash
git pull origin main
```
Após baixar as mudanças e resolver possíveis conflitos, o `push` será aceito.

### 4. Colaborador vs Contribuidor
Não, você não conseguirá dar `push` direto porque não é um **Colaborador** oficial (não tem permissão de escrita). Para contribuir, você deve agir como **Contribuidor**: fazer um Fork, alterar no seu repositório e enviar um Pull Request.

### 5. Simulando o Fluxo de Time
Resposta reflexiva. A experiência de Pull Request e Merge é a base de como times de engenharia de software operam no mundo real, garantindo qualidade através do Code Review.
