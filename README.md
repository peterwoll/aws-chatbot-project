# AWS Bedrock RAG Chatbot Using Python and Boto3

## Project Overview

This project implements a Retrieval-Augmented Generation (RAG) chatbot using Amazon Bedrock, Python, and Boto3.

The chatbot retrieves relevant information from an Amazon Bedrock Knowledge Base and generates conversational answers using Amazon Nova Lite.

The application also supports follow-up questions and displays citations identifying the source documents used to generate answers.

## AWS Services and Technologies

- **Amazon Bedrock:** Managed generative AI service.
- **Amazon Bedrock Knowledge Bases:** Retrieves relevant information from indexed documents.
- **Amazon S3:** Stores source documents.
- **Amazon S3 Vectors:** Provides vector storage and similarity search.
- **Amazon Titan Text Embeddings v2:** Generates document embeddings.
- **Amazon Nova Lite:** Generates conversational responses.
- **AWS CloudShell:** Development and testing environment.
- **Python 3.13 and Boto3:** Application programming language and AWS SDK.

## Architecture

The application follows this workflow:

1. A user enters a question in the Python command-line chatbot.
2. Boto3 calls the Amazon Bedrock `RetrieveAndGenerate` API.
3. Bedrock retrieves relevant document content through the Knowledge Base and its S3 Vectors store.
4. Amazon Nova Lite generates an answer using the retrieved information.
5. The Python application displays the answer and source citations.
6. Bedrock maintains session context for follow-up questions.

## Implementation

1. Created an S3 bucket containing `aws-services.txt`.
2. Created a Bedrock Knowledge Base named `rag-chatbot-kb`.
3. Configured Titan Text Embeddings v2 and Amazon S3 Vectors.
4. Synchronized the S3 data source with the Knowledge Base.
5. Tested retrieval and answer generation in the AWS Console.
6. Developed `chatbot.py` using Python and Boto3.
7. Configured the Amazon Nova Lite inference profile.
8. Added source citation handling and conversation session support.
9. Tested the application using AWS CloudShell.

## Project Files

- `chatbot.py` — Python chatbot application.
- `requirements.txt` — Python dependencies.
- `README.md` — Project documentation.

## Prerequisites

- AWS account with access to Amazon Bedrock.
- An existing Bedrock Knowledge Base containing synchronized documents.
- Access to Amazon Nova Lite and the required IAM permissions.
- Python 3.13 or another compatible Python 3 version.
- Boto3 installed.

## Installation

Clone the repository and install the dependencies:

```bash
pip3 install -r requirements.txt
```

Configure AWS credentials and update the Knowledge Base ID, inference profile ARN, and AWS Region in `chatbot.py` for your environment.

Run the application:

```bash
python3 chatbot.py
```

## Example Conversation

**User:** What is Amazon S3?

**Chatbot:** Amazon S3 is an object storage service that stores files in buckets. It offers versioning, encryption, and lifecycle management.

**Sources:** aws-services.txt

**User:** What are its main features?

**Chatbot:** Provides a contextual answer using the Knowledge Base and conversation history.

## Testing Results

The application was successfully tested using AWS CloudShell.

Verified functionality:

- Successful connection to the Bedrock Knowledge Base.
- Retrieval of relevant document information.
- Generation of answers using Amazon Nova Lite.
- Display of source document citations.
- Successful contextual follow-up questions.
- Successful Python syntax validation.

## Future Enhancements

- Add a web interface using Streamlit.
- Support multiple documents and additional AWS topics.
- Improve error handling and logging.
- Externalize configuration using environment variables.
- Deploy the chatbot as a hosted application.

## Project Status

**Completed:** Working command-line RAG chatbot with source citations and multi-turn conversation support.
