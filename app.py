import streamlit as st
import pandas as pd
import textwrap

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Agencia OS",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# MÓDULOS DE LA APLICACIÓN (FUNCIONES)
# ==========================================

def mostrar_dashboard():
    st.title("📊 Dashboard 360°")
    st.markdown("Vista general del rendimiento global y estado de tu agencia.")
    
    # KPIs principales
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Facturación Anual", "41.800 €", "+18%")
    col2.metric("Clientes Activos", "18", "+3 este mes")
    col3.metric("Proyectos Activos", "12", "3 por entregar")
    col4.metric("Satisfacción Cliente", "98%", "+2%")
    
    st.divider()
    
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.subheader("📈 Rendimiento de Ingresos (2026)")
        datos_dashboard = {
            "Mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul"],
            "Ingresos (€)": [4200, 5100, 4800, 6200, 5900, 7100, 8500]
        }
        df_dash = pd.DataFrame(datos_dashboard).set_index("Mes")
        st.line_chart(df_dash)
        
    with col_right:
        st.subheader("🔔 Últimas Actividades")
        st.info("📌 **Factura FACT-2026-001** registrada para Clínica Dental Murcia.")
        st.success("✅ **Proyecto Web** completado para Tech Solutions.")
        st.warning("⏳ **Reunión de seguimiento** pendiente con Abogados Martínez.")
        st.info("📥 **Nuevo Lead:** Restaurante El Faro ha solicitado presupuesto.")


def mostrar_crm():
    st.title("🎯 CRM & Prospección")
    st.markdown("Gestión de contactos, embudo de ventas y seguimiento de oportunidades.")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Leads Nuevos", "14", "+4 esta semana")
    col2.metric("En Negociación", "6", "12.500 € en juego")
    col3.metric("Ratio de Cierre", "32%", "+5%")
    col4.metric("Valor Pipeline", "28.400 €", "8 propuestas")
    
    st.divider()
    
    st.subheader("Embudo de Ventas (Pipeline)")
    
    datos_crm = {
        "Cliente / Contacto": ["Gimnasio FitLife", "Hotel Costa Azul", "Clínica Estética Aura", "Moda Urbana", "Panadería Gourmet"],
        "Contacto Principal": ["Carlos Gómez", "Elena Soria", "Dr. Roberto Ruiz", "Marta Vidal", "Javier López"],
        "Fase de Venta": ["Propuesta Enviada", "Contacto Inicial", "Negociación", "Cierre Ganado", "Propuesta Enviada"],
        "Valor Estimado": ["2.500 €", "1.200 €", "4.800 €", "3.000 €", "1.500 €"],
        "Prioridad": ["Alta 🔴", "Media 🟡", "Alta 🔴", "Baja 🟢", "Media 🟡"]
    }
    df_crm = pd.DataFrame(datos_crm)
    st.dataframe(df_crm, use_container_width=True, hide_index=True)
    
    st.subheader("➕ Registrar Nuevo Lead")
    with st.form("nuevo_lead_form"):
        c1, c2 = st.columns(2)
        nombre_empresa = c1.text_input("Nombre de la Empresa / Cliente")
        persona_contacto = c2.text_input("Persona de Contacto")
        
        c3, c4, c5 = st.columns(3)
        email_lead = c3.text_input("Correo Electrónico")
        fase = c4.selectbox("Fase Inicial", ["Contacto Inicial", "Reunión Agendada", "Propuesta Enviada", "Negociación"])
        valor = c5.number_input("Valor Estimado (€)", value=1000.0, step=100.0)
        
        submitted = st.form_submit_button("Añadir al CRM")
        if submitted and nombre_empresa:
            st.success(f"¡Lead '{nombre_empresa}' añadido correctamente al CRM!")


