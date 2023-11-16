import streamlit as st
from PIL import Image
# Initialize connection.
conn = st.connection('mysql', type='sql')
# Perform query.
df = conn.query('SELECT * FROM clientes.datos_user;', ttl=600)
# Print results.
st.dataframe(df)

# CONECCIÒN:
# DATABASE: SEMILLERO_DB 
# TABLE: USUARIOS (CORREO_ELECTRÓNICO, CONTRASEÑA, USUARIO, SUSCRIBCIÓN)


with st.form("my_form"):
   st.write("")
   col1 ,  col2 = st.columns(2)
   with col1:
    my_number = st.text_input('Usuario')
    my_color = st.text_input('Contraseña')
    st.form_submit_button('ingresar')
    with col2:
        image = Image.open('fish.jpg')
        st.image(image, caption='Still alive')