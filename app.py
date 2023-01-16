import streamlit as st
import openai

def get_openai_answer(post_content):
    # Get API key
    openai.api_key = st.secrets["api-keys"]["open_ai"]

    # Set the model and compose the prompt
    model_engine = "text-davinci-003"
    prompt = f"Write a catchy linkedin post about {post_content}"

    # Set the maximum number of tokens to generate in the response
    max_tokens = 1024

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Get the response
    answer = completion.choices[0].text

    return answer

# Write intro text
st.write("Welcome to the LinkedIn post generator!")

# Get input
user_input = st.text_input("Describe what you would like to have a LinkedIn post about: ")

# Wait until click
if(st.button("Generate LinkedIn post")):
    answer = get_openai_answer(user_input)
    # Write answer
    st.write(answer)