def mostrar_facturacion():
    st.title("📄 Generador de Facturas Oficiales")
    
    col1, col2 = st.columns([1, 1.2], gap="large")
    
    with col1:
        st.subheader("📝 Datos de la Factura")
        num_factura = st.text_input("Número de Factura", "FACT-2026-001")
        cliente = st.text_input("Nombre / Razón Social del Cliente", "Clínica Dental Murcia S.L.")
        nif = st.text_input("NIF / CIF Cliente", "B12345678")
        concepto = st.text_area("Concepto / Servicio", "Servicio de Posicionamiento SEO y Gestión de Campañas")
        
        c1, c2 = st.columns(2)
        base_imponible = c1.number_input("Base Imponible (€)", value=500.00, step=10.0, format="%.2f")
        iva = c2.selectbox("IVA (%)", [21, 10, 4, 0], index=0)
        
        cuota_iva = base_imponible * (iva / 100)
        total = base_imponible + cuota_iva
        
        st.markdown(f"**Total Factura:** <span style='color:#2ecc71; font-size:18px;'>{total:.2f} €</span> (IVA incluido)", unsafe_allow_html=True)
        
        if st.button("💾 Registrar Factura"):
            st.success("¡Factura registrada en el sistema!")

    with col2:
        st.subheader("👁️ Vista Previa de la Factura")
        
        # Uso de textwrap.dedent para corregir la renderización de HTML
        html_factura = textwrap.dedent(f"""
        <div style="background-color: white; padding: 30px; border-radius: 8px; color: #212529; box-shadow: 0 4px 6px rgba(0,0,0,0.1); font-family: Arial, sans-serif;">
            <h1 style="color: #333; margin-bottom: 5px; font-size: 26px; font-weight: bold;">MI AGENCIA DIGITAL</h1>
            <p style="color: #777; font-size: 12px; margin-top: 0; margin-bottom: 20px;">NIF: B99887766 | info@miagencia.com</p>
            <hr style="border: 0; border-top: 1px solid #eee; margin-bottom: 20px;">
            
            <p style="font-size: 14px; margin: 0 0 5px 0;"><strong>Factura Nº:</strong> {num_factura}</p>
            <p style="font-size: 14px; margin: 0 0 20px 0;"><strong>Fecha:</strong> 28/07/2026</p>
            
            <div style="background-color: #f8f9fa; padding: 12px; border-radius: 5px; margin-bottom: 20px; border: 1px solid #eee;">
                <p style="font-size: 14px; margin: 0 0 5px 0;"><strong>Cliente:</strong> {cliente}</p>
                <p style="font-size: 14px; margin: 0;"><strong>NIF/CIF:</strong> {nif}</p>
            </div>
            
            <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px; font-size: 14px;">
                <thead>
                    <tr style="background-color: #f8f9fa; border-bottom: 2px solid #dee2e6;">
                        <th style="text-align: left; padding: 10px;">Concepto</th>
                        <th style="text-align: right; padding: 10px; width: 100px;">Importe</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="border-bottom: 1px solid #eee;">
                        <td style="padding: 10px;">{concepto}</td>
                        <td style="text-align: right; padding: 10px;">{base_imponible:.2f} €</td>
                    </tr>
                </tbody>
            </table>
            
            <div style="text-align: right; font-size: 14px;">
                <p style="margin: 5px 0;">Base Imponible: <strong>{base_imponible:.2f} €</strong></p>
                <p style="margin: 5px 0;">IVA ({iva}%): <strong>{cuota_iva:.2f} €</strong></p>
                <h2 style="margin-top: 10px; font-size: 22px; color: #111;">Total: {total:.2f} €</h2>
            </div>
        </div>
        """)
        st.markdown(html_factura, unsafe_allow_html=True)
        st.caption("💡 Para guardar en PDF: Pulsa Ctrl + P (o Cmd + P en Mac) y elige 'Guardar como PDF'.")


