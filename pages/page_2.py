import streamlit as st
from PIL import Image

import pandas as pd


st.write("**HERE ADD ONE DESCRIPTION**")


if 'disable' not in st.session_state:
    st.session_state.disable = True
if 'collapse' not in st.session_state:
    st.session_state.collapse = 'visible'

def primer_requisito(**colums):
    colap = False
    nombres_columnas = [str(i) for i in colums.values()]
    values = {}
    print(nombres_columnas)
    if len(nombres_columnas) == 2:
        nombres_columnas = st.columns(len(nombres_columnas))
        with nombres_columnas[0]:
            st.text_input(label= 'add theme', value= '' , key= 'input_text_1',label_visibility= st.session_state.collapse)
            if st.session_state['input_text_1'] == "": 
                st.session_state.disable = True
            else:
                st.session_state.disable = False

        with nombres_columnas[1]:
            st.selectbox(label= 'add boolean', options=('NON','AND','OR'), key= 'select_box_1', disabled= st.session_state.disable , label_visibility= st.session_state.collapse)
            if st.session_state['select_box_1'] != 'NON':

                colap = True
        if colap:
            st.session_state.collapse = 'visible'
            primer_requisito(col1 = 'col1',col2 = 'col2', col3 = 'col3',col4='col4')           
    if len(nombres_columnas) == 4:
        colap = False
        nombres_columnas = st.columns(len(nombres_columnas)-2)
        with nombres_columnas[0]:
            st.text_input(label= 'add theme', value= '' , key= 'input_text_2', label_visibility= st.session_state.collapse)
            if st.session_state['input_text_2'] == "": 
                st.session_state.disable = True
            else:
                st.session_state.disable = False

        with nombres_columnas[1]:
            st.selectbox(label= 'add boolean', options=('NON','AND','OR'), key= 'select_text_2', disabled= st.session_state.disable, label_visibility= st.session_state.collapse )                
            if st.session_state['select_text_2'] != 'NON':
                colap = True    

        if colap:
            st.session_state.collapse = 'visible'
            primer_requisito(col1 = 'col1',col2 = 'col2', col3 = 'col3',col4='col4' , col5= 'col5', col6='col6')
            colap = False
    if len(nombres_columnas) == 6:
        colap = False
        nombres_columnas = st.columns(len(nombres_columnas)-5)
        with nombres_columnas[0]:
            st.text_input(label= 'add theme', value= '' , key= 'input_text_3' , label_visibility= st.session_state.collapse)
            if st.session_state['input_text_3'] == "": 
                st.session_state.disable = True
            else:
                st.session_state.disable = False
                st.session_state.collapse = 'visible'




        if colap:
            st.session_state.collapse = 'collapsed'
            primer_requisito(col1 = 'col1',col2 = 'col2', col3 = 'col3',col4='col4', )
            colap = False


    for key in st.session_state:
        values[str(key)] = st.session_state[str(key)]

    return values

 # solo hay que añadir dos columnas en dos columnas hacia abajo   
def segundo_requisito(diccionary):
    query = ''
    string_bol = ''
    string_str = ''

    if 'disable' in diccionary:
        diccionary.pop('disable')
        diccionary.pop('collapse')
    if 'button' in diccionary:
        diccionary.pop('button')

    for key , value in diccionary.items():

        if value == 'OR' or value == 'AND' or value == 'NON':
            if value == 'NON':
                string_bol = ''
            elif query != '' :
                string_bol = value
                query += "  {}  ".format(string_bol)
                string_bol = ''
            else:
                string_bol = value
        else:
            string_str = value
            query += "   {}  {}  ".format(string_str,string_bol)
            string_bol = ''
            
    return query   
def tercer_requisito(**kwargs):
    pass

var = primer_requisito(col1 = 'col1',col2 = 'col2')
col1,col2 = st.columns([0.2,0.8]) 

with col1:
    st.button(label= 'Click to send query', on_click= tercer_requisito, key= 'button', kwargs=var)
with col2:
    if st.session_state.button:
        st.write(segundo_requisito(var))
    else:
        st.write('Nothing')

image = Image.open('fish.jpg')
st.image(image, caption='Still alive')