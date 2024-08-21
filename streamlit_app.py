import streamlit as st

#Titulo
st.title("Curriculum personal | Cecilia Escobar Briones")

st.header("Estudiante Administración y Finanzas")

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
st.header("Educación")
st.write("""
**Título:** Grado Obtenido  
**Institución:** Nombre de la Universidad  
**Fechas:** Mes/Año - Mes/Año  
**Descripción:** Breve descripción de tus estudios, si es relevante.
""")

# Sección de Habilidades
st.header("Habilidades")
st.write("""
- Habilidad 1
- Habilidad 2
- Habilidad 3
- Habilidad 4
""")

# Sección de Idiomas
st.header("Idiomas")
st.write("""
- Idioma 1 (Nivel)
- Idioma 2 (Nivel)
""")

# Sección de Proyectos o Publicaciones (Opcional)
st.header("Proyectos o Publicaciones")
st.write("""
**Título del Proyecto o Publicación**  
Breve descripción del proyecto o publicación. Incluir enlace si es relevante.
""")

# Sección de Referencias (Opcional)
st.header("Referencias")
st.write("Disponibles a solicitud.")

# Pie de página
st.write("---")
st.write("Esta aplicación fue creada con Streamlit.")
