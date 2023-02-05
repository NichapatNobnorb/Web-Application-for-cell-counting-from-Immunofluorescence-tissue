import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import time, datetime
from PIL import Image
import PIL.ImageOps   
from io import BytesIO
from matplotlib import cm
from ML import invert
from imagemks_function import vis,get_df,labelvis,cell_counting


st.set_page_config(
    page_title="Counting Nucleus",
    layout="wide"
)
st.markdown("""
        <style>
               .block-container {
                    padding-top: 5rem;
                    padding-bottom: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)

data = {'Nucleus': [1, 2, 3, 4],
        'Location X': [20.444, 21.22, 19.567, 18.234],
        'Location Y': [3.20, 0.21, 1.19, 2.18],
        'Area': [20, 21, 19, 18]}
df_result = pd.DataFrame(data)
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')


st.markdown("<h1 style='text-align: center; font-size:450%;'>Welcome to</h1>", unsafe_allow_html=True)
spacer,colh1,spacer = st.columns([13,11,10])
with colh1:
    imagehead = Image.open('logi-removebg.png')
    st.image(imagehead,width=300)
spacer,colh2,spacer = st.columns([1,2,1])
with colh2:
    st.markdown("<hr align='center' width='100%;' size='10'>  ", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; '>Web Application for cell counting from Immunofluorescence tissue</h4>", unsafe_allow_html=True)
st.text(" ")
st.write("#")
st.text(" ")
spacer,col1,spacer,col2,spacer = st.columns([1,6,1,4,1])
run = False
with col1:
    st.header('Upload Your Image')
    uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img , araaylable = cell_counting(image)
    imagee = Image.fromarray(img)
    df_result = get_df(araaylable)
    with col2:
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.image(image, caption='Your input Image')
    spacer,colrun,spacer = st.columns([8,1,10])
    with colrun:
        if st.button('RUN'):
            run = True
    if run:
        spacer,col3,spacer,col4,spacer = st.columns([1,6,1,4,1])
        with col3:
            st.header('Result')
            numbercell = len(df_result. index)
            st.markdown(
            """ ###### Number of Nucleus is <span style="background-color: #AA706A; color:white">{temp}</span> nucleus """.format(temp=str(numbercell))  , unsafe_allow_html=True)    
            csv = convert_df(df_result)
            st.write(df_result)
            
        with col4:
            st.write("#")
            st.text(" ")
            st.text(" ")
            st.text(" ")
            st.image(imagee, caption='Your result Image')
        spacer,col5,col6,spacer = st.columns([2,3,4,10])
        with col5:
            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='Result_Nucleus.csv',
                mime='text/csv',
            )
        with col6:
            buf = BytesIO()
            imagee.save(buf, format="png")
            byte_im = buf.getvalue()
            btn = st.download_button(
                label="Download Image",
                data=byte_im,
                file_name="result.png",
                mime="image/png"
                )
spacer,footer,spacer = st.columns([1,10,1])
with footer:
    st.markdown("<hr align='center' width='100%;' size='10'>  ", unsafe_allow_html=True)
spacer,footer3,footer2,spacer = st.columns([4,3,5,1])
with footer3:
    st.markdown("<h2 style='text-align: left; '>Members : </h2>  ", unsafe_allow_html=True)
with footer2:
    st.markdown("<p style='text-align: left; '>Ms. Kanchayapond Seajoong</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left; '>Ms. Nichapat Nobnorb</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left; '>Mr. Wayu Ragwongsiri</p>", unsafe_allow_html=True)
    st.text(" ")
st.markdown("<h6 style='text-align: center; '>Web Application for Automatic Nucleus Counting 3D Immunofluorescence Tissue Biopsies Using Image Processing</h6>", unsafe_allow_html=True)
st.text("A PROJECT SUBMITTED IN PARTIAL FULFILLMENT OF THE REQUIREMENTS FOR THE DEGREE OF BACHELOR OF SCIENCE (COMPUTER ENGINEERING) FACULTY OF ENGINEERING KING MONGKUT’S UNIVERSITY OF TECHNOLOGY THONBURI 2022")
#        st.info('☝️ Upload a image file')
    # with open(imagee, "rb") as file:
        # btn = st.download_button(
        #     label="Download image",
        #     data=file,
        #     file_name="result.png",
        #     mime="image/png"
        #   )
# with st.expander('About this app'):
#   st.write('This app shows the various ways on how you can layout your Streamlit app.')
#   st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)
# st.write('Hello world!')
# st.header('st.button')

# if st.button('Say hello'):
#      st.write('Why hello there')
# else:
#      st.write('Goodbye')
# if st.button('Upload Image'):
#      st.write('Why hello there')
# else:
#      st.write('Goodbye')
# if st.button('Save Image'):
#      st.write('Why hello there')
# else:
#      st.write('Goodbye')
# if st.button('Save Table'):
#      st.write('Why hello there')
# else:
#      st.write('Goodbye')
# st.selectbox('Save Table',('Save Table as CSV','Save Image'))