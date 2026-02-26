# Exercícios da Aula 07

## 🛠 Sincronização: Repositórios Remotos e .gitignore

### Nível: Básico

1.  **A Prática do Clone**:
    - Saia da pasta do seu projeto atual no terminal (`cd ..`).
    - Escolha um repositório público no GitHub (ex: um projeto de código aberto).
    - Utilize o comando de clonagem para baixar esse projeto completo para sua máquina. Qual o comando utilizado?

2.  **Verificando o Vínculo**:
    - Dentro da pasta do projeto que você acabou de clonar, digite um comando para listar os endereços remotos de `fetch` e `push`. O que o termo "origin" representa?

### Nível: Intermediário

3.  **Segurança com .gitignore**:
    - No seu repositório de testes, crie um arquivo chamado `configuracao_privada.txt`.
    - Crie (ou edite) o arquivo `.gitignore` na raiz e adicione o nome do arquivo acima dentro dele.
    - Tente adicionar o arquivo ao Git (`git add configuracao_privada.txt`). O que acontece?

4.  **Conexão Remota**:
    - Imagine que você criou um repositório local e agora quer vinculá-lo a um novo repositório vazio no GitHub. Qual o comando utilizado para adicionar esse "vínculo remoto" com o apelido `origin`?

### Nível: Desafio

5.  **Ignorando por Padrão**:
    - No seu arquivo `.gitignore`, adicione uma regra que ignore **todos** os arquivos que terminem com a extensão `.log`, independentemente do nome. Como você escreveu essa regra utilizando caracteres curinga?

---

[:octicons-arrow-right-24: Ver Solução](solutions/solucao-07.md)
