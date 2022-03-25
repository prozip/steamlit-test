import streamlit as st
import streamlit.components.v1 as components
import tensorflow as tf
from PIL import Image
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
    # uploaded_file = st.file_uploader("Choose a file")
    # if uploaded_file is not None:
    #     bytes_data = uploaded_file.getvalue()
    #     with open(UPLOADED_PATH + uploaded_file.name,"wb") as binary_file:
    #         binary_file.write(bytes_data)
    # if st.button('Run'):
    #     os.system("rm -r yolov5/runs")
    #     # os.system("python yolov5/detect.py --weights yolov5/yolov5l.pt --img 640 --conf 0.25 --source uploaded_file")
    #     image = Image.open('yolov5/runs/detect/exp/' + uploaded_file.name)
    #     st.image(image, caption='Finised')


if __name__ == "__main__":
    cleanup_file()
    main()
    hide()
