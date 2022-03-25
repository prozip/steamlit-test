import streamlit as st
import tensorflow as tf
import cv2
import os

UPLOADED_PATH = 'uploaded_file/'

def hide():
    hide_menu_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

    # my_html = f"<script>document.querySelector('footer > a').href = 'https://www.tensorflow.org/';</script>"
    # components.html(my_html)

def cleanup_file():
    os.system("rm -r " + UPLOADED_PATH)
    os.mkdir(UPLOADED_PATH)


def main():
    st.title("this is title")
    st.write("hello world")
    st.write("Tensorflow: ", tf.__version__)
    st.write("cv2: ", cv2.__version__)

if __name__ == "__main__":
    cleanup_file()
    main()
    hide()
