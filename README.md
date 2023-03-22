# Exercício Cloud 

## Objetivo 

Utilizar a [API do Rick e Morty](https://rickandmortyapi.com/documentation) para extrair as informações dos episódios de Rick e Morty e disponibilizar as informações em um banco de dados para consulta de analistas, de forma a relacionar episódios, localizações e personagens.

## Passos

1. Criação de um bucket no Cloud Storage "Jerry Data". Esse bucket deve receber os dados crus, ou seja, diretamente vindos da API, sem nenhum tipo de transformação ou processamento. Nesse bucket será realizado um EL (Extract & Load). A função desse bucket é que os dados estejam sem nenhuma transformação aplicada, para que em casos de erros, seja possível retornar aos dados originais sem precisar extrair novamente da API;
2. Criação da camada de extração. Essa camada deve conter 3 cloud functions, uma para cada endpoint da API (localização, personagens e episódios). Cada cloud function deve rodar de tempos em tempos, de maneira automática; extrair os dados da API e armazena-los no bucket Jerry. É importante que cada cloud Function armazene os dados do seu enpoint em uma pasta específica, para melhor organização, e o nome do arquivo contenha a data de extração, por exemplo: nome-do-arquivo?extract-date=20220909;
3. Após a chegada dos dados no bucket Jerry, deve haver uma segunda camada de processamento para padronização e pré-processamento dos dados. Esta camada será responsável por padronizar as informações, podendo alterar os tipos de dados originais e padronizar o nome das chaves dos dados originais. Essa etapa de processamento deve ser acionada automaticamente após a chegada de um dado no bucket Jerry e armazenar o novo dado pré-processado no bucket Morty;
4. Semelhante a etapa 3, a ideia é que nessa etapa um novo processo de processamento de dados seja acionado após a chegada do dado no bucket Morty, e armazenado no bucket Rick. Nessa etapa é necessário que o dado seja tratado e processado de modo a facilitar ao máximo as análises. O schema resultante desse processamento deve ser o schema final das tabelas dos dados a serem consultados, portanto, analise os dados, defina um schema de tabela para realização das consultas e só então transforme os dados do bucket Morty para o schema que você definiu nessa etapa;
4. Linkar o Athena ao bucket Rick Data para consumo dos dados via SQL;
6. Crie um dashboard no Quicksight para visualização dos dados armazenados no BigQuery;
7. (Bônus): Realize a subida de toda a infraestrutura do projeto via terraform;
8. (Bônus): Verifique a possibilidade da utilização do Step Functions para orquestração das cloud functions;
9. (Bônus): Pesquise sobre os formatos de dados json, parquet e avro, e realize um levantamento de quais as vantagens de cada formato e se/onde você pode aplica-los na sua arquitetura.

