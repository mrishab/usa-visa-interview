## Get Started


To run the project, add the value for your slack token in the placeholder and run the snippet once

## Setup Project

```
git clone git@github.com:mrishab/usa-visa-interview.git && \
cd usa-visa-interview/ && \
echo "SLACK_TOKEN=<PUT-SLACK-TOKEN-HERE>" > .env
```

## Local Development

To spin up a local environment, execute `make dev` and that will spin a docker container with mounts and env setup for you to run the code locally.

## Production

To execute the job, run `make run`.