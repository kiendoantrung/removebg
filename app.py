import streamlit as st
from PIL import Image
from rembg import remove
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.title("Remove Background")
file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])


def removeBackground(img):
    img = Image.open(img)
    result = remove(img)

    result.save("result.png")

    st.image(
        result,
        caption=f"Your image has been processed",
        use_column_width=True,
    )


def downloadFileResult():
    file = open("result.png", "rb")
    bytes = file.read()
    st.download_button(label="Download Result", data=bytes,
                       file_name="result.png", mime="image/png")


if file is not None:
    image = Image.open(file)

    st.image(
        image,
        caption=f"It's look amazing!",
        use_column_width=True,
    )
    if st.button("Remove Background"):
        removeBackground(file)
        downloadFileResult()
