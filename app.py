import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Agencia OS", page_icon="🚀", layout="wide")

# Estilo personalizado rápido
st.markdown("""
    <style>
    .main { padding: 1rem; }
    .stButton>button { width: 100%; border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

# Menú Lateral Principal
st.sidebar.title("🚀 Agencia OS")
menu = st.sidebar.radio(
    "Navegación", 
    ["📊 Dashboard 360°", "🎯 CRM & Prospección", "📄 Facturación PDF", "📋 Tareas & Proyectos", "💰 Finanzas"]
)

# --- MÓDULO 1: DASHBOARD ---
if menu == "📊 Dashboard 360°":
    st.title("📊 Visión General de la Agencia")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("MRR (Recurrente)", "1,200 €", "+15%")
    col2.metric("Clientes Activos", "4", "+1")
    col3.metric("Leads Calientes", "12", "3 pendientes hoy")
    col4.metric("Facturado este mes", "2,450 €", "Pendiente: 500 €")
    
    st.info("💡 **Acción recomendada hoy:** Tienes 3 leads en el CRM a los que no contactas desde hace 4 días.")

# --- MÓDULO 2: CRM & PROSPECCIÓN ---
elif menu == "🎯 CRM & Prospección":
    st.title("🎯 CRM de Ventas y Prospección")
    
    # Formulario rápido para añadir lead
    with st.expander("➕ Añadir Nuevo Lead"):
        c1, c2, c3 = st.columns(3)
        nombre = c1.text_input("Nombre / Negocio")
        telefono = c2.text_input("Teléfono (con prefijo 34)")
        servicio = c3.selectbox("Servicio de Interés", ["SEO Local", "Meta Ads", "Web / Funnel", "Pack Completo"])
        if st.button("Guardar Lead"):
            st.success(f"Lead {nombre} guardado correctamente.")

    st.subheader("Pipeline de Contactos")
    
    # Ejemplo de tabla dinámica de leads
    leads_demo = [
        {"Nombre": "Clínica Dental Murcia", "Teléfono": "34600112233", "Estado": "Llamada Hecha", "Valoración": "4.9 ⭐"},
        {"Nombre": "Gabinete Psicología Alicante", "Teléfono": "34699887766", "Estado": "Sin Contactar", "Valoración": "5.0 ⭐"}
    ]
    
    for l in leads_demo:
        with st.container():
            col_a, col_b, col_c, col_d = st.columns([3, 2, 2, 2])
            col_a.write(f"**{l['Nombre']}** ({l['Valoración']})")
            col_b.write(f"Estado: `{l['Estado']}`")
            
            # Enlace automático a WhatsApp
            msg = f"Hola, te escribo desde la agencia respecto a mejorar la captación de pacientes para {l['Nombre']}."
            wa_url = f"https://wa.me/{l['Teléfono']}?text={msg.replace(' ', '%20')}"
            col_c.markdown(f"[💬 Abrir WhatsApp]({wa_url})")
            
            if col_d.button("Editar", key=l['Nombre']):
                st.write("Editar ficha...")
        st.divider()

# --- MÓDULOS EN CONSTRUCCIÓN ---
else:
    st.title(f"Módulo: {menu}")
    st.warning("Este módulo está listo para recibir el código del siguiente paso.")
