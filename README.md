# QABot-1 Accelerator 

## About QABot-1 Accelerator

QABot-1 accelerator is a template for provisioning custom QA (Question/Answer) Bots. The number "1" in QABot-1 indicates this is one of many different types or configurations of QA Bots in the Project Genaissance collection of bot accelerators.

QABot-1 can load your custom data, and allow you or your target users to have natural language conversations with a bot about your custom dataset. QABot-1 is hard-coded to use the OpenAI API's and currently supports the GPT-3.5-Turbo and GPT-4 Models. 

Rather than training the LLM with your custom data which can be very complex and costly, QABot-1 uses Retrieval Augmented Generation. 

Your custom dataset is used to created a Vectorized index, which is loaded into an in-memory vector database. When a user enters a question into the bot UI, the bot first queries the vector database that has your custom data loaded, and identifies which parts of your document have information related to the users question, and then provides the context from you document set along with the users query in an api call to the LLM. 

In many cases, the related context from your custom dataset is larger than the context window accepted by the LLM, in which case multiple API calls are made to the LLM to cumulitively improve the response based on all the related data in your custom dataset. 

The bot then returns the response back to the user.

### QABot-1 Specifications

QABot-1 uses the Llama-index python library to provide bot services. It uses the most basic llama-index use case with default settings as reflected in the web.py file. Llama-index provides a large variety of different methodologies to provide bot services, and additional accelerators in this series will be made to explore different approaches to providing QA services, both using Llama-index and with different OSS solutions. 

- Model Orchestration: Lllama-index
- Supported LLMs: GPT-3.5-turbo, GPT-4
- LLM Tuning Parameters:
  - Temperature: 0
- Embeddings Model: text-ada-002
- VectorDB: Llama-index VectorStoreIndex

## How to use QABot-1-Accelerator
The QABot-1 Accelerator is a template that uses the VMware Tanzu Application Platform (TAP) Application Accelerator solution to provide templating services. 

Typically a user would access the application accelerator service on a TAP instance which provides a wizard allowing a user to generate a package or repository with an instance of the QABot-1 Code customized with a users desired project name and configuration parameters. 

Once the user generates their own QABot-1 instance, they can customize and deploy their instance. Typically application accelerators are used for projects that are deployed to Kubernetes cluster(s) running Tanzu Application Platform, and accordingly qabot-1 can easily be deployed to TAP clusters. However, this accelerator has also been prepared such that a user can deploy as a container to a OCI Compatible Container host, or to Kubernetes, using the open source pack or kpack projects as describes in the DEPLOYING.md document in this repository.

## Data Ingestion

In some simple bot tutorials, data ingestion and data querying are done in a combined step, but, it is a better practice to seperate these processes. QABot-1 is optimized for a use case in which a container is packaged with your custom dataset. The bot itself assumes the data ingestion has already been completed and accepts a URL with the location of the pre-ingested data index made from your custom dataset. 

Accordingly, before you can build qabot-1, you will need to have saved storage context that can be loaded into a llama-index VectorStoreIndex in-memory database. You can ingest your data and create a saved storage context by following the steps below:

### How to ingest your data

The ingest.py function is included in this repo as a functional example of how to ingest data. If you want to maintain and update this data source over and extended period, it is recommended that you handle ingestion through a seperate out of band process, but, following the steps provided here will allow you to ingest the data needed to create a functional bot that will be able to answer natural language questions from the context provided by your document(s).

To ingest the data you would like to use for your chatbot, execute the following steps:

1. Create a folder within the same directory as this document named "ingest"
2. Save any files you want to ingest in the "ingest" directory. 
3. Update the ingest.py file with your openai api key where specified
4. (Recommended) Create a python virutal environment to execute the remaining steps
5. Do a pip install for openai, llamaindex and any other required python libraries. In some cases depending on the types of documents you are ingesting, if you try to execute ingest.py, it may fail and provide an error message indicating you need to install an additional library with pip. If this happens just pip install the specified library and re-execute ingest.py.
6. Execute the ingest.py file with python which, depending on your system should be the command `python3 ingest.py` or `python ingest.py`. This step will create a subdirectory named "storage" which will be loaded with a chunked and vectorized index of your document(s).
7. Tar and zip the storage directory, you can name the archive anything you want: `tar -czvf archive.tar.gz ./storage`
8. Upload you saved archive.tar.gz file to some unauthenticated file or blob store. Make sure the file can be downloaded using curl or wget without requiring authentication. 
9. The data ingestion step is now complete. To include this data in your chatbot build, make sure the URL to your archive.tar.gz file is specified as the file_url value in the init.py file. 