# README

aws lambda create-function \
    --endpoint-url http://0.0.0.0:4566 \
    --profile localstack \
    --function-name hello-world \
    --runtime "python3.9" \
    --role arn:aws:iam::123456789012:role/lambda-ex \
    --code S3Bucket="hot-reload",S3Key="$PWD" \
    --handler handler.hello

aws lambda invoke \
    --endpoint-url http://0.0.0.0:4566 \
    --profile localstack \
    --function-name serverless-python-rest-api-with-dynamodb-local-list \
    output.txt

aws lambda invoke \
    --endpoint-url http://0.0.0.0:4566 \
    --profile localstack \
    --function-name localstack-lambda-local-hello \
    output.txt

aws lambda invoke \
    --endpoint-url http://0.0.0.0:4566 \
    --profile localstack \
    --function-name hello-world \
    --payload '{"action": "test"}' output.txt


aws dynamodb list-tables \
    --endpoint-url http://0.0.0.0:4566 \
    --profile localstack



executa lambda
curl -XPOST "http://localhost:4566/2015-03-31/functions/my-serverless-service-local-hello/invocations"


curl -XPOST "http://localhost:4566/2015-03-31/functions/my-serverless-service-local-hello/invocations"


aws --endpoint-url http://0.0.0.0:4566 lambda list-functions --profile localstack 



history
curl -XPOST "http://localhost:4566/2015-03-31/functions/my-serverless-service-local-hello/invocations"
curl -XPOST "http://localhost:4566/2015-03-31/functions/my-serverless-service-local-hello/invocations" -d '{}'
aws --endpoint-url http://0.0.0.0:4566 lambda list-functions
curl -XPOST "http://localhost:4566/2015-03-31/functions/hello/invocations" -d '{}'
curl -XPOST "http://localhost:4566/2015-03-31/functions/function/invocations" -d '{}'
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
aws lambda invoke --function-name my-serverless-service-local-hello --payload '{"key1": "value1", "key2": "value2"}' response.txt --endpoint-url http://localhost:4566
aws lambda invoke --function-name my-serverless-service-local-hello --payload '{"key1": "value1", "key2": "value2"}' response.json --endpoint-url http://localhost:4566
sls deploy --stage local --aws-profile localstack
sls dev
aws lambda invoke --function-name my-serverless-service-local-hello --payload '{"key1": "value1", "key2": "value2"}'  --endpoint-url http://localhost:4566
sls invoke -f hello --stage local
history | grep curl | grep 4566
docker ps
serverless invoke -f hello --data '{"a":"bar"}' --stage local
serverless invoke -f hello --data '{"a":"bar"}' --stage dev
serverless invoke -f hello --data '{"a":"bar"}' 
serverless invoke local -f hello --data '{"a":"bar"}' 
sls invoke -f lambda_handler --stage local
localstack --version
npm install --save-dev serverless-localstack
cat ~/.aws/config 
aws configure list 
aws configure list --profile default
aws configure --help
aws configure --profile default
sls deploy --stage local --aws-profile adriano
sls deploy --stage local
python
serverless invoke local -f hello
aws --endpoint-url http://0.0.0.0:4566 s3api create-bucket --bucket meu-buxket
aws --endpoint-url http://0.0.0.0:4566 s3 ls
aws --endpoint-url http://0.0.0.0:4566 s3api create-bucket --bucket sample-bucket
aws --endpoint-url http://0.0.0.0:8000 s3api create-bucket --bucket sample-bucket
pip freeze > requirements.txt
pip list 
touch requirements.txt
cd /mnt/windows/adriano/temp/download/testes/lambda-localstack/lambda-localstack-serverless/my-serverless-service/



# aws

# cria role para lambda
# arn:aws:iam::834635717119:role/lambda-ex
aws iam create-role \
--profile sandbox \
--role-name lambda-ex --assume-role-policy-document \
'{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal":
{"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'

# lista as roles criadas
aws iam list-roles --profile sandbox

# adiciona permissão de execução na role lambda-ex
aws iam attach-role-policy \
--profile sandbox \
--role-name lambda-ex \
--policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

# lista as polices anexadas na role lambda-ex
aws iam list-attached-role-policies \
--profile sandbox \
--role-name lambda-ex

# cria a lambda
aws \
lambda create-function --function-name my-lambda-function \
--profile sandbox \
--zip-file fileb://lambda-ex.zip \
--handler lambda.handler --runtime python3.8 \
--role arn:aws:iam::834635717119:role/lambda-ex 

# lista as Lambdas
aws lambda list-functions --profile sandbox --query "Functions[].[FunctionName]"


# executando a lambda
aws \
lambda invoke --function-name my-lambda-function \
--profile sandbox \
out --log-type Tail --query 'LogResult' --output result.txt

