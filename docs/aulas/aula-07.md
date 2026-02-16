# Aula 07 – Criando e gerenciando repositórios no GitHub

## 🎯 Objetivos de Aprendizagem
- Criar um novo repositório no GitHub.
- Conectar um repositório local a um remoto (`git remote add`).
- Enviar alterações para a nuvem (`git push`).
- Baixar projetos existentes (`git clone`).
- Entender o arquivo `.gitignore`.

## 📚 Conteúdo

### 1. Criando um Repositório Remoto
No GitHub, clique no botão **New** (ou `+` no canto superior direito).
- Dê um nome (ex: `meu-primeiro-repo`).
- Escolha Público ou Privado.
- (Opcional) Inicializar com README, .gitignore ou License.

### 2. Conectando Local e Remoto
Se você já tem um repo local (como nosso portfólio), conecte-o assim:
```bash
git remote add origin https://github.com/SEU-USUARIO/NOME-DO-REPO.git
```
- **origin**: É apenas um apelido padrão para o link do repositório remoto.

### 3. Enviando Alterações (Push)
Para enviar seus commits locais para o servidor:
```bash
git push -u origin main
```
- `-u`: Configura o vínculo (upstream) para que nos próximos pushes você possa digitar apenas `git push`.

### 4. Baixando Projetos (Clone)
Para baixar um projeto completo do GitHub para seu computador:
```bash
git clone https://github.com/usuario/projeto.git
```
Isso cria uma pasta com todo o histórico do projeto.

### 5. Ignorando Arquivos (.gitignore)
Nem tudo deve ir para o Git (senhas, arquivos temporários, pastas de build).
Crie um arquivo chamado `.gitignore` e liste o que o Git deve ignorar:
```text
.env
node_modules/
*.log
```

## 📽 Roteiro de Slides
- Local vs Remoto: Conceito chave.
- Criando o "Balde" na Nuvem (New Repo).
- O Elo de Ligação: `git remote add origin URL`.
- O Envio: `git push` (Empurrar).
- O Download: `git clone` (Clonar).
- A Importância do `.gitignore` (Não suba lixo nem senhas!).

## 📝 Quiz
1. Qual comando envia commits locais para o GitHub?
2. O que é "origin" no comando `git push origin main`?
3. Qual comando copia um repositório inteiro do GitHub para sua máquina?
4. Para que serve o arquivo `.gitignore`?
5. Se eu quiser baixar apenas as atualizações de um repo já clonado, usaria `clone` novamente?

## Gabarito
1: C
2: B
3: A
4: D
5: B (Não, usaria `git pull` - spoiler da próxima aula, mas a resposta certa é "Não").

## 🛠 Exercícios
1. **GitHub**: Crie um repositório chamado `teste-remoto`. Não marque nenhuma opção (README, gitignore).
2. **Local**: Crie uma pasta `teste-local`, inicie o git, crie um arquivo e commite.
3. **Link**: Adicione o remote (`git remote add origin ...`).
4. **Push**: Envie (`git push -u origin main`).
5. **Confira**: Recarregue a página do GitHub e veja seu arquivo lá!

## 🚀 Projeto da Aula
Agora é a hora da verdade para o `meu-portfolio-git`.

1. Vá no GitHub e crie um novo repositório chamado `portfolio-dev`.
2. Não marque nenhuma opção de inicialização (README, etc). Crie o repo vazio.
3. Copie o link HTTPS fornecido (ex: `https://github.com/seu-user/portfolio-dev.git`).
4. No terminal do seu projeto local:
   ```bash
   git remote add origin COLAR_O_LINK_AQUI
   git branch -M main
   git push -u origin main
   ```
   *(Pode pedir login/senha. Se usar HTTPS, pode precisar de um Token ou Git Credential Manager).*
5. Vá ao GitHub e veja: Seu portfólio está online!
