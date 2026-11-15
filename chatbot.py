
import boto3
from botocore.exceptions import ClientError

# AWS configuration
REGION = "us-east-1"
KNOWLEDGE_BASE_ID = "5RDKWENJKX"

# Amazon Nova Lite 1.0 inference profile
MODEL_ARN = (
    "arn:aws:bedrock:us-east-1::"
    "inference-profile/us.amazon.nova-lite-v1:0"
)

# Create Bedrock client
client = boto3.client(
    "bedrock-agent-runtime",
    region_name=REGION
)


def ask_question(question, session_id=None):
    """Ask the Bedrock Knowledge Base a question."""

    request = {
        "input": {"text": question},
        "retrieveAndGenerateConfiguration": {
            "type": "KNOWLEDGE_BASE",
            "knowledgeBaseConfiguration": {
                "knowledgeBaseId": KNOWLEDGE_BASE_ID,
                "modelArn": MODEL_ARN
            }
        }
    }

    # Reuse session for follow-up questions
    if session_id:
        request["sessionId"] = session_id

    response = client.retrieve_and_generate(**request)

    answer = response["output"]["text"]
    new_session_id = response.get("sessionId")

    return answer, new_session_id


def main():
    print("\nAWS Bedrock RAG Chatbot")
    print("-----------------------")
    print("Type 'exit' to quit.\n")

    session_id = None

    while True:
        question = input("You: ").strip()

        if question.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        if not question:
            continue

        try:
            answer, session_id = ask_question(
                question, session_id
            )
            print(f"\nChatbot: {answer}\n")

        except ClientError as error:
            print(f"\nAWS error: {error}\n")


if __name__ == "__main__":
    main()

