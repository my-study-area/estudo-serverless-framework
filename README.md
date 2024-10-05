# estudo-serverless-framework
![GitHub top language](https://img.shields.io/github/languages/top/my-study-area/estudo-serverless-framework)
![Terraform Version](https://img.shields.io/badge/Terraform-v1.6.4-blue.svg)
[![Repository size](https://img.shields.io/github/repo-size/my-study-area/estudo-serverless-framework)](https://img.shields.io/github/repo-size/my-study-area/estudo-serverless-framework)
[![Last commit](https://img.shields.io/github/last-commit/my-study-area/estudo-serverless-framework)](https://github.com/my-study-area/estudo-serverless-framework/commits/master)

## tutorial-serverless-node-offline
- Node: v20.17.0
- NPM: 10.8.2

```bash
# entra no diretório
cd tutorial-servless-node-offline/

# instala as dependências
npm install

# inicie o serverless e caso necessário realize o seu login na plataforma
npx sls offline

# execute a lambda
curl 'http://localhost:3000/dev/hi'
```

## python example
```bash
# instala o serverless globalmente
npm install -g serverless

# executa a lambda
serverless invoke local -f hello

# executa a lambda passando objeto como event para lambda
serverless invoke local -f hello --data '{"a":"bar"}'

# executa a lambda passando objeto e uma variável
serverless invoke local -f hello \
--data '{"a":"bar"}' \
-e VAR1='algum valor'
```

## python-localstack-serverless
```bash
# entra no diretório
cd python-localstack-serverless

# instala dependências do node
npm install --save-dev serverless-localstack

# inicia o localstack
docker-compose up -d

# faz deploy da lambda no localstack
sls deploy --stage local

# execta a lambda com serverless
sls invoke -f hello --stage local

# lista os nomes das lambdas no localstack
aws lambda list-functions \
--endpoint-url http://127.0.0.1:4566 \
--query "Functions[].FunctionName[]"

# executa lambda no localstack com aws cli
aws lambda invoke \
--endpoint-url http://127.0.0.1:4566 \
--function-name mylambda-service-local-hello \
--output table result.txt
```

## Links
- [Como construir uma API poderosa com Node.js, Serverless e Lambda](https://medium.com/building-kovi/construindo-uma-aplica%C3%A7%C3%A3o-serverless-do-zero-cd0d70527d61)
- [Local development with Serverless](https://towardsaws.com/local-development-with-serverless-46a219876a67)
- [serverless invoke local](https://www.serverless.com/framework/docs/providers/aws/cli-reference/invoke-local)
- [Usando LocalStack junto com Serverless Framework: Um guia passo a passo](https://www.linkedin.com/pulse/usando-localstack-junto-com-serverless-framework-um-guia-felipe/?originalSubdomain=pt)
- [Repositório com exemplo de deploy manual de lambda empacotando as dependências](https://github.com/awsdocs/aws-lambda-developer-guide/tree/master/sample-apps/blank-python)
