import streamlit as st
import pandas as pd
from datetime import date

# ==========================================
# CONFIGURACIÓN DE PÁGINA Y ESTILOS CSS
# ==========================================
st.set_page_config(
    page_title="Agencia OS",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos visuales para mejorar tipografía, tarjetas y botones
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Tarjetas de métricas estilizadas */
    div[data-testid="stMetric"] {
        background: #1e222d;
        border: 1px solid #2e3444;
        padding: 18px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }
    
    /* Botones primarios */
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        transition: all 0.2s ease-in-out;
    }
    
    .stButton>button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.35);
    }
</style>
""", unsafe_allow_html=True)

# Función para limpiar HTML y evitar errores de renderizado en Streamlit
def render_html_clean(html_text):
    clean_text = "\n".join([line.strip() for line in html_text.split("\n")])
    st.markdown(clean_text, unsafe_allow_html=True)

# ==========================================
# INICIALIZACIÓN DEL ESTADO (PERSISTENCIA)
# ==========================================
if "leads" not in st.session_state:
    st.session_state.leads = pd.DataFrame([
        {"Cliente": "Gimnasio FitLife", "Contacto": "Carlos Gómez", "Fase": "Propuesta Enviada", "Valor (€)": 2500.0, "Prioridad": "Alta 🔴"},
        {"Cliente": "Hotel Costa Azul", "Contacto": "Elena Soria", "Fase": "Contacto Inicial", "Valor (€)": 1200.0, "Prioridad": "Media 🟡"},
        {"Cliente": "Clínica Estética Aura", "Contacto": "Dr. Roberto Ruiz", "Fase": "Negociación", "Valor (€)": 4800.0, "Prioridad": "Alta 🔴"},
        {"Cliente": "Moda Urbana", "Contacto": "Marta Vidal", "Fase": "Cierre Ganado", "Valor (€)": 3000.0, "Prioridad": "Baja 🟢"},
        {"Cliente": "Panadería Gourmet", "Contacto": "Javier López", "Fase": "Propuesta Enviada", "Valor (€)": 1500.0, "Prioridad": "Media 🟡"}
    ])

if "facturas" not in st.session_state:
    st.session_state.facturas = pd.DataFrame([
        {"Número": "FACT-2026-001", "Cliente": "Clínica Dental Murcia S.L.", "Fecha": "2026-07-28", "Base (€)": 500.0, "IVA (%)": 21, "Total (€)": 605.0}
    ])

if "gastos" not in st.session_state:
    st.session_state.gastos = pd.DataFrame([
        {"Concepto": "Herramientas Software", "Categoría": "Suscripciones", "Importe (€)": 450.0, "Fecha": "2026-07-05"},
        {"Concepto": "Servidores & Hosting", "Categoría": "Infraestructura", "Importe (€)": 250.0, "Fecha": "2026-07-12"},
        {"Concepto": "Campañas Meta Ads", "Categoría": "Marketing", "Importe (€)": 800.0, "Fecha": "2026-07-20"}
    ])

# ==========================================
# MÓDULOS DE LA APLICACIÓN
# ==========================================

def mostrar_dashboard():
    st.title("📊 Dashboard 360°")
    st.markdown("Resumen global del estado y métricas en tiempo real de tu agencia.")
    
    total_ingresos = st.session_state.facturas["Total (€)"].sum()
    total_leads = len(st.session_state.leads)
    leads_ganados = len(st.session_state.leads[st.session_state.leads["Fase"] == "Cierre Ganado"])
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Facturación Total", f"{total_ingresos:,.2f} €")
    col2.metric("Prospectos Activos", f"{total_leads}")
    col3.metric("Clientes Ganados", f"{leads_ganados}")
    col4.metric("Tasa de Conversión", f"{(leads_ganados/total_leads*100) if total_leads > 0 else 0:.1f}%")
    
    st.divider()
    
    col_l, col_r = st.columns([2, 1])
    with col_l:
        st.subheader("📈 Registro de Facturas Recientes")
        st.dataframe(st.session_state.facturas, use_container_width=True, hide_index=True)
    
    with col_r:
        st.subheader("🔔 Estado del Pipeline")
        st.write("Suma total de oportunidades:")
        valor_pipeline = st.session_state.leads["Valor (€)"].sum()
        st.info(f"💰 **Valor Total en Pipeline:** {valor_pipeline:,.2f} €")


def mostrar_crm():
    st.title("🎯 CRM & Prospección")
    st.markdown("Gestión interactiva de clientes. **Puedes editar las celdas o añadir/borrar filas directamente.**")
    
    total_pipeline = st.session_state.leads["Valor (€)"].sum() if not st.session_state.leads.empty else 0
    leads_count = len(st.session_state.leads)
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Prospects", f"{leads_count}")
    c2.metric("Valor del Pipeline", f"{total_pipeline:,.2f} €")
    c3.metric("Promedio / Lead", f"{(total_pipeline/leads_count) if leads_count > 0 else 0:,.2f} €")
    
    st.divider()
    
    st.subheader("📋 Embudo de Ventas (Pipeline)")
    st.caption("💡 Haz doble clic en cualquier celda para modificarla, o selecciona filas y pulsa 'Supr' / 'Delete' para eliminar.")
    
    # Editor de datos dinámico: Permite editar, agregar y borrar filas interactivamente
    edited_leads = st.data_editor(
        st.session_state.leads,
        num_rows="dynamic",
        use_container_width=True,
        key="editor_leads"
    )
    
    # Guardamos los cambios hechos directamente en la tabla
    st.session_state.leads = edited_leads
    
    st.divider()
    
    # Formulario rápido para añadir nuevos prospectos
    with st.expander("➕ Añadir Nuevo Lead mediante Formulario"):
        with st.form("form_nuevo_lead", clear_on_submit=True):
            col_a, col_b = st.columns(2)
            cliente = col_a.text_input("Nombre de la Empresa / Cliente")
            contacto = col_b.text_input("Persona de Contacto")
            
            col_c, col_d, col_e = st.columns(3)
            fase = col_c.selectbox("Fase Inicial", ["Contacto Inicial", "Propuesta Enviada", "Negociación", "Cierre Ganado"])
            valor = col_d.number_input("Valor Estimado (€)", value=1000.0, step=100.0)
            prioridad = col_e.selectbox("Prioridad", ["Alta 🔴", "Media 🟡", "Baja 🟢"])
            
            if st.form_submit_button("Guardar Lead"):
                if cliente:
                    nuevo_registro = pd.DataFrame([{
                        "Cliente": cliente,
                        "Contacto": contacto,
                        "Fase": fase,
                        "Valor (€)": valor,
                        "Prioridad": prioridad
                    }])
                    st.session_state.leads = pd.concat([st.session_state.leads, nuevo_registro], ignore_index=True)
                    st.success(f"¡Lead '{cliente}' registrado correctamente!")
                    st.rerun()


def mostrar_facturacion():
    st.title("📄 Generador de Facturas Oficiales")
    
    col1, col2 = st.columns([1, 1.2], gap="large")
    
    with col1:
        st.subheader("📝 Datos de la Factura")
        num_factura = st.text_input("Número de Factura", "FACT-2026-002")
        cliente = st.text_input("Nombre / Razón Social del Cliente", "Clínica Dental Murcia S.L.")
        nif = st.text_input("NIF / CIF Cliente", "B12345678")
        concepto = st.text_area("Concepto / Servicio", "Servicio de Posicionamiento SEO y Gestión de Campañas")
        
        c1, c2 = st.columns(2)
        base_imponible = c1.number_input("Base Imponible (€)", value=500.00, step=10.0, format="%.2f")
        iva = c2.selectbox("IVA (%)", [21, 10, 4, 0], index=0)
        
        cuota_iva = base_imponible * (iva / 100)
        total = base_imponible + cuota_iva
        
        st.markdown(f"**Total Factura:** <span style='color:#2ecc71; font-size:18px;'>{total:.2f} €</span>", unsafe_allow_html=True)
        
        if st.button("💾 Registrar y Guardar Factura"):
            nueva_factura = pd.DataFrame([{
                "Número": num_factura,
                "Cliente": cliente,
                "Fecha": str(date.today()),
                "Base (€)": base_imponible,
                "IVA (%)": iva,
                "Total (€)": total
            }])
            st.session_state.facturas = pd.concat([st.session_state.facturas, nueva_factura], ignore_index=True)
            st.success(f"Factura {num_factura} registrada. ¡Impactará en tus Finanzas!")

    with col2:
        st.subheader("👁️ Vista Previa de la Factura")
        
        # Plantilla HTML limpia sin problemas de indentación
        html_factura = f"""
        <div style="background-color: #ffffff; padding: 30px; border-radius: 8px; color: #111111; box-shadow: 0 4px 12px rgba(0,0,0,0.2); font-family: Arial, sans-serif;">
            <h2 style="color: #111; margin: 0 0 5px 0; font-size: 24px;">MI AGENCIA DIGITAL</h2>
            <p style="color: #666; font-size: 12px; margin: 0 0 20px 0;">NIF: B99887766 | info@miagencia.com</p>
            <hr style="border: 0; border-top: 1px solid #ddd; margin-bottom: 20px;">
            <p style="font-size: 13px; margin: 3px 0;"><strong>Factura Nº:</strong> {num_factura}</p>
            <p style="font-size: 13px; margin: 3px 0 15px 0;"><strong>Fecha:</strong> {date.today()}</p>
            <div style="background-color: #f8f9fa; padding: 12px; border-radius: 6px; margin-bottom: 20px; border: 1px solid #e9ecef;">
                <p style="font-size: 13px; margin: 2px 0;"><strong>Cliente:</strong> {cliente}</p>
                <p style="font-size: 13px; margin: 2px 0;"><strong>NIF/CIF:</strong> {nif}</p>
            </div>
            <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px; font-size: 13px;">
                <thead>
                    <tr style="background-color: #f1f3f5; border-bottom: 2px solid #dee2e6;">
                        <th style="text-align: left; padding: 8px;">Concepto</th>
                        <th style="text-align: right; padding: 8px;">Importe</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="border-bottom: 1px solid #eee;">
                        <td style="padding: 8px;">{concepto}</td>
                        <td style="text-align: right; padding: 8px;">{base_imponible:.2f} €</td>
                    </tr>
                </tbody>
            </table>
            <div style="text-align: right; font-size: 13px;">
                <p style="margin: 4px 0;">Base Imponible: <strong>{base_imponible:.2f} €</strong></p>
                <p style="margin: 4px 0;">IVA ({iva}%): <strong>{cuota_iva:.2f} €</strong></p>
                <h3 style="margin-top: 10px; font-size: 20px; color: #000;">Total: {total:.2f} €</h3>
            </div>
        </div>
        """
        render_html_clean(html_factura)
        st.caption("💡 Para guardar en PDF: Pulsa Ctrl + P (o Cmd + P en Mac) y elige 'Guardar como PDF'.")


def mostrar_tareas_proyectos():
    st.title("📋 Tareas & Proyectos")
    st.markdown("Control de estados y entregables operativos.")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Proyectos Activos", "5")
    c2.metric("Pendientes", "2")
    c3.metric("Entregas esta semana", "1")
    
    st.divider()
    
    st.subheader("Lista de Proyectos")
    proyectos_df = pd.DataFrame([
        {"Proyecto": "Diseño Web Corporativa", "Cliente": "Clínica Dental Murcia", "Estado": "En Progreso", "Prioridad": "Alta 🔴"},
        {"Proyecto": "Campaña SEO Local", "Cliente": "Abogados Martínez", "Estado": "Pendiente", "Prioridad": "Media 🟡"},
        {"Proyecto": "Auditoría Técnica", "Cliente": "Tech Solutions", "Estado": "En Revisión", "Prioridad": "Alta 🔴"}
    ])
    st.dataframe(proyectos_df, use_container_width=True, hide_index=True)


def mostrar_finanzas():
    st.title("💰 Panel Financiero Dinámico")
    st.markdown("Los datos de ingresos se calculan **automáticamente** a partir de las facturas que registras.")
    
    # Cálculo dinámico basado en las facturas y gastos registrados
    total_ingresos = st.session_state.facturas["Total (€)"].sum()
    total_gastos = st.session_state.gastos["Importe (€)"].sum()
    beneficio_neto = total_ingresos - total_gastos
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Ingresos Totales (Facturados)", f"{total_ingresos:,.2f} €")
    col2.metric("Gastos Totales", f"{total_gastos:,.2f} €", delta_color="inverse")
    col3.metric("Beneficio Neto", f"{beneficio_neto:,.2f} €")
    
    st.divider()
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.subheader("📥 Desglose de Ingresos (Facturas)")
        st.dataframe(st.session_state.facturas[["Número", "Cliente", "Total (€)", "Fecha"]], use_container_width=True, hide_index=True)
        
    with col_b:
        st.subheader("📤 Desglose de Gastos")
        edited_gastos = st.data_editor(st.session_state.gastos, num_rows="dynamic", use_container_width=True, key="editor_gastos")
        st.session_state.gastos = edited_gastos

# ==========================================
# MENÚ LATERAL Y NAVEGACIÓN
# ==========================================
with st.sidebar:
    st.markdown("### 🚀 Agencia OS")
    st.markdown("**Navegación**")
    
    opcion = st.radio(
        "Selecciona un módulo:",
        ["Dashboard 360°", "CRM & Prospección", "Facturación PDF", "Tareas & Proyectos", "Finanzas"],
        label_visibility="collapsed"
    )

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