def mostrar_tareas_proyectos():
    st.title("📋 Tareas & Proyectos")
    st.markdown("Gestiona el estado de los proyectos de tu agencia y las tareas pendientes.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Proyectos Activos", "12", "+2 este mes")
    col2.metric("Tareas Pendientes", "28", "-5 desde ayer")
    col3.metric("Entregas esta semana", "3", delta_color="off")
    
    st.divider()
    
    st.subheader("Proyectos en Curso")
    
    datos_proyectos = {
        "Proyecto": ["Diseño Web Corporativa", "Campaña SEO Local", "Gestión RRSS Agosto", "Migración E-commerce", "Auditoría Técnica"],
        "Cliente": ["Clínica Dental Murcia S.L.", "Abogados Martínez", "Restaurante El Faro", "Zapatos Online", "Tech Solutions"],
        "Estado": ["En Progreso", "Pendiente", "En Progreso", "Revisión", "Pendiente"],
        "Prioridad": ["Alta 🔴", "Media 🟡", "Baja 🟢", "Alta 🔴", "Media 🟡"],
        "Fecha Límite": ["2026-08-15", "2026-08-05", "2026-08-31", "2026-08-10", "2026-09-01"]
    }
    
    df_proyectos = pd.DataFrame(datos_proyectos)
    st.dataframe(df_proyectos, use_container_width=True, hide_index=True)
    
    st.subheader("Tus Tareas para Hoy")
    st.checkbox("Llamar al cliente 'Clínica Dental' para revisar facturación")
    st.checkbox("Enviar reporte de métricas de Julio a 'Abogados Martínez'")
    st.checkbox("Revisar textos de la nueva web de 'Tech Solutions'")


def mostrar_finanzas():
    st.title("💰 Panel Financiero")
    st.markdown("Resumen de ingresos, gastos y rentabilidad de la agencia.")
    
    datos_finanzas = {
        "Mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio"],
        "Ingresos (€)": [4200, 5100, 4800, 6200, 5900, 7100, 8500],
        "Gastos (€)": [2100, 2300, 2400, 2900, 2700, 3100, 3500]
    }
    
    df_finanzas = pd.DataFrame(datos_finanzas)
    df_finanzas["Beneficio Neto (€)"] = df_finanzas["Ingresos (€)"] - df_finanzas["Gastos (€)"]
    
    ingresos_actuales = df_finanzas["Ingresos (€)"].iloc[-1]
    gastos_actuales = df_finanzas["Gastos (€)"].iloc[-1]
    beneficio_actual = df_finanzas["Beneficio Neto (€)"].iloc[-1]
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Ingresos (Julio)", f"{ingresos_actuales:,.2f} €", "+19.7% vs Junio")
    col2.metric("Gastos (Julio)", f"{gastos_actuales:,.2f} €", "+12.9% vs Junio", delta_color="inverse")
    col3.metric("Beneficio Neto", f"{beneficio_actual:,.2f} €", "+25.0% vs Junio")
    
    st.divider()
    
    st.subheader("Evolución Anual (2026)")
    
    df_grafica = df_finanzas.set_index("Mes")[["Ingresos (€)", "Gastos (€)"]]
    st.bar_chart(df_grafica, color=["#2ecc71", "#e74c3c"])
    
    with st.expander("Ver desglose mensual detallado"):
        st.dataframe(df_finanzas, use_container_width=True, hide_index=True)


# ==========================================
# MENÚ LATERAL (SIDEBAR)
# ==========================================
with st.sidebar:
    st.markdown("### 🚀 Agencia OS")
    st.markdown("**Navegación**")
    
    opcion = st.radio(
        "Selecciona un módulo:",
        ["Dashboard 360°", "CRM & Prospección", "Facturación PDF", "Tareas & Proyectos", "Finanzas"],
        label_visibility="collapsed"
    )

# ==========================================
# LÓGICA DE NAVEGACIÓN
# ==========================================
if opcion == "Dashboard 360°":
    mostrar_dashboard()
elif opcion == "CRM & Prospección":
    mostrar_crm()
elif opcion == "Facturación PDF":
    mostrar_facturacion()
elif opcion == "Tareas & Proyectos":
    mostrar_tareas_proyectos()
elif opcion == "Finanzas":
    mostrar_finanzas()
