# 🚀 Introdução ao Git e Github

Este guia oferece uma introdução abrangente ao Git e GitHub, ferramentas essenciais para o desenvolvimento de software moderno. Abordaremos desde a instalação e configuração até os fluxos de trabalho básicos e comandos úteis.

## 💻 Instalação do Visual Studio Code

Para acompanhar os exemplos e praticar, é recomendável ter um editor de código instalado. O Visual Studio Code (VS Code) é uma excelente opção gratuita e amplamente utilizada.

Você pode baixá-lo em: [https://code.visualstudio.com/download](https://code.visualstudio.com/download)

Existem vídeos de instalação disponíveis para Windows e Ubuntu, caso precise de auxílio.

## 🤔 Visão geral de Git e Github

### O que é Git?
**Git** é um sistema de controle de versionamento distribuído. Ele permite que você controle as modificações de um projeto ao longo do tempo por meio de versões chamadas "commits". Cada commit é como uma fotografia do seu projeto em um determinado ponto, registrando o que foi alterado.

Imagine o histórico de um projeto como uma linha do tempo de commits:
`e8aab78 (commit 1) <-- 38k2ane (commit 2) <-- c9g57ef (commit 3) <-- k2f89m3 (commit 4)`

**Benefícios do Git:**
* **Histórico de Alterações:** Você pode ver quem alterou o quê e quando.
* **Reversão de Mudanças:** Facilidade para voltar a versões anteriores do projeto caso algo dê errado.
* **Trabalho em Equipe:** Permite que múltiplos desenvolvedores trabalhem no mesmo projeto de forma organizada, gerenciando diferentes versões e mesclando contribuições.
* **Ramificações (Branches):** Desenvolvedores podem trabalhar em novas funcionalidades ou correções de forma isolada em "branches" sem afetar a versão principal do projeto.

### O que é Github?
**Github** é uma plataforma online que hospeda repositórios Git remotos. Ele adiciona uma camada de colaboração e gerenciamento sobre o Git.

* **Interface Gráfica Web:** Oferece uma interface amigável (github.com) para visualizar e gerenciar seus repositórios.
* **Plataforma Social:** Funciona como uma rede social para desenvolvedores, com perfis de usuário, seguidores, e ferramentas para colaboração em projetos. É uma excelente vitrine para seu portfólio!
* **Hospedagem de Projetos:** É o maior serviço do mundo para hospedar projetos de código aberto.
* **Modelo de Cobrança:** Gratuito para projetos de código aberto e oferece planos pagos para projetos privados com funcionalidades adicionais.
* **Alternativas:** Existem outras plataformas similares como BitBucket e GitLab.

### Repositório Remoto e Local
Um projeto controlado pelo Git é chamado de **repositório**.

1.  **Servidor (Repositório Remoto):** Geralmente, uma cópia "oficial" do repositório fica salva em um servidor online (como o Github). Este é o repositório remoto.
2.  **Seu Computador (Repositório Local):** Cada pessoa que trabalha no projeto faz uma cópia (um "clone") desse repositório para seu próprio computador. Este é o repositório local.
3.  **Fluxo de Trabalho:**
    * Você faz alterações no seu repositório local (criando novos commits).
    * Depois, você envia ("push") essas alterações para o repositório remoto no servidor, atualizando a cópia oficial e compartilhando suas mudanças com a equipe.
    * Para receber as atualizações feitas por outros colaboradores, você "puxa" ("pull") as alterações do repositório remoto para o seu local.

**Fluxo Visual Simplificado:**

* **Do Servidor para seu Computador:**
    1.  `CLONE` (primeira vez) ou `PULL` (para atualizações)
        * Servidor (ex: Github) -> Seu Computador

* **Do Seu Computador para o Servidor:**
    1.  `COMMIT` (salva alterações localmente)
        * Seu Computador
    2.  `PUSH` (envia commits para o servidor)
        * Seu Computador -> Servidor (ex: Github)

## 🛠️ Instalação e Configuração do Git

### Instalação do Git no Computador
Antes de usar o Git, você precisa instalá-lo.
Você pode encontrar os downloads e instruções em: [https://git-scm.com/downloads](https://git-scm.com/downloads)

**Observação Importante para Usuários Windows:** Durante a instalação, na seção "Choose a credential helper" (Escolha um gerenciador de credenciais), **não escolha** a opção "Git Credential Manager Core" se quiser seguir algumas configurações mais tradicionais ou se encontrar problemas. A opção "None" (Não usar um gerenciador de credenciais) ou a versão mais antiga "Git Credential Manager" (se disponível e você souber como configurá-la) podem ser alternativas, mas a configuração de chaves SSH (abordada adiante) é o método mais robusto para autenticação com o Github.

### Configurando sua Identificação no Git
Após a instalação, configure seu nome de usuário e email. Essa informação será usada para identificar seus commits.

Abra um terminal ou prompt de comando e execute:
```bash
git config --global user.name "Seu Nome Completo"
git config --global user.email "seu_email_cadastrado_no_github@exemplo.com"
```
Para verificar as configurações:
```bash
git config --list
```

## ⚙️ Configurações Adicionais

### Configuração para Ver Arquivos Ocultos (Windows)
Para algumas operações com Git ou para ver pastas como `.git`, pode ser útil configurar o Windows para mostrar arquivos e pastas ocultas e extensões de arquivos.

1.  Abra o "Explorador de Arquivos".
2.  Vá em "Exibir" (no Windows 10/11) ou "Organizar" -> "Opções de pasta e pesquisa" (Windows 7).
3.  Na aba "Modo de Exibição" (ou "View"):
    * **DESMARQUE** a opção: "Ocultar as extensões dos tipos de arquivos conhecidos".
    * **MARQUE** a opção: "Mostrar arquivos, pastas e unidades ocultas".

### Configurar Chave SSH para o Github 🔑
**SSH (Secure Shell)** é um protocolo para comunicação de dados segura. O Github utiliza chaves SSH para autenticação segura entre seu computador e os servidores do Github, sendo o método preferencial e mais seguro, especialmente porque o Github aboliu a autenticação apenas com usuário e senha para operações Git.

**A ideia básica é:**
1.  Você gera um par de chaves SSH (uma pública e uma privada) no seu computador.
2.  Você cadastra a sua **chave pública** na sua conta do Github.
3.  Quando você tenta se conectar ao Github, ele usa esse par de chaves para verificar sua identidade. Seu computador só será autorizado se possuir a chave privada correspondente à pública cadastrada.

**Passos gerais:**
1.  **Gerar uma chave SSH no seu computador:**
    * Geralmente, usa-se o comando `ssh-keygen` no terminal.
    ```bash
    ssh-keygen -t ed25519 -C "seu_email_cadastrado_no_github@exemplo.com"
    ```
    * Siga as instruções, pressionando Enter para aceitar os locais padrão e, opcionalmente, definindo uma senha para sua chave (recomendado).
2.  **Cadastrar essa chave no seu Github:**
    * Copie o conteúdo da sua chave pública (normalmente no arquivo `~/.ssh/id_ed25519.pub` ou `~/.ssh/id_rsa.pub`).
    * No Github, vá em *Settings* -> *SSH and GPG keys* -> *New SSH key*. Cole sua chave lá.

Com a chave SSH configurada, as operações como `push`, `pull` e `clone` (usando URLs SSH) não pedirão mais seu usuário e senha do Github repetidamente.

## 🔄 Fluxo de Trabalho Básico com Git e Github

Considerando que seu ambiente já está todo configurado (Git instalado, usuário e email definidos, chave SSH configurada no Github), estes são os passos básicos.

### Passo a passo: Salvando a Primeira Versão de um Projeto no Github
Estes comandos são usados quando você tem um projeto local que ainda não está no Git/Github.

1.  **`git init`**
    * **O que faz:** Inicializa um novo repositório Git na pasta atual do seu projeto. Cria uma subpasta oculta chamada `.git` que armazena todas as informações do versionamento.
    ```bash
    git init
    ```

2.  **`git add .`**
    * **O que faz:** Adiciona todos os arquivos e modificações do seu diretório de trabalho atual à "área de stage" (preparação). O `.` significa "todos os arquivos e pastas a partir do diretório atual". Se quiser adicionar arquivos específicos, substitua `.` pelo nome do arquivo (ex: `git add README.md`).
    ```bash
    git add .
    ```

3.  **`git commit -m "Mensagem explicativa"`**
    * **O que faz:** Salva as alterações que estão na área de stage como uma nova versão (commit) no seu repositório local. A mensagem deve ser descritiva, explicando o que foi feito neste commit (ex: "Commit inicial do projeto com estrutura básica").
    ```bash
    git commit -m "Primeiro commit: Estrutura inicial do projeto"
    ```

4.  **`git branch -M main`**
    * **O que faz:** Renomeia a branch atual para `main`. `main` é o nome padrão para a branch principal de muitos projetos atualmente (substituindo o antigo `master`). Se você já está em uma branch chamada `main` ou prefere outro nome, este passo pode ser ajustado.
    ```bash
    git branch -M main
    ```

5.  **`git remote add origin git@github.com:seu_usuario_github/nome_do_seu_repositorio.git`**
    * **O que faz:** Conecta seu repositório local a um repositório remoto no Github.
        * `origin`: É um apelido (nome padrão) para o seu repositório remoto.
        * `git@github.com:seu_usuario_github/nome_do_seu_repositorio.git`: É a URL SSH do seu repositório no Github. Você precisa criar um repositório vazio no Github primeiro para obter essa URL. Substitua `seu_usuario_github` e `nome_do_seu_repositorio`.
    ```bash
    # Exemplo:
    # git remote add origin git@github.com:fulano-de-tal/meu-projeto-incrivel.git
    ```

6.  **`git push -u origin main`**
    * **O que faz:** Envia os commits da sua branch `main` local para o repositório remoto `origin` no Github.
        * `-u` (ou `--set-upstream`): Cria uma ligação entre sua branch local `main` e a branch `main` remota. Nas próximas vezes que fizer push desta branch, você poderá usar apenas `git push`.
    ```bash
    git push -u origin main
    ```

### Passo a passo: Salvando uma Nova Versão (Commit e Push)
Após o primeiro push, para salvar novas alterações:

1.  **Modifique seus arquivos.**
2.  **`git status`** (Opcional, mas recomendado)
    * **O que faz:** Mostra o estado dos seus arquivos: quais foram modificados, quais são novos (untracked), etc. Ajuda a ver o que será incluído no próximo commit.
    ```bash
    git status
    ```
3.  **`git add .`** (ou `git add <arquivo_especifico>`)
    * **O que faz:** Adiciona as alterações desejadas à área de stage.
    ```bash
    git add .
    ```
4.  **`git commit -m "Mensagem explicativa da nova versão"`**
    * **O que faz:** Cria um novo commit com as alterações preparadas.
    ```bash
    git commit -m "Adiciona funcionalidade de login"
    ```
5.  **`git push`**
    * **O que faz:** Envia seus novos commits locais (da branch atual) para o repositório remoto (`origin`).
    ```bash
    git push
    ```

### Clonando e Modificando um Projeto Remoto
Se o projeto já existe no Github e você quer baixá-lo e contribuir (assumindo que você tem permissão):

1.  **`git clone git@github.com:usuario_do_dono/nome_do_repositorio.git`**
    * **O que faz:** Baixa ("clona") um repositório remoto para o seu computador, criando uma cópia local. Use a URL SSH do repositório.
    ```bash
    # Exemplo:
    # git clone git@github.com:devsuperior/dsmovie.git
    ```
    * Isso cria uma pasta com o nome do repositório, já configurada para interagir com o `origin`.

2.  **Entre na pasta do projeto:**
    ```bash
    cd nome_do_repositorio
    ```

3.  **Faça suas modificações nos arquivos.**

4.  **`git add .`**
    ```bash
    git add .
    ```

5.  **`git commit -m "Mensagem sobre as modificações"`**
    ```bash
    git commit -m "Corrige bug na página de contato"
    ```

6.  **`git push`**
    ```bash
    git push
    ```

### Verificando o Histórico de Versões 📜
Para ver os commits feitos:

* **`git log`**
    * Mostra o histórico completo de commits, com detalhes como autor, data e mensagem de cada commit.
    ```bash
    git log
    ```

* **`git log --oneline`**
    * Mostra uma listagem resumida: o código do commit (hash) e a primeira linha da mensagem do commit. É útil para uma visão rápida.
    ```bash
    git log --oneline
    ```

## 🔍 Comandos Úteis do Git

### `git status`, `git add` e o "Stage" (Área de Preparação)
O Git tem um conceito chamado "área de stage" (ou "index"). É uma área intermediária onde você prepara as alterações que farão parte do próximo commit.

O fluxo é:
1.  **`modified` / `untracked` / `deleted` (Modificado / Não Rastreado / Deletado):** Seus arquivos no diretório de trabalho estão neste estado após você fazer alterações, criar novos arquivos ou deletar arquivos.
    * `git status` mostra esses arquivos.
2.  **`staged` (Preparado):** Você usa `git add <arquivo>` para mover as alterações desejadas do seu diretório de trabalho para a área de stage. Somente o que está "staged" será incluído no próximo commit.
3.  **`committed` (Commitado):** Você usa `git commit` para pegar tudo que está na área de stage e salvar permanentemente como uma nova versão (commit) no seu repositório local.

### `git diff`
* **O que faz:** Mostra as diferenças entre os arquivos modificados e a última versão commitada ou entre diferentes estados/commits.
    * `git diff`: Mostra as alterações no diretório de trabalho que ainda não foram para o stage.
    * `git diff --staged`: Mostra as alterações que estão no stage e prontas para o próximo commit.
* **Dica:** Ferramentas como VS Code e IntelliJ IDEA possuem interfaces gráficas excelentes para visualizar as diferenças (`diffs`) de forma mais intuitiva, destacando linhas adicionadas e removidas.

### `git checkout`: Navegando entre Versões
* **O que faz:** Permite modificar temporariamente os arquivos do seu projeto para o estado de um dado commit ou branch. É como "viajar no tempo" para ver o projeto como ele estava em um ponto anterior.

* **Referenciando Commits:**
    * Cada commit possui um **código hash** único (ex: `e8aab78f9f21b752051707575a75b6f9a789d13a`). Você pode usar os primeiros caracteres desse hash.
    * **`HEAD`**: É uma referência especial que aponta para o último commit do histórico da branch corrente.
    * **`HEAD~N`**: Permite referenciar um commit N versões antes de `HEAD`.
        * `HEAD~1`: Penúltimo commit.
        * `HEAD~2`: Antepenúltimo commit.

    ```bash
    # Voltar para o estado de um commit específico (use o hash do commit)
    git checkout <hash_do_commit>

    # Voltar para o penúltimo commit
    git checkout HEAD~1

    # Para voltar para o commit mais recente da sua branch (geralmente 'main')
    git checkout main
    ```

* **⚠️ IMPORTANTE:** Antes de fazer `checkout` para um commit anterior, certifique-se de que não haja mudanças não salvas (não commitadas) nos seus arquivos. O Git pode impedir a operação ou você pode perder alterações.
    * Se você acidentalmente mudou alguma coisa e quer desfazer as modificações nos arquivos para o estado do último commit (HEAD):
        ```bash
        # Descarta todas as alterações nos arquivos monitorados para o estado do último commit
        git checkout -- .

        # Para remover arquivos não rastreados (novos arquivos que nunca foram adicionados/commitados)
        # CUIDADO: isso deleta os arquivos permanentemente!
        git clean -df
        ```
    * `git reset` também é usado para desfazer commits ou alterações no stage, mas é um comando mais complexo com diferentes modos de operação.

### Ignorando Arquivos com `.gitignore` 🚫
* **O que é:** O `.gitignore` é um arquivo de texto simples onde você lista os arquivos e pastas que o Git deve **ignorar**. Arquivos ignorados não serão rastreados, adicionados ao stage ou commitados.
* **Localização:**
    * Geralmente, o arquivo `.gitignore` fica salvo na pasta principal (raiz) do repositório.
    * Também é possível ter arquivos `.gitignore` em subpastas, aplicando regras de ignorar específicas para aquelas subpastas.

### O que Ignorar: Casos Comuns para `.gitignore`
Você deve ignorar arquivos que não precisam ser versionados, como:

1.  **Arquivos Compilados e de Build:**
    * Linguagens compiladas (Java, C#, C++, etc.) geram arquivos binários ou de build que não são o código-fonte.
    * **Java (Maven/Gradle):** `target/`, `build/`, `*.class`, `*.jar`, `*.war`
    * **C# (.NET):** `bin/`, `obj/`, `*.dll`, `*.exe`
    * **JavaScript (Builds):** `dist/`, `build/`, `out/`

2.  **Arquivos de Bibliotecas Externas (Dependências):**
    * Projetos modernos utilizam gerenciadores de pacotes que baixam bibliotecas externas. Essas bibliotecas não devem ser commitadas diretamente; em vez disso, commita-se o arquivo de configuração do gerenciador (ex: `package.json` para NPM, `pom.xml` para Maven, `build.gradle` para Gradle).
    * **JavaScript (NPM/Yarn):** `node_modules/`
    * **Java (Maven/Gradle):** As dependências são gerenciadas e não precisam ser explicitamente ignoradas no `.gitignore` da mesma forma que `node_modules`, pois os diretórios de build (`target/`, `build/`) que podem conter os `.jar`s das dependências já são ignorados.

3.  **Arquivos de Configuração da sua IDE:**
    * IDEs como VS Code, IntelliJ IDEA, Eclipse, etc., podem salvar pastas com configurações específicas do projeto ou do usuário dentro da pasta do projeto.
    * **VS Code:** `.vscode/`
    * **IntelliJ IDEA:** `.idea/`, `*.iml`
    * **Eclipse:** `.project`, `.classpath`, `.settings/`

4.  **Arquivos de Configuração e Temporários do Sistema Operacional:**
    * Sistemas operacionais criam arquivos ocultos ou temporários.
    * **macOS:** `.DS_Store`
    * **Windows:** `Thumbs.db`, `desktop.ini`
    * **Arquivos de Log:** `*.log`
    * **Arquivos Temporários:** `*.tmp`, `*~`

5.  **Arquivos de Credenciais e Sensíveis:**
    * Nunca commite senhas, chaves de API, ou qualquer informação sensível. Utilize variáveis de ambiente ou arquivos de configuração locais (que estejam no `.gitignore`) para isso.
    * Ex: `.env`, `config/secrets.yml`

**Exemplo de um arquivo `.gitignore` para um projeto Java (Maven):**
```gitignore
# Arquivos compilados e de saída do Java/Maven
target/
*.class
*.jar
*.war
*.ear

# Logs
*.log
LOGS/
logs/

# Arquivos de configuração de IDEs
.idea/
*.iml
*.ipr
*.iws
.project
.classpath
.settings/
.vscode/

# Arquivos do sistema operacional
.DS_Store
Thumbs.db

# Arquivos temporários
*.tmp
*~

# Arquivos de configuração local (exemplo)
local.properties
```

**Exemplo de um arquivo `.gitignore` para um projeto Node.js:**
```gitignore
# Dependências
node_modules/

# Arquivos de build
dist/
build/
out/

# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Arquivos de configuração de ambiente (mantenha o .env.example versionado)
.env
.env.local
.env.*.local

# Arquivos do sistema operacional
.DS_Store
Thumbs.db

# Arquivos de configuração de IDEs
.vscode/
.idea/
```

Lembre-se que existem templates de `.gitignore` bem completos para diversas linguagens e frameworks disponíveis no Github (por exemplo, no repositório [github/gitignore](https://github.com/github/gitignore)).

Este guia deve fornecer uma base sólida para começar a usar Git e Github. A prática leva à maestria, então comece a usar essas ferramentas em seus projetos!

## 📚 Recursos Adicionais
* [Documentação Oficial do Git](https://git-scm.com/doc)
* [Documentação do Github](https://docs.github.com/)
* [GitHub Learning Lab](https://lab.github.com/)
* [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf) - Um guia rápido com os comandos mais comuns do Git.
* [GitHub Guides](https://guides.github.com/) - Tutoriais e guias para iniciantes e usuários avançados.
* [Pro Git Book](https://git-scm.com/book/en/v2) - Um livro completo e gratuito sobre Git, disponível online.
* [GitHub Desktop](https://desktop.github.com/) - Uma aplicação desktop para gerenciar repositórios Git de forma gráfica, ideal para quem prefere uma interface amigável.
* [GitKraken](https://www.gitkraken.com/) - Uma ferramenta gráfica poderosa para gerenciar repositórios Git, com uma interface intuitiva e recursos avançados.
* [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials) - Uma série de tutoriais abrangentes sobre Git, cobrindo desde o básico até tópicos avançados.
