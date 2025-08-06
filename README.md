# 🗂️ Gerador de Script de Mapeamento de Unidade de Rede

Este é um utilitário simples em Python com interface gráfica (Tkinter) que gera automaticamente um arquivo `.bat` para mapear uma unidade de rede no Windows.

## 🧩 Funcionalidades

- Interface gráfica amigável com Tkinter.
- Geração automática de um arquivo `.bat` para mapear pastas de rede (UNC).
- Verifica se o caminho já está mapeado antes de tentar mapear.
- Escolhe automaticamente a próxima letra de unidade disponível (de Z até D).
- Salva o script gerado diretamente na pasta **Downloads** do usuário.

---

## 🖥️ Captura de Tela

<img width="463" height="206" alt="image" src="https://github.com/user-attachments/assets/b831a65f-ddeb-46c5-9da6-b5290d9e84fd" />

---

## 🚀 Como Usar

### 1. Clonar o repositório

```bash
git clone https://github.com/Prof-Anderson-Sousa/GeradorMapeamentoDePastas.git
cd GeradorMapeamentoDePastas
2. Instalar dependências (Python ≥ 3.7)
Este projeto só usa bibliotecas da biblioteca padrão do Python. Nenhuma instalação extra é necessária.

3. Executar o programa

python index.py

📝 Exemplo de uso
Execute o programa.

Digite um caminho UNC válido (ex: \\servidor\compartilhamento).

Clique em Gerar.

Um arquivo .bat será salvo na pasta Downloads.

Ao executar o script .bat, a pasta será mapeada automaticamente para uma letra de unidade disponível (ex: Z:, Y:, ...).

📁 Estrutura do Projeto
GeradorMapeamentoDePastas/
├── index.py
├── README.md

🔐 Permissões
O script .bat gerado pode exigir permissões administrativas, dependendo da política de rede da sua empresa ou organização.

⚠️ Avisos
Este projeto é voltado para sistemas Windows.

O caminho deve obrigatoriamente começar com \\.

📄 Licença
Este projeto está licenciado sob a MIT License.

🤝 Contribuições
Pull requests são bem-vindos! Se você tiver sugestões de melhorias, novas funcionalidades ou ajustes, fique à vontade para abrir uma issue ou PR.

✉️ Contato
Para dúvidas ou sugestões:

GitHub: @Prof-Anderson-Sousa

Email: professorandersonsousa@gmail.com
