# Exercícios da Aula 05

## 🛠 Resolução de Conflitos: O Poder da Escolha

### Nível: Básico

1.  **Provocando a Colisão**:
    - Crie uma pasta `treino-conflito` e inicie o Git.
    - Crie um arquivo `compras.txt` com o texto: "Arroz, Feijão". Realize o commit inicial na `main`.
    - Crie uma branch `extra` e mude para ela. Altere o texto para: "Arroz, Feijão, Batata". Commite.
    - Volte para a `main` e altere o mesmo arquivo para: "Arroz, Feijão, Macarrão". Commite.
    - Tente fazer o merge da branch `extra` na `main`.

2.  **Identificando os Sinais**:
    - Após o comando de merge, o Git avisará sobre um conflito. Qual o comando você deve usar para ver quais arquivos estão com o estado de "both modified"?

### Nível: Intermediário

3.  **Limpando os Marcadores**:
    - Abra o arquivo `compras.txt`. Localize os símbolos `<<<<<<<`, `=======` e `>>>>>>>`. 
    - Edite o arquivo para que ele contenha os três itens: "Arroz, Feijão, Batata, Macarrão".
    - **Importante**: Remova todos os marcadores de conflito do arquivo.

4.  **Finalizando o Pacto**:
    - Após salvar o arquivo resolvido, quais são os dois passos (comandos) finais para concluir o merge e registrar a solução no histórico?

### Nível: Desafio

5.  **Abortando a Operação**:
    - Suponha que você começou um merge, deu conflito, e você percebeu que não era a hora certa de fazer isso. Descubra qual comando permite "cancelar" o merge em andamento e voltar ao estado anterior ao conflito.

---

[:octicons-arrow-right-24: Ver Solução](solutions/solucao-05.md)
