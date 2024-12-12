# Import necessary libraries
import streamlit as st
import os
from openai import OpenAI

# To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings. 
# Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
#client = OpenAI(
#    base_url="https://models.inference.ai.azure.com",
#    api_key=os.environ["GITHUB_TOKEN"],
#)

import os
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference.models import SystemMessage, UserMessage

client = ChatCompletionsClient(
    endpoint=os.environ["AZUREAI_ENDPOINT_URL"],
    credential=AzureKeyCredential(os.environ["AZUREAI_ENDPOINT_KEY"]),
)

# Initialize the OpenAI API key
# Please replace 'your_openai_api_key' with your actual OpenAI API key.

# Define a function to ask GPT-4 for an explanation
def get_joke_explanation(joke):
    try:
        #chat_completion = client.chat.completions.create(
        #messages=[
        #{
        #    "role": "user",
        #    "content": f"Explain this joke: {joke}",
        #}
        #],
        #model="gpt-4o-mini",
        #)
        #print(chat_completion.choices[0].message.content)
        #return chat_completion.choices[0].message.content
        #client = ChatCompletionsClient(
        #endpoint=endpoint,
        #credential=AzureKeyCredential(api_key),
        #)

        response = client.complete(
            messages=[
                SystemMessage(content="You are a helpful assistant."),
                UserMessage(content=f"Explain this joke: {joke}"),
            ],
            temperature=1.0,
            top_p=1.0,
            max_tokens=1000,
            model="4o-miniJF"
        )

        print(response.choices[0].message.content)
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit app starts here
st.title("Joke Explainer")

# Text input for entering the joke
joke = st.text_area("Enter a joke that you want explained:")

# Button to submit the joke
if st.button("Submit"):
    if joke:
        explanation = get_joke_explanation(joke)
        st.subheader("Explanation")
        st.write(explanation)
    else:
        st.write("Please enter a joke to get an explanation.")