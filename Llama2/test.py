import re
import torch
import folium
import requests
import streamlit as st
import streamlit_folium
from transformers import pipeline, AutoTokenizer

# Function to initialize Llama-2 model and tokenizer
@st.cache(allow_output_mutation=True)
def initialize_llama_model():
    model_name = "meta-llama/Llama-2-7b-hf"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    llama_pipeline = pipeline("text-generation", model=model_name, torch_dtype=torch.float16, device='cuda')  # Load onto GPU device 0
    return tokenizer, llama_pipeline

# Function to query Overpass API
def query_overpass(query):
    payload = {"data": query}
    response = requests.post("https://overpass-api.de/api/interpreter", data=payload)
    return response.json()

# Streamlit app
def main():
    st.title("OSM Overpass Query App")
    st.write("Hello! I'm an AI assistant powered by Llama-2 model. Ask me anything about locations and I'll generate an Overpass query for you!")

    # Initialize model and tokenizer
    tokenizer, llama_pipeline = initialize_llama_model()

    prompt = st.text_area("What can I help you find?")

    if st.button("Generate Query"):
        # Generate Overpass query using Llama-2 model
        generated_query = llama_pipeline(prompt, max_length=300)[0]["generated_text"]
         # Remove user's prompt from generated query
        generated_query = re.sub(re.escape(prompt), '', generated_query, count=1).strip()

        # Display generated query
        st.write("Generated Overpass Query:")
        st.code(generated_query, language="text")

        # Query Overpass API
        response = query_overpass(generated_query)

        # Visualize results on map
        if "elements" in response and len(response["elements"]) > 0:
            st.write("Results found!")
            m = folium.Map(location=[response["elements"][0]["lat"], response["elements"][0]["lon"]], zoom_start=12)

            for element in response["elements"]:
                if "lat" in element and "lon" in element:
                    folium.Marker([element["lat"], element["lon"]]).add_to(m)

            streamlit_folium.folium_static(m)
        else:
            st.write("No results found :(")

if __name__ == "__main__":
    main()
