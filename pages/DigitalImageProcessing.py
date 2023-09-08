import streamlit as st
import sys
import cv2
import numpy as np
from PIL import Image
# import tkinter
# from tkinter import Tk, filedialog

import Chapter3 as c3
import Chapter4 as c4
import Chapter9 as c9

st.set_page_config(
    page_title="Image Processing",
    page_icon="📸",
)
st.markdown("<h2 style = 'text-align: center; font-size: 40px; font-family: comic sans ms, cursive; color: #800000;'>Image Processing</h2>", unsafe_allow_html=True)
st.sidebar.header("Digital Image Processing")

def imgin_header():
    imgin_Title = '<p style="font-family: Courier; color: #3333ff; font-size: 24px;"><b>Original Uploaded Image</b></p>'
    st.markdown(imgin_Title, unsafe_allow_html=True)
def imgout_header():
    imgout_Title = '<p style="font-family: Courier; color: #3333ff; font-size: 24px;"><b>Image after being processed</b></p>'
    st.markdown(imgout_Title, unsafe_allow_html=True)
def download_info():
    download_notice = '<p style="font-family: monospace; font-size: 14px; color: #c2c2d6;"><i>For downloading, please right click on the image.</i></p>'
    st.markdown(download_notice, unsafe_allow_html=True) 
    

