import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Agencia OS", page_icon="🚀", layout="wide")

# Estilo personalizado
st.markdown("""
    <style>
    .main { padding: 1.5rem; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; }
    .invoice-box {
        background-color: #ffffff;
        color: #111111;
        padding: 25px;
        border-radius: 10px;
        border: 1px solid #dddddd;
        font-family: Arial, sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# Inicializar memoria interna de la app
if 'leads' not in st.session_state:
    st.session_state.leads = [
        {"Nombre": "Clínica Dental Murcia", "Teléfono": "34600112233", "Estado": "Llamada Hecha", "Valoración": "4.9 ⭐", "Servicio": "SEO Local"},
        {"Nombre": "Gabinete Psicología Alicante", "Teléfono": "34699887766", "Estado": "Sin Contactar", "Valoración": "5.0 ⭐", "Servicio": "Meta Ads"}
    ]

if 'facturas' not in st.session_state:
    st.session_state.facturas = []

# Menú Lateral Principal
st.sidebar.title("🚀 Agencia OS")
menu = st.sidebar.radio(
    "Navegación", 
    ["📊 Dashboard 360°", "🎯 CRM & Prospección", "📄 Facturación PDF", "📋 Tareas & Proyectos", "💰 Finanzas"]
)

# --- MÓDULO 1: DASHBOARD ---
if menu == "📊 Dashboard 360°":
    st.title("📊 Visión General de la Agencia")
    
    total_leads = len(st.session_state.leads)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("MRR (Recurrente)", "1,200 €", "+15%")
    col2.metric("Clientes Activos", "4", "+1")
    col3.metric("Leads Registrados", f"{total_leads}", "En pipeline")
    col4.metric("Facturas Creadas", f"{len(st.session_state.facturas)}", "Este mes")
    
    st.info("💡 **Acción recomendada hoy:** Tienes leads pendientes en el CRM. Abre el módulo de Prospección para enviarles WhatsApp.")

# --- MÓDULO 2: CRM & PROSPECCIÓN ---
elif menu == "🎯 CRM & Prospección":
    st.title("🎯 CRM de Ventas y Prospección")
    
    with st.expander("➕ Añadir Nuevo Lead"):
        with st.form("form_lead", clear_on_submit=True):
            c1, c2, c3 = st.columns(3)
            nombre = c1.text_input("Nombre / Negocio")
            telefono = c2.text_input("Teléfono (con prefijo 34)")
            servicio = c3.selectbox("Servicio de Interés", ["SEO Local", "Meta Ads", "Web / Funnel", "Pack Completo"])
            submit = st.form_submit_button("Guardar Lead")
            if submit and nombre and telefono:
                st.session_state.leads.append({
                    "Nombre": nombre,
                    "Teléfono": telefono,
                    "Estado": "Sin Contactar",
                    "Valoración": "Nuevo ⭐",
                    "Servicio": servicio
                })
                st.success(f"Lead '{nombre}' guardado con éxito.")
                st.rerun()

    st.subheader("Pipeline de Contactos")
    
    for idx, l in enumerate(st.session_state.leads):
        with st.container():
            col_a, col_b, col_c, col_d = st.columns([3, 2, 2, 2])
            col_a.write(f"**{l['Nombre']}** ({l['Valoración']}) — *{l.get('Servicio', 'Gral')}*")
            col_b.write(f"Estado: `{l['Estado']}`")
            
            msg = f"Hola, te escribo desde la agencia respecto a mejorar la captación de clientes para {l['Nombre']}."
            wa_url = f"https://wa.me/{l['Teléfono']}?text={msg.replace(' ', '%20')}"
            col_c.markdown(f"[💬 Abrir WhatsApp]({wa_url})")
            
            if col_d.button("Eliminar", key=f"del_{idx}"):
                st.session_state.leads.pop(idx)
                st.rerun()
        st.divider()

# --- MÓDULO 3: FACTURACIÓN PDF ---
elif menu == "📄 Facturación PDF":
    st.title("📄 Generador de Facturas Oficiales")
    
    col_form, col_preview = st.columns([1, 1])
    
    with col_form:
        st.subheader("📝 Datos de la Factura")
        num_factura = st.text_input("Número de Factura", f"FACT-2026-{len(st.session_state.facturas)+1:03d}")
        cliente_nombre = st.text_input("Nombre / Razón Social del Cliente", "Clínica Dental Murcia S.L.")
        cliente_cif = st.text_input("NIF / CIF Cliente", "B12345678")
        concepto = st.text_area("Concepto / Servicio", "Servicio de Posicionamiento SEO y Gestión de Campañas")
        
        c_base, c_iva = st.columns(2)
        base_imponible = c_base.number_input("Base Imponible (€)", min_value=0.0, value=500.0, step=50.0)
        tipo_iva = c_iva.selectbox("IVA (%)", [21, 10, 4, 0], index=0)
        
        cuota_iva = base_imponible * (tipo_iva / 100.0)
        total_factura = base_imponible + cuota_iva
        
        st.markdown(f"**Total Factura:** `{total_factura:.2f} €` (IVA incluido)")
        
        if st.button("💾 Registrar Factura"):
            st.session_state.facturas.append({
                "Número": num_factura,
                "Cliente": cliente_nombre,
                "Base": base_imponible,
                "Total": total_factura,
                "Fecha": datetime.now().strftime("%Y-%m-%d")
            })
            st.success("Factura registrada en el sistema.")
    
    with col_preview:
        st.subheader("👁️ Vista Previa de la Factura")
        
        html_factura = f"""
        <div class="invoice-box">
            <h2 style="color: #2b2b2b; margin-bottom: 5px;">MI AGENCIA DIGITAL</h2>
            <p style="color: #666; font-size: 12px; margin-top: 0;">NIF: B99887766 | info@miagencia.com</p>
            <hr style="border: 0.5px solid #eee;">
            <p><strong>Factura Nº:</strong> {num_factura}<br>
            <strong>Fecha:</strong> {datetime.now().strftime('%d/%m/%Y')}</p>
            
            <div style="background-color: #f9f9f9; padding: 10px; border-radius: 5px; margin: 15px 0;">
                <strong>Cliente:</strong> {cliente_nombre}<br>
                <strong>NIF/CIF:</strong> {cliente_cif}
            </div>
            
            <table style="width:100%; border-collapse: collapse; margin-top: 15px;">
                <tr style="background-color: #f2f2f2;">
                    <th style="text-align:left; padding:8px;">Concepto</th>
                    <th style="text-align:right; padding:8px;">Importe</th>
                </tr>
                <tr>
                    <td style="padding:8px; border-bottom:1px solid #eee;">{concepto}</td>
                    <td style="text-align:right; padding:8px; border-bottom:1px solid #eee;">{base_imponible:.2f} €</td>
                </tr>
            </table>
            
            <div style="text-align: right; margin-top: 20px;">
                <p style="margin:2px;">Base Imponible: <strong>{base_imponible:.2f} €</strong></p>
                <p style="margin:2px;">IVA ({tipo_iva}%): <strong>{cuota_iva:.2f} €</strong></p>
                <h3 style="color: #111; margin-top: 5px;">Total: {total_factura:.2f} €</h3>
            </div>
        </div>
        """
        
        st.markdown(html_factura, unsafe_allow_html=True)
        st.caption("💡 Para guardar en PDF: Pulsa Ctrl + P (o Cmd + P en Mac) y elige 'Guardar como PDF'.")

# --- MÓDULOS EN CONSTRUCCIÓN ---
else:
    st.title(f"Módulo: {menu}")
    st.warning("Este módulo está listo para recibir el código del siguiente paso.")
