# Solução – Exercícios da Aula 05

Aqui você encontra as respostas sugeridas para os exercícios de Resolução de Conflitos da Aula 05.

### 1. Provocando a Colisão
Confirmação visual. O merge deve falhar com a mensagem: `CONFLICT (content): Merge conflict in compras.txt`.

### 2. Identificando os Sinais
O comando é:
```bash
git status
```
Arquivos com conflito aparecerão como `both modified`.

### 3. Limpando os Marcadores
Após editar o arquivo para conter "Arroz, Feijão, Batata, Macarrão" e remover as linhas com `<<<<`, `====` e `>>>>`, o arquivo deve ser salvo.

### 4. Finalizando o Pacto
Os comandos finais são:
```bash
git add compras.txt
git commit
```
*Observação*: No `git commit`, ele abrirá o editor para confirmar a mensagem de merge. Basta salvar e fechar.

### 5. Abortando a Operação
Para cancelar um merge que deu conflito e voltar ao estado anterior:
```bash
git merge --abort
```
