import streamlit as st

# Initialize connection.
conn = st.connection('mysql', type='sql')
# Perform query.
df = conn.query('SELECT * FROM clientes.datos_user;', ttl=600)
# Print results.
st.dataframe(df)