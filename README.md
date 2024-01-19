# PDF Mixer
PDF Mixer é um script em Python que oferece funcionalidades para processar e manipular arquivos PDF. O script permite personalizar a configuração, incluindo o caminho de entrada, se deseja randomizar a ordem das páginas e páginas específicas para excluir de cada PDF.

## Recursos
> - Exclusão de Páginas: Remova páginas específicas de cada arquivo PDF com base na configuração.  <br />
> - Randomização de Páginas: Opcionalmente, randomize a ordem das páginas no PDF de saída. <br />
> - Configuração: Personalize o comportamento do processamento editando o arquivo settings.json. <br />

## Pré-Requisitos
Antes de prosseguir com as instruções abaixo, certifique-se de que você possui uma versão atualizada do Python e instalou todos os requisitos listados no arquivo requirements.txt.

## Instalação e Uso
Ao colocar cada um dos arquivos desta página em uma pasta, inclua os PDFs que deseja processar nessa pasta e execute o arquivo run.bat. Dessa forma, eles serão processados de acordo com as configurações do arquivo JSON.

## Configuração
Certifique-se de que o arquivo settings.json está presente no diretório do script. Caso contrário, o script o criará com a configuração padrão. Em seguida, edite o arquivo settings.json para personalizar o comportamento do PDF Mixer. A configuração padrão é a seguinte:

```
  "path": "",
  "randomize": false,
  "deletable_pages": {
      "exemplo": [0, 1, 2]
  }
```

> - path: O caminho onde os arquivos PDF estão localizados. <br />
> - randomize: Se deseja ou não randomizar a ordem das páginas no PDF de saída. <br />
> - deletable_pages: Especifique as páginas a serem excluídas de cada PDF. O exemplo mostra a exclusão das páginas 0, 1 e 2 de um arquivo chamado "exemplo.pdf". <br />
