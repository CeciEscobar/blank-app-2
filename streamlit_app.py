import streamlit as st

#Titulo
st.title("Cecilia Escobar Briones")

st.header("Estudiante Administración y Finanzas")

### FOTO PERFIL

import requests
import streamlit as st

# iamge ID
file_id = "1dSRPt8BOQXvwE0jpULs0jyRKCewf24sV"

# URL
url = f"https://drive.google.com/uc?export=view&id={file_id}"

response = requests.get(url)
st.image(response.content)

### SECCION INFORMACIÓN

# Sección de Información Personal
st.header("Información Personal")
st.write("""
**Nombre:** Cecilia Escobar  
**Correo Electrónico:** cecilia.escobarb01@gmail.com  
**Teléfono:** 4442361322   
**Dirección:** Av. de la estrella 677, 45019. Solares, Zapopan  
**Linkedin:** www.linkedin.com/in/cecilia-escobar-briones-074a00318 
""")


# Sección de Perfil Profesional
st.header("Perfil Profesional")
st.write("""
Estudiante universitaria de Administración y Finanzas en séptimo semestre con
experiencia en el área de administración y servicio al cliente. Estoy comprometida con
mi crecimiento personal y busco poder aplicar lo aprendido en la universidad en un
entorno profesional y dinámico donde pueda contribuir al exito de su empresa.
""")

# Sección de Experiencia Laboral
st.header("Experiencia Laboral")
st.subheader("Becaria Área de Credencialización")
st.write("""
**Empresa:** Universidad Panamericana  
**Ubicación:** Guadalajara, Jalisco  
**Fechas:** Dic/2022 - Presente    
**Descripción:**  
- Atención al cliente 
- Gestión de datos 
- Administración de inventario 
- Creación y distribución de credenciales 
""")

# Sección de Educación
st.header("Experiencia Académica")
st.write("""
**Título:** Licenciatura en Administración y Finanzas  
**Institución:** Universidad Panamericana  
**Fechas:** Ago/2021 - Actualidad    

**Título:** Mejores promedios  
**Institución:** Universidad Panamericana  
**Fechas:** Ago/2021 - Actualidad   

**Título:** Preparatoria Tec de Monterrey  
**Institución:** Tec de Monterrey, San Luis Potosí  
**Fechas:** 2017-2020  

**Título:** Representativo Voleibol  
**Institución:** Tec de Monterrey, San Luis Potosí  
**Fechas:** 2017-2019  
""")

# Sección de Habilidades
st.header("Habilidades")
st.write("""
- Comunicación efectiva
- Trabajo en equipo
- Gestión de tiempo
- Pensamiento critico
- Creatividad
- Disiplina
""")

# Sección de Idiomas
st.header("Idiomas")
st.write("""
- Español (Nativo)
- Ingles (Avanzado, C1)
""")

# Sección de Programas que domino)
st.header("Programas que domino")
st.write("""
- Word
- Power Point
- Excel
- Canva
- Google Drive (Docs, Sheets, Calendar, etc)
- SAP
""")


# Pie de página
st.write("---")
st.write("Esta aplicación fue creada con Streamlit.")





