import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import io

# Set the title of the app
st.title("Word Cloud Generator")

# Text input for user to enter text
text_input = st.text_area("Enter text here:", height=300)

# Button to generate the word cloud
if st.button("Generate Word Cloud"):
    if text_input:
        # Generate word cloud
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_input)

        # Display the word cloud using matplotlib
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')  # Turn off axis
        plt.tight_layout()

        # Show the word cloud in Streamlit
        st.pyplot(plt)

        # Save the word cloud to a BytesIO object
        img_buffer = io.BytesIO()
        wordcloud.to_image().save(img_buffer, format='PNG')
        img_buffer.seek(0)

        # Provide a download button for the generated word cloud
        st.download_button(
            label="Download Word Cloud",
            data=img_buffer,
            file_name="wordcloud.png",
            mime="image/png"
        )
    else:
        st.warning("Please enter some text to generate a word cloud.")
