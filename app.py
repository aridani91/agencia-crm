import streamlit as st
import pandas as pd

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
    st.info("Este módulo está listo para recibir código. Aquí podrás ver el resumen global de tu agencia.")

def mostrar_crm():
    st.title("🎯 CRM & Prospección")
    st.info("Este módulo está listo para recibir código. Aquí irá la gestión de clientes.")

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
        
        html_factura = f"""
        <div style="background-color: white; padding: 40px; border-radius: 8px; color: #212529; box-shadow: 0 4px 6px rgba(0,0,0,0.1); font-family: Arial, sans-serif;">
            <h1 style="color: #333; margin-bottom: 5px; font-size: 28px;">MI AGENCIA DIGITAL</h1>
            <p style="color: #777; font-size: 12px; margin-top: 0; margin-bottom: 20px;">NIF: B99887766 | info@miagencia.com</p>
            <hr style="border: 0; border-top: 1px solid #eee; margin-bottom: 20px;">
            
            <p style="font-size: 14px; margin: 0 0 5px 0;"><strong>Factura Nº:</strong> {num_factura}</p>
            <p style="font-size: 14px; margin: 0 0 20px 0;"><strong>Fecha:</strong> 28/07/2026</p>
            
            <div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin-bottom: 30px; border: 1px solid #eee;">
                <p style="font-size: 14px; margin: 0 0 5px 0;"><strong>Cliente:</strong> {cliente}</p>
                <p style="font-size: 14px; margin: 0;"><strong>NIF/CIF:</strong> {nif}</p>
            </div>
            
            <table style="width: 100%; border-collapse: collapse; margin-bottom: 30px; font-size: 14px;">
                <thead>
                    <tr style="background-color: #f8f9fa; border-bottom: 2px solid #dee2e6;">
                        <th style="text-align: left; padding: 12px;">Concepto</th>
                        <th style="text-align: right; padding: 12px; width: 120px;">Importe</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="border-bottom: 1px solid #eee;">
                        <td style="padding: 12px;">{concepto}</td>
                        <td style="text-align: right; padding: 12px;">{base_imponible:.2f} €</td>
                    </tr>
                </tbody>
            </table>
            
            <div style="text-align: right; font-size: 14px;">
                <p style="margin: 5px 0;">Base Imponible: <strong style="display: inline-block; width: 100px;">{base_imponible:.2f} €</strong></p>
                <p style="margin: 5px 0;">IVA ({iva}%): <strong style="display: inline-block; width: 100px;">{cuota_iva:.2f} €</strong></p>
                <h2 style="margin-top: 15px; font-size: 24px;">Total: {total:.2f} €</h2>
            </div>
        </div>
        """
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
    
    # Preparamos los datos para el gráfico nativo de Streamlit
    df_grafica = df_finanzas.set_index("Mes")[["Ingresos (€)", "Gastos (€)"]]
    
    # Gráfico de barras nativo de Streamlit (Verde para Ingresos, Rojo para Gastos)
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
