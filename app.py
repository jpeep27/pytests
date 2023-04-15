import openai
import streamlit as st

openai.api_key = "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"

def generate_conspiracy():
    prompt = (
        "Generate a funny, non-sensical conspiracy theory about anything."

    )
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=1.0,
    )
    conspiracy = response.choices[0].text.strip()
    return conspiracy

st.title("Conspiracy Generator")
st.write("Press the button below to generate a funny conspiracy theory.")

if st.button("Conspiracize"):
    conspiracy = generate_conspiracy()
    st.write(conspiracy)
