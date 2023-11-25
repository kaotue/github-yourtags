sam build
sam deploy \
--stack-name github-yourtags-api \
--s3-bucket github-yourtags-api \
--capabilities CAPABILITY_NAMED_IAM \
--parameter-overrides GitHubApiUserName=$GITHUB_API_USER_NAME GitHubApiToken=$GITHUB_API_TOKEN