from faker import Faker
import pandas as pd
import streamlit as st
from io import BytesIO

country = [
    ("Colombia", "es_CO" ),
    ("Chile", "es_CL" ),
    ("Argentina", "es_AR"),
    ("Estados Unidos", "en_US")

]

fake = Faker(country[0][1]) #Seleccionamos Colombia

available_fields= {
'Nombre': fake.name,
'Dirección': fake.address,
'Email': fake.email,
'Corres Electronico': fake.phone_number,
'Empresa': fake.company,
'Fecha': fake.date,
'Numero tarjeta credito': fake.credit_card_full,
'Fecha pasaporte': fake.passport_dob,
'Numero pasaporte': fake.passport_number
}

def generate_fake_data(fields, num_rows):
    data = {field: [func() for _ in range (num_rows)] for field, func in fields.items()}
    return pd.DataFrame(data)

st.title('Generador de Datos Falsos con Faker')
st.write('Selecciona los campos que quieras generar y la cantidad de datos.')

selected_fields = st.multiselect("Selecciona los campos", options=list(available_fields.keys()),
                               default=list(available_fields.keys()))
num_rows = st.number_input('Cantidad de registros a generar', min_value=1, max_value=100, value=10)

if st.button('Generar Datos'):
    selected_funcs = {field: available_fields[field] for field in selected_fields}
    df = generate_fake_data(selected_funcs, num_rows)

    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        writer.book.use_constant_memory=True #Se usa para reducir tamñaño de memoria
        df.to_excel(writer, index=False) #guardamos el archivo
    output.seek(0) #movemos el puntero al inicio del archivo
    st.success('Datos Generados')
    st.write(df)

    st.download_button( 
        label='Descargar Archivo Excel',
        data=output,
        file_name='Datos_generados.xlsx',
        mime='application/vnd.openxmformats-officedocument.spreadsheetml.sheet'
    )
