import streamlit as st
import pandas as pd
from datetime import date

# ==========================================
# CONFIGURACIÓN DE PÁGINA Y CSS PREMIUM
# ==========================================
st.set_page_config(
    page_title="Agencia OS",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inyección de CSS personalizado para estética SaaS Moderna
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    /* Fuente global */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    /* Fondo principal sutilmente oscurecido */
    .stApp {
        background-color: #0b0f17;
    }
    
    /* Tarjetas personalizadas del Dashboard */
    .dash-card {
        background: linear-gradient(135deg, #161b26 0%, #11141d 100%);
        border: 1px solid #232a3b;
        border-radius: 16px;
        padding: 22px;
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
        margin-bottom: 15px;
    }
    
    .dash-card-title {
        color: #8b949e;
        font-size: 13px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
    }
    
    .dash-card-value {
        color: #ffffff;
        font-size: 28px;
        font-weight: 800;
        margin-bottom: 6px;
    }
    
    /* Badges de estado */
    .badge-success {
        background-color: rgba(16, 185, 129, 0.15);
        color: #10b981;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
    }
    
    .badge-indigo {
        background-color: rgba(99, 102, 241, 0.15);
        color: #818cf8;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
    }

    .badge-warning {
        background-color: rgba(245, 158, 11, 0.15);
        color: #f59e0b;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
    }
    
    /* Banner de bienvenida */
    .hero-banner {
        background: linear-gradient(90deg, #1e1b4b 0%, #31104b 50%, #0f172a 100%);
        border: 1px solid #3730a3;
        border-radius: 18px;
        padding: 28px;
        margin-bottom: 25px;
    }
    
    /* Botones estilizados */
    .stButton>button {
        border-radius: 10px !important;
        font-weight: 600 !important;
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.6rem 1.2rem !important;
        box-shadow: 0 4px 14px rgba(99, 102, 241, 0.3) !important;
    }
    
    /* Ajustes generales de tablas */
    div[data-testid="stDataFrame"] {
        border: 1px solid #232a3b;
        border-radius: 12px;
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

# Función auxiliar para renderizar HTML limpio
def render_html_clean(html_text):
    clean_text = "\n".join([line.strip() for line in html_text.split("\n")])
    st.markdown(clean_text, unsafe_allow_html=True)

# ==========================================
# INICIALIZACIÓN DE DATOS (PERSISTENCIA)
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
    # Banner de bienvenida tipo SaaS
    html_banner = """
    <div class="hero-banner">
        <h1 style="color: #ffffff; font-size: 26px; font-weight: 800; margin: 0 0 6px 0;">⚡ Panel de Control de la Agencia</h1>
        <p style="color: #a5b4fc; font-size: 14px; margin: 0;">Resumen en tiempo real del rendimiento operativo, financiero y comercial.</p>
    </div>
    """
    render_html_clean(html_banner)
    
    # Cálculos en tiempo real
    total_ingresos = st.session_state.facturas["Total (€)"].sum()
    total_gastos = st.session_state.gastos["Importe (€)"].sum()
    beneficio = total_ingresos - total_gastos
    valor_pipeline = st.session_state.leads["Valor (€)"].sum() if not st.session_state.leads.empty else 0
    total_prospects = len(st.session_state.leads)
    
    # Tarjetas KPI con CSS estilizado
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        render_html_clean(f"""
        <div class="dash-card">
            <div class="dash-card-title">Facturación Total</div>
            <div class="dash-card-value">{total_ingresos:,.2f} €</div>
            <span class="badge-success">↑ 100% Facturado</span>
        </div>
        """)
        
    with c2:
        render_html_clean(f"""
        <div class="dash-card">
            <div class="dash-card-title">Beneficio Neto</div>
            <div class="dash-card-value" style="color: {'#10b981' if beneficio >= 0 else '#ef4444'};">{beneficio:,.2f} €</div>
            <span class="badge-indigo">Margen Real</span>
        </div>
        """)
        
    with c3:
        render_html_clean(f"""
        <div class="dash-card">
            <div class="dash-card-title">Pipeline Comercial</div>
            <div class="dash-card-value">{valor_pipeline:,.2f} €</div>
            <span class="badge-warning">{total_prospects} Oportunidades</span>
        </div>
        """)
        
    with c4:
        render_html_clean(f"""
        <div class="dash-card">
            <div class="dash-card-title">Proyectos Activos</div>
            <div class="dash-card-value">3</div>
            <span class="badge-indigo">1 Entregable HOY</span>
        </div>
        """)
    
    st.write("") # Espaciador
    
    # Grid de 2 columnas: Gráfica de Tendencia + Actividad Reciente
    col_izq, col_der = st.columns([1.8, 1.2], gap="large")
    
    with col_izq:
        st.subheader("📈 Tendencia Financiera (2026)")
        
        # Generación de datos visuales armoniosos
        df_tendencia = pd.DataFrame({
            "Mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul"],
            "Ingresos (€)": [4200, 5100, 4800, 6200, 5900, 7100, total_ingresos if total_ingresos > 0 else 8500],
            "Gastos (€)": [2100, 2300, 2400, 2900, 2700, 3100, total_gastos]
        }).set_index("Mes")
        
        # Gráfica de área moderna
        st.area_chart(df_tendencia, color=["#6366f1", "#ef4444"])
        
    with col_der:
        st.subheader("🔔 Feed de Actividad y Estado")
        
        feed_html = """
        <div style="background: #161b26; border: 1px solid #232a3b; border-radius: 14px; padding: 18px;">
            <div style="margin-bottom: 16px; border-bottom: 1px solid #232a3b; padding-bottom: 12px;">
                <span class="badge-success">Facturación</span>
                <p style="color: #e2e8f0; font-size: 13px; font-weight: 600; margin: 6px 0 2px 0;">Nueva factura registrada</p>
                <p style="color: #64748b; font-size: 12px; margin: 0;">Clínica Dental Murcia S.L. • Hace un momento</p>
            </div>
            <div style="margin-bottom: 16px; border-bottom: 1px solid #232a3b; padding-bottom: 12px;">
                <span class="badge-warning">CRM</span>
                <p style="color: #e2e8f0; font-size: 13px; font-weight: 600; margin: 6px 0 2px 0;">Propuesta enviada</p>
                <p style="color: #64748b; font-size: 12px; margin: 0;">Gimnasio FitLife (2.500 €)</p>
            </div>
            <div>
                <span class="badge-indigo">Operaciones</span>
                <p style="color: #e2e8f0; font-size: 13px; font-weight: 600; margin: 6px 0 2px 0;">Sprint de Proyectos en curso</p>
                <p style="color: #64748b; font-size: 12px; margin: 0;">3 entregables en revisión esta semana</p>
            </div>
        </div>
        """
        render_html_clean(feed_html)


def mostrar_crm():
    st.title("🎯 CRM & Prospección")
    st.markdown("Gestión interactiva de clientes. **Edita las celdas directamente o añade/elimina filas.**")
    
    total_pipeline = st.session_state.leads["Valor (€)"].sum() if not st.session_state.leads.empty else 0
    leads_count = len(st.session_state.leads)
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Prospects", f"{leads_count}")
    c2.metric("Valor del Pipeline", f"{total_pipeline:,.2f} €")
    c3.metric("Promedio / Lead", f"{(total_pipeline/leads_count) if leads_count > 0 else 0:,.2f} €")
    
    st.divider()
    
    st.subheader("📋 Embudo de Ventas (Pipeline)")
    st.caption("💡 Haz doble clic en cualquier celda para editar, o selecciona filas y usa la tecla 'Supr' / 'Delete' para eliminar.")
    
    edited_leads = st.data_editor(
        st.session_state.leads,
        num_rows="dynamic",
        use_container_width=True,
        key="editor_leads"
    )
    st.session_state.leads = edited_leads
    
    st.divider()
    
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
        
        st.markdown(f"**Total Factura:** <span style='color:#10b981; font-size:18px; font-weight:700;'>{total:.2f} €</span>", unsafe_allow_html=True)
        
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
            st.success(f"Factura {num_factura} registrada correctamente.")

    with col2:
        st.subheader("👁️ Vista Previa del Documento")
        
        html_factura = f"""
        <div style="background-color: #ffffff; padding: 32px; border-radius: 12px; color: #111111; box-shadow: 0 10px 25px rgba(0,0,0,0.3); font-family: Arial, sans-serif;">
            <h2 style="color: #0f172a; margin: 0 0 4px 0; font-size: 24px; font-weight: 800;">MI AGENCIA DIGITAL</h2>
            <p style="color: #64748b; font-size: 12px; margin: 0 0 20px 0;">NIF: B99887766 | info@miagencia.com</p>
            <hr style="border: 0; border-top: 1px solid #e2e8f0; margin-bottom: 20px;">
            <p style="font-size: 13px; margin: 3px 0;"><strong>Factura Nº:</strong> {num_factura}</p>
            <p style="font-size: 13px; margin: 3px 0 16px 0;"><strong>Fecha:</strong> {date.today()}</p>
            <div style="background-color: #f8fafc; padding: 14px; border-radius: 8px; margin-bottom: 20px; border: 1px solid #e2e8f0;">
                <p style="font-size: 13px; margin: 2px 0;"><strong>Cliente:</strong> {cliente}</p>
                <p style="font-size: 13px; margin: 2px 0;"><strong>NIF/CIF:</strong> {nif}</p>
            </div>
            <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px; font-size: 13px;">
                <thead>
                    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
                        <th style="text-align: left; padding: 10px;">Concepto</th>
                        <th style="text-align: right; padding: 10px;">Importe</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="border-bottom: 1px solid #e2e8f0;">
                        <td style="padding: 10px;">{concepto}</td>
                        <td style="text-align: right; padding: 10px;">{base_imponible:.2f} €</td>
                    </tr>
                </tbody>
            </table>
            <div style="text-align: right; font-size: 13px;">
                <p style="margin: 4px 0;">Base Imponible: <strong>{base_imponible:.2f} €</strong></p>
                <p style="margin: 4px 0;">IVA ({iva}%): <strong>{cuota_iva:.2f} €</strong></p>
                <h3 style="margin-top: 10px; font-size: 22px; color: #0f172a;">Total: {total:.2f} €</h3>
            </div>
        </div>
        """
        render_html_clean(html_factura)
        st.caption("💡 Para guardar en PDF: Pulsa Ctrl + P (o Cmd + P en Mac) y selecciona 'Guardar como PDF'.")


def mostrar_tareas_proyectos():
    st.title("📋 Tareas & Proyectos")
    st.markdown("Control de estados y entregables operativos.")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Proyectos Activos", "3")
    c2.metric("Pendientes", "1")
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
    st.markdown("Los datos de ingresos se calculan de forma **automatizada** a partir de tus facturas.")
    
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
