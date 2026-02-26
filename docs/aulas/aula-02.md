# Aula 02 – Instalando e Configurando o Git

## 🎯 Objetivos de Aprendizagem
- Instalar o Git no seu sistema operacional (Windows, Mac ou Linux).
- Configurar sua identidade global (nome e e-mail).
- Verificar e validar a instalação e o ambiente.
- Entender a importância da configuração de autoria.

---

## 📚 Conteúdo

### 1. Preparando o Ambiente
Para começar a usar o Git, precisamos de duas coisas: a ferramenta instalada e uma identidade configurada.

```mermaid
flowchart LR
    A[Download] --> B[Instalação]
    B --> C[Terminal / Git Bash]
    C --> D[Configurar Nome]
    D --> E[Configurar Email]
    E --> F[Validar! OK]
```

#### Windows
- Acesse [git-scm.com](https://git-scm.com) e baixe a versão para Windows.
- No instalador: mantenha o padrão (Vim) ou selecione **VS Code** se preferir.
- **Dica**: No Windows, sempre use o **Git Bash** que vem junto na instalação. Ele emula um terminal Linux/Unix robusto.

#### macOS
- Instale via Homebrew: `brew install git`.
- Ou baixe o instalador no site oficial.

#### Linux (Ubuntu/Debian)
- Execute: `sudo apt-get update && sudo apt-get install git-all`.

### 2. Configuração de Identidade (Obrigatória)
O Git registra quem fez cada alteração. Sem isso, você não consegue fazer "commits".

!!! important "Configuração Global"
    As configurações abaixo precisam ser feitas apenas uma vez no seu computador.

<!-- termynal -->
```bash
# Configure seu nome profissional
$ git config --global user.name "Seu Nome Completo"

# Configure seu e-mail (prefira o mesmo do GitHub)
$ git config --global user.email "seu.email@exemplo.com"
```

!!! tip "Dica de Ouro"
    Use o e-mail que você pretende usar na sua conta do GitHub para que seu gráfico de contribuições ("paredão verde") seja contabilizado corretamente.

### 3. Onde as configurações ficam salvas?
O Git guarda essas informações em um arquivo chamado `.gitconfig` na sua pasta de usuário (`HOME`).

!!! info "Verificando tudo"
    Para listar todas as configurações ativas e confirmar se seu nome e e-mail estão corretos, use:
    <!-- termynal -->
    ```bash
    $ git config --list
    user.name=Seu Nome Completo
    user.email=seu.email@exemplo.com
    core.editor=vim
    ```

---

## 📝 Prática

### Exercícios de Fixação
Coloque a mão na massa instalando e configurando sua máquina.
[:octicons-arrow-right-24: Ver Exercícios da Aula 02](../exercicios/exercicio-02.md)

### Mini-Projeto
Garantindo que sua pasta de portfólio está pronta para o terminal.
[:octicons-arrow-right-24: Ver Projeto da Aula 02](../projetos/projeto-02.md)