option = st.sidebar.selectbox('Choose topic', ['--Select topic--', 'Chương 3', 'Chương 4', 'Chương 9'])
if option == 'Chương 3':
    img_upload = st.file_uploader('Upload Image', type=['jpg', 'tif', 'bmp', 'gif', 'png'])
    if img_upload is not None:
            global imgin
            filepath = '..\ProjectCuoiKy\ProcessingImage\Chuong3\\' + img_upload.name
            imgin = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            # imgin = img_upload.read()
            imgin_header()
            st.image(imgin)

            c3_function = st.sidebar.selectbox('Please pick up a function', [
                '--Select function--','Negative', 'Logarit', 'Power', 'PieceWiseLinear', 'Histogram',
                'HistogramEqualization', 'LocalHistogram', 'HistogramStatistics',
                'SmoothingGauss', 'Smoothing', 'MedianFilter', 'Sharpen', 'UnSharpMasking', 'Gradient'])
            # Negative
            if c3_function == 'Negative':
                global imgout
                imgout = np.zeros(imgin.shape, np.uint8)
                c3.Negative(imgin,imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>Negative</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # Logarit
            elif c3_function == 'Logarit':
                imgout = np.zeros(imgin.shape, np.uint8)
                c3.Logarit(imgin,imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>Logarit</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # Power
            elif c3_function == 'Power':
                imgout = np.zeros(imgin.shape, np.uint8)
                c3.Power(imgin,imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>Power</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # PieceWiseLinear
            elif c3_function == 'PieceWiseLinear':
                imgout = np.zeros(imgin.shape, np.uint8)
                c3.PiecewiseLinear(imgin,imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>PieceWiseLinear</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # Histogram
            elif c3_function == 'Histogram':
                imgout = np.zeros((imgin.shape[0], 256, 3), np.uint8) + 255
                c3.Histogram(imgin,imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>Histogram</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # HistogramEqualization            
            elif c3_function == 'HistogramEqualization':
                imgout = np.zeros(imgin.shape, np.uint8)
                cv2.equalizeHist(imgin, imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>HistogramEqualization</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # LocalHistogram
            elif c3_function == 'LocalHistogram':
                imgout = np.zeros(imgin.shape, np.uint8)
                c3.LocalHistogram(imgin, imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>LocalHistogram</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # HistogramStatistics
            elif c3_function == 'HistogramStatistics':
                imgout = np.zeros(imgin.shape, np.uint8)
                c3.HistogramStatistics(imgin, imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>HistogramStatistics</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # SmoothingGauss
            elif c3_function == 'SmoothingGauss':
                imgout = c3.SmoothingGauss(imgin)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>SmoothingGauss</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # Smoothing
            elif c3_function == 'Smoothing':
                imgout = c3.Smoothing(imgin)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>Smoothing</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # MedianFilter
            elif c3_function == 'MedianFilter':
                imgout = np.zeros(imgin.shape, np.uint8)
                c3.MedianFilter(imgin, imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>MedianFilter</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # Sharpen
            elif c3_function == 'Sharpen':
                imgout = c3.Sharpen(imgin)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>Sharpen</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # UnSharpMasking
            elif c3_function == 'UnSharpMasking':
                imgout = c3.UnSharpMasking(imgin)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>UnSharpMasking</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # Gradient
            elif c3_function == 'Gradient':
                imgout = c3.Gradient(imgin)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>Gradient</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            else:
                st.image('waiting.gif', caption='Wait for processing...')
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>None</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)

elif option == 'Chương 4':
    img_upload = st.file_uploader('Upload Image', type=['jpg', 'tif', 'bmp', 'gif', 'png'])
    if img_upload is not None:
        filepath = '..\ProjectCuoiKy\ProcessingImage\Chuong4\\' + img_upload.name
        imgin = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        imgin_header()
        st.image(imgin)

        c4_function = st.sidebar.selectbox('Please pick up a function', [
            '--Select function--','Spectrum', 'FrequencyFilter', 'DrawFilter', 'RemoveMoire'])
        # Spectrum
        if c4_function == 'Spectrum':
            imgout = c4.Spectrum(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>Spectrum</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # FrequencyFilter
        elif c4_function == 'FrequencyFilter':
            imgout = c4.FrequencyFilter(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>FrequencyFilter</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # DrawFilter
        elif c4_function == 'DrawFilter':
            imgout = c4.DrawFilter(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>DrawFilter</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # RemoveMoire
        elif c4_function == 'RemoveMoire':
            imgout = c4.RemoveMoire(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>RemoveMoire</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        else:
            st.image('waiting.gif', caption='Wait for processing...')
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>None</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)

elif option == 'Chương 9':
    img_upload = st.file_uploader('Upload Image', type=['jpg', 'tif', 'bmp', 'gif', 'png'])
    if img_upload is not None:
        filepath = '..\ProjectCuoiKy\ProcessingImage\Chuong9\\' + img_upload.name
        imgin = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        imgin_header()
        st.image(imgin)

        c9_function = st.sidebar.selectbox('Please pick up a function', [
            '--Select function--','Erosion', 'Dilation', 'OpeningClosing', 'Boundary', 'HoleFill', 
            'MyConnectedComponent', 'ConnectedComponent', 'CountRice'])
        # Erosion
        if c9_function == 'Erosion':
            imgout = np.zeros(imgin.shape, np.uint8)
            c9.Erosion(imgin, imgout)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>Erosion</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # Dilation
        elif c9_function == 'Dilation':
            imgout = np.zeros(imgin.shape, np.uint8)
            c9.Dilation(imgin, imgout)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>Dilation</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # OpeningClosing
        elif c9_function == 'OpeningClosing':
            imgout = np.zeros(imgin.shape, np.uint8)
            c9.OpeningClosing(imgin, imgout)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>OpeningClosing</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # Boundary
        elif c9_function == 'Boundary':
            imgout = c9.Boundary(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>Boundary</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # HoleFill
        elif c9_function == 'HoleFill':
            imgout = c9.HoleFill(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>HoleFill</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # MyConnectedComponent
        elif c9_function == 'MyConnectedComponent':
            imgout = c9.MyConnectedComponent(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>MyConnectedComponent</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # ConnectedComponent
        elif c9_function == 'ConnectedComponent':
            imgout = c9.ConnectedComponent(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>ConnectedComponent</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # CountRice
        elif c9_function == 'CountRice':
            imgout = c9.CountRice(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>CountRice</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        else:
            st.image('waiting.gif', caption='Wait for processing...')
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #000000; font-size: 16px; texxt-align: left;"><i>None</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
else:
    st.image('annoucement.png', use_column_width=True)



        