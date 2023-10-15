# estudo-serverless-framework

## tutorial-serverless-node-offline

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
- [Como construir uma API poderosa com Node.js, Serverless e Lambda](https://how.kovi.work/construindo-uma-aplica%C3%A7%C3%A3o-serverless-do-zero-cd0d70527d61)
- [Local development with Serverless](https://towardsaws.com/local-development-with-serverless-46a219876a67)
- [serverless invoke local](https://www.serverless.com/framework/docs/providers/aws/cli-reference/invoke-local)
- [Usando LocalStack junto com Serverless Framework: Um guia passo a passo](https://www.linkedin.com/pulse/usando-localstack-junto-com-serverless-framework-um-guia-felipe/?originalSubdomain=pt)
- [Repositório com exemplo de deploy manual de lambda empacotando as dependências](https://github.com/awsdocs/aws-lambda-developer-guide/tree/master/sample-apps/blank-python)
