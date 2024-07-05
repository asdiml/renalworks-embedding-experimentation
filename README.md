## Experimentation with Embedding Tabular Data

This repository deals with 

## Using the Repo

To use the repo, create a [Python virtual environment](https://docs.python.org/3/library/venv.html) and install the dependencies found in [requirements.txt](requirements.txt). Upon activating the venv, this can be done with

```bash
pip install -r requirements.txt
```

You will also need access to Amazon Bedrock's Anthropic Claude v3 Sonnet and Titan Embedding v2.0 models, and ensure that your AWS SSO login is configured using the command

```cmd
aws configure sso
```

This requires that [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) is installed, and will prompt your input of some information that can be found when logging into your AWS IAM console. 

Once your profile is created in your `.aws/config` file, update your profile name in [bedrock_caller.py](./src/bedrock_caller.py), in the __init__ method. If you are using [01a_create_embeddings.ipynb](./01a_create_embedding.ipynb), you will need to update your profile name in the notebook as well. 

## Maintaining the Repo

To update the `requirements.txt` file, ensure that your Python virtual environment is activated and run (at the root of this repo)

```bash
pip freeze > requirements.txt
```

## Results

Results of generation can be found in the [results](./results) folder. For more detailed explanations, see [report.md](./report.md). 

## Credits

Credit is due to Farzad for the script to chunk the csv for embedding, as well as the code for similarity search. The original repo referenced can be found at [this link](https://github.com/Farzad-R/Advanced-QA-and-RAG-Series/commits?author=Farzad-R).
