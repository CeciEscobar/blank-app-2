import streamlit as st

st.title("Curriculum personal | Cecilia Escobar")

 #Título
st.title("Cecilia Escobar Briones")

# Sección de Información Personal
st.header("Información Personal")
st.write("""
**Nombre:** Tu Nombre Aquí  
**Correo Electrónico:** tu.email@ejemplo.com  
**Teléfono:** +123456789  
**Dirección:** Dirección completa
""")

# Sección de Perfil Profesional
st.header("Perfil Profesional")
st.write("""
Soy un [insertar tu profesión aquí], con [insertar años de experiencia] años de experiencia en [industria/sector]. 
Experto en [habilidades clave], con un fuerte enfoque en [intereses profesionales específicos]. 
Me apasiona [mencionar algún interés profesional] y siempre estoy buscando nuevas oportunidades para [logro o habilidad].
""")

# Sección de Experiencia Laboral
st.header("Experiencia Laboral")
st.subheader("Puesto Actual o Más Reciente")
st.write("""
**Empresa:** Nombre de la Empresa  
**Ubicación:** Ciudad, País  
**Fechas:** Mes/Año - Presente  
**Descripción:**  
- Describa sus responsabilidades y logros aquí.
- Añadir puntos adicionales según sea necesario.
""")

# Añadir más experiencias laborales si es necesario
st.subheader("Puesto Anterior")
st.write("""
**Empresa:** Nombre de la Empresa  
**Ubicación:** Ciudad, País  
**Fechas:** Mes/Año - Mes/Año  
**Descripción:**  
- Describa sus responsabilidades y logros aquí.
- Añadir puntos adicionales según sea necesario.
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
