# 🤖 Automação de Cotação do Dólar via Bing

Este projeto é um script de automação simples desenvolvido em **Python** utilizando a biblioteca **Selenium**. O objetivo é abrir o navegador Microsoft Edge, pesquisar pela cotação atual do dólar no Bing e exibir o resultado no terminal.

## 📋 Funcionalidades

* **Abertura Automática:** Inicia uma instância do navegador Microsoft Edge.
* **Tratamento de Cookies:** Identifica e aceita automaticamente o popup de cookies do Bing (se aparecer).
* **Busca Automatizada:** Digita "Cotação Dólar" na barra de pesquisa e envia o comando.
* **Extração de Dados:** Captura o valor exato da cotação nos resultados da busca.
* **Encerramento Seguro:** Garante que o navegador seja fechado ao final da execução ou em caso de erro.

---

## 🛠️ Pré-requisitos

Antes de rodar o código, você precisa ter o seguinte instalado:

1.  **Python 3.x**: [Download aqui](https://www.python.org/downloads/)
2.  **Biblioteca Selenium**:
    ```bash
    pip install selenium
    ```
3.  **Microsoft Edge WebDriver**:
    * Você precisa baixar o `msedgedriver.exe` compatível com a versão do seu navegador Edge.
    * [Baixe aqui o WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
    * **Importante:** O arquivo `msedgedriver.exe` deve estar na mesma pasta que este script ou o caminho deve ser atualizado no código.

---

## 🚀 Como Executar

1.  Clone este repositório ou baixe o arquivo `.py`.
2.  Coloque o arquivo `msedgedriver.exe` na raiz do projeto.
3.  Execute o comando no terminal:

```bash
python nome_do_seu_arquivo.py
