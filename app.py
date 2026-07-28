import streamlit as st
import pandas as pd
from datetime import date

# ==========================================
# CONFIGURACIÓN DE PÁGINA Y CSS PREMIUM
# ==========================================
st.set_page_config(
    page_title="Presencia Web Pro - Agencia OS",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS avanzados para interfaz SaaS moderna
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    .stApp {
        background-color: #0b0f17;
    }
    
    /* Tarjetas de métricas */
    .dash-card {
        background: linear-gradient(135deg, #161b26 0%, #11141d 100%);
        border: 1px solid #232a3b;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 10px 25px -10px rgba(0, 0, 0, 0.4);
        margin-bottom: 15px;
    }
    
    .dash-card-title {
        color: #94a3b8;
        font-size: 13px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
    }
    
    .dash-card-value {
        color: #ffffff;
        font-size: 26px;
        font-weight: 800;
        margin-bottom: 4px;
    }
    
    /* Etiquetas / Badges */
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
    
    /* Hero Banner */
    .hero-banner {
        background: linear-gradient(90deg, #1e1b4b 0%, #31104b 50%, #0f172a 100%);
        border: 1px solid #3730a3;
        border-radius: 18px;
        padding: 24px;
        margin-bottom: 25px;
    }
    
    /* Botones principales */
    .stButton>button {
        border-radius: 10px !important;
        font-weight: 600 !important;
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.5rem 1.2rem !important;
        box-shadow: 0 4px 14px rgba(99, 102, 241, 0.3) !important;
    }
    
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

# Formateador de moneda en español
def formato_euro(valor):
    return f"{valor:,.2f} €".replace(",", "X").replace(".", ",").replace("X", ".")

# ==========================================
# INICIALIZACIÓN DE DATOS (PERSISTENCIA)
# ==========================================
if "leads" not in st.session_state:
    st.session_state.leads = pd.DataFrame([
        {"Cliente": "Clínica Dental Murcia S.L.", "Contacto": "Dr. Antonio", "Fase": "Cierre Ganado", "Valor (€)": 605.0, "Prioridad": "Alta 🔴"},
        {"Cliente": "Gimnasio FitLife", "Contacto": "Carlos Gómez", "Fase": "Propuesta Enviada", "Valor (€)": 2500.0, "Prioridad": "Alta 🔴"},
        {"Cliente": "Hotel Costa Azul", "Contacto": "Elena Soria", "Fase": "Contacto Inicial", "Valor (€)": 1200.0, "Prioridad": "Media 🟡"},
        {"Cliente": "Clínica Estética Aura", "Contacto": "Dr. Roberto Ruiz", "Fase": "Negociación", "Valor (€)": 4800.0, "Prioridad": "Alta 🔴"},
        {"Cliente": "Panadería Gourmet", "Contacto": "Javier López", "Fase": "Propuesta Enviada", "Valor (€)": 1500.0, "Prioridad": "Media 🟡"}
    ])

if "proyectos" not in st.session_state:
    st.session_state.proyectos = pd.DataFrame([
        {"Proyecto": "Posicionamiento SEO & Campañas", "Cliente": "Clínica Dental Murcia S.L.", "Estado": "En Progreso", "Prioridad": "Alta 🔴", "Fecha Límite": "2026-08-15"},
        {"Proyecto": "Rediseño Web Corporativo", "Cliente": "Gimnasio FitLife", "Estado": "Pendiente", "Prioridad": "Alta 🔴", "Fecha Límite": "2026-08-20"},
        {"Proyecto": "Estrategia Local Google Maps", "Cliente": "Hotel Costa Azul", "Estado": "Pendiente", "Prioridad": "Media 🟡", "Fecha Límite": "2026-08-30"},
        {"Proyecto": "Landing Page Captación", "Cliente": "Clínica Estética Aura", "Estado": "En Revisión", "Prioridad": "Alta 🔴", "Fecha Límite": "2026-08-10"},
        {"Proyecto": "Branding & Redes Sociales", "Cliente": "Panadería Gourmet", "Estado": "En Progreso", "Prioridad": "Media 🟡", "Fecha Límite": "2026-09-05"}
    ])

if "facturas" not in st.session_state:
    st.session_state.facturas = pd.DataFrame([
        {"Número": "FACT-2026-001", "Cliente": "Clínica Dental Murcia S.L.", "Fecha": "2026-07-28", "Base (€)": 500.0, "IVA (%)": 21, "Total (€)": 605.0}
    ])

if "gastos" not in st.session_state:
    st.session_state.gastos = pd.DataFrame([
        {"Concepto": "Herramientas SEO & Software", "Categoría": "Suscripciones", "Importe (€)": 450.0, "Fecha": "2026-07-05"},
        {"Concepto": "Servidores & Hosting Pro", "Categoría": "Infraestructura", "Importe (€)": 250.0, "Fecha": "2026-07-12"},
        {"Concepto": "Publicidad Meta Ads", "Categoría": "Marketing", "Importe (€)": 800.0, "Fecha": "2026-07-20"}
    ])

# ==========================================
# MÓDULOS DE LA APLICACIÓN
# ==========================================

def mostrar_dashboard():
    html_banner = """
    <div class="hero-banner">
        <h1 style="color: #ffffff; font-size: 26px; font-weight: 800; margin: 0 0 6px 0;">⚡ Presencia Web Pro — Control General</h1>
        <p style="color: #a5b4fc; font-size: 14px; margin: 0;">Panel consolidado con métricas operativas, comerciales y financieras en tiempo real.</p>
    </div>
    """
    render_html_clean(html_banner)
    
    total_ingresos = st.session_state.facturas["Total (€)"].sum() if not st.session_state.facturas.empty else 0.0
    total_gastos = st.session_state.gastos["Importe (€)"].sum() if not st.session_state.gastos.empty else 0.0
    beneficio = total_ingresos - total_gastos
    valor_pipeline = st.session_state.leads["Valor (€)"].sum() if not st.session_state.leads.empty else 0.0
    
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        render_html_clean(f"""
        <div class="dash-card">
            <div class="dash-card-title">Facturación Emitida</div>
            <div class="dash-card-value">{formato_euro(total_ingresos)}</div>
            <span class="badge-success">Ingresos Reales</span>
        </div>
        """)
        
    with c2:
        render_html_clean(f"""
        <div class="dash-card">
            <div class="dash-card-title">Beneficio Neto</div>
            <div class="dash-card-value" style="color: {'#10b981' if beneficio >= 0 else '#ef4444'};">{formato_euro(beneficio)}</div>
            <span class="badge-indigo">Ingresos - Gastos</span>
        </div>
        """)
        
    with c3:
        render_html_clean(f"""
        <div class="dash-card">
            <div class="dash-card-title">Pipeline Comercial</div>
            <div class="dash-card-value">{formato_euro(valor_pipeline)}</div>
            <span class="badge-warning">{len(st.session_state.leads)} Prospects</span>
        </div>
        """)
        
    with c4:
        render_html_clean(f"""
        <div class="dash-card">
            <div class="dash-card-title">Proyectos en Curso</div>
            <div class="dash-card-value">{len(st.session_state.proyectos)}</div>
            <span class="badge-indigo">Sincronizados</span>
        </div>
        """)
    
    st.write("")
    col_izq, col_der = st.columns([1.8, 1.2], gap="large")
    
    with col_izq:
        st.subheader("📈 Resumen de Crecimiento")
        df_tendencia = pd.DataFrame({
            "Mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul"],
            "Ingresos (€)": [4200, 5100, 4800, 6200, 5900, 7100, total_ingresos],
            "Gastos (€)": [2100, 2300, 2400, 2900, 2700, 3100, total_gastos]
        }).set_index("Mes")
        st.area_chart(df_tendencia, color=["#6366f1", "#ef4444"])
        
    with col_der:
        st.subheader("🔔 Feed de Operaciones")
        feed_html = f"""
        <div style="background: #161b26; border: 1px solid #232a3b; border-radius: 14px; padding: 18px;">
            <div style="margin-bottom: 16px; border-bottom: 1px solid #232a3b; padding-bottom: 12px;">
                <span class="badge-success">Facturación</span>
                <p style="color: #e2e8f0; font-size: 13px; font-weight: 600; margin: 6px 0 2px 0;">Última factura cobrada</p>
                <p style="color: #64748b; font-size: 12px; margin: 0;">Clínica Dental Murcia S.L. • {formato_euro(total_ingresos)}</p>
            </div>
            <div style="margin-bottom: 16px; border-bottom: 1px solid #232a3b; padding-bottom: 12px;">
                <span class="badge-warning">CRM</span>
                <p style="color: #e2e8f0; font-size: 13px; font-weight: 600; margin: 6px 0 2px 0;">Valor Total Oportunidades</p>
                <p style="color: #64748b; font-size: 12px; margin: 0;">{formato_euro(valor_pipeline)} en negociación</p>
            </div>
            <div>
                <span class="badge-indigo">Proyectos</span>
                <p style="color: #e2e8f0; font-size: 13px; font-weight: 600; margin: 6px 0 2px 0;">Carga Operativa</p>
                <p style="color: #64748b; font-size: 12px; margin: 0;">{len(st.session_state.proyectos)} clientes activos en desarrollo</p>
            </div>
        </div>
        """
        render_html_clean(feed_html)


def mostrar_crm():
    st.title("🎯 CRM & Prospección Comercial")
    st.markdown("Edita las celdas directamente o utiliza las herramientas rápidas de alta y baja.")
    
    total_pipeline = st.session_state.leads["Valor (€)"].sum() if not st.session_state.leads.empty else 0.0
    leads_count = len(st.session_state.leads)
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Oportunidades Totales", f"{leads_count}")
    c2.metric("Valor del Pipeline", formato_euro(total_pipeline))
    c3.metric("Promedio por Lead", formato_euro(total_pipeline / leads_count if leads_count > 0 else 0))
    
    st.divider()
    
    st.subheader("📋 Tabla de Leads y Estado Comercial")
    st.caption("💡 Para borrar desde la tabla: Marca el checkbox de la izquierda del cliente y pulsa la papelera (o tecla 'Supr').")
    
    edited_leads = st.data_editor(
        st.session_state.leads,
        num_rows="dynamic",
        use_container_width=True,
        key="editor_leads"
    )
    st.session_state.leads = edited_leads
    
    st.divider()
    
    # Herramientas de Gestión (Añadir / Eliminar Rápido)
    col_add, col_del = st.columns(2, gap="large")
    
    with col_add:
        with st.expander("➕ Añadir Nuevo Lead Rápidamente"):
            with st.form("form_nuevo_lead", clear_on_submit=True):
                cliente = st.text_input("Nombre de la Empresa / Cliente")
                contacto = st.text_input("Persona de Contacto")
                fase = st.selectbox("Fase Inicial", ["Contacto Inicial", "Propuesta Enviada", "Negociación", "Cierre Ganado"])
                valor = st.number_input("Valor Estimado (€)", value=1000.0, step=100.0)
                prioridad = st.selectbox("Prioridad", ["Alta 🔴", "Media 🟡", "Baja 🟢"])
                
                if st.form_submit_button("Guardar en el CRM"):
                    if cliente:
                        nuevo_registro = pd.DataFrame([{
                            "Cliente": cliente,
                            "Contacto": contacto,
                            "Fase": fase,
                            "Valor (€)": valor,
                            "Prioridad": prioridad
                        }])
                        st.session_state.leads = pd.concat([st.session_state.leads, nuevo_registro], ignore_index=True)
                        st.success(f"¡Lead '{cliente}' añadido!")
                        st.rerun()

    with col_del:
        with st.expander("🗑️ Borrado Rápido de Lead"):
            if not st.session_state.leads.empty:
                lead_a_borrar = st.selectbox("Selecciona el cliente a eliminar:", st.session_state.leads["Cliente"].unique(), key="select_del_lead")
                if st.button("❌ Eliminar Lead Seleccionado", key="btn_del_lead"):
                    st.session_state.leads = st.session_state.leads[st.session_state.leads["Cliente"] != lead_a_borrar].reset_index(drop=True)
                    st.success(f"Lead '{lead_a_borrar}' eliminado.")
                    st.rerun()
            else:
                st.info("No hay leads para eliminar.")


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
        
        st.markdown(f"**Total Factura:** <span style='color:#10b981; font-size:18px; font-weight:700;'>{formato_euro(total)}</span>", unsafe_allow_html=True)
        
        if st.button("💾 Registrar Factura"):
            nueva_factura = pd.DataFrame([{
                "Número": num_factura,
                "Cliente": cliente,
                "Fecha": str(date.today()),
                "Base (€)": base_imponible,
                "IVA (%)": iva,
                "Total (€)": total
            }])
            st.session_state.facturas = pd.concat([st.session_state.facturas, nueva_factura], ignore_index=True)
            st.success(f"Factura {num_factura} registrada. ¡Añadida automáticamente a tus Finanzas!")

    with col2:
        st.subheader("👁️ Vista Previa del Documento")
        
        html_factura = f"""
        <div style="background-color: #ffffff; padding: 32px; border-radius: 12px; color: #111111; box-shadow: 0 10px 25px rgba(0,0,0,0.3); font-family: Arial, sans-serif;">
            <h2 style="color: #0f172a; margin: 0 0 4px 0; font-size: 24px; font-weight: 800;">Presencia Web Pro</h2>
            <p style="color: #64748b; font-size: 12px; margin: 0 0 20px 0;">NIF: B99887766 | contacto@presenciawebpro.com</p>
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
                        <td style="text-align: right; padding: 10px;">{formato_euro(base_imponible)}</td>
                    </tr>
                </tbody>
            </table>
            <div style="text-align: right; font-size: 13px;">
                <p style="margin: 4px 0;">Base Imponible: <strong>{formato_euro(base_imponible)}</strong></p>
                <p style="margin: 4px 0;">IVA ({iva}%): <strong>{formato_euro(cuota_iva)}</strong></p>
                <h3 style="margin-top: 10px; font-size: 22px; color: #0f172a;">Total: {formato_euro(total)}</h3>
            </div>
        </div>
        """
        render_html_clean(html_factura)
        st.caption("💡 Para guardar en PDF: Pulsa Ctrl + P (o Cmd + P en Mac) y selecciona 'Guardar como PDF'.")


def mostrar_tareas_proyectos():
    st.title("📋 Tareas & Proyectos")
    st.markdown("Gestión interactiva de proyectos operativos.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Proyectos Totales", f"{len(st.session_state.proyectos)}")
    col2.metric("En Progreso", f"{len(st.session_state.proyectos[st.session_state.proyectos['Estado'] == 'En Progreso'])}")
    col3.metric("Pendientes", f"{len(st.session_state.proyectos[st.session_state.proyectos['Estado'] == 'Pendiente'])}")
    
    st.divider()
    
    st.subheader("🛠️ Control Operativo de Proyectos")
    st.caption("💡 Haz doble clic en las celdas para modificar datos, o usa los paneles de abajo para añadir/borrar.")
    
    edited_proyectos = st.data_editor(
        st.session_state.proyectos,
        num_rows="dynamic",
        use_container_width=True,
        key="editor_proyectos"
    )
    st.session_state.proyectos = edited_proyectos
    
    st.divider()
    
    col_add_p, col_del_p = st.columns(2, gap="large")
    
    with col_add_p:
        with st.expander("➕ Crear Nuevo Proyecto"):
            with st.form("form_nuevo_proyecto", clear_on_submit=True):
                nombre_p = st.text_input("Nombre del Proyecto")
                cliente_p = st.text_input("Cliente Asignado")
                estado_p = st.selectbox("Estado", ["Pendiente", "En Progreso", "En Revisión", "Completado"])
                prioridad_p = st.selectbox("Prioridad", ["Alta 🔴", "Media 🟡", "Baja 🟢"])
                fecha_p = st.date_input("Fecha Límite")
                
                if st.form_submit_button("Guardar Proyecto"):
                    if nombre_p:
                        nuevo_p = pd.DataFrame([{
                            "Proyecto": nombre_p,
                            "Cliente": cliente_p,
                            "Estado": estado_p,
                            "Prioridad": prioridad_p,
                            "Fecha Límite": str(fecha_p)
                        }])
                        st.session_state.proyectos = pd.concat([st.session_state.proyectos, nuevo_p], ignore_index=True)
                        st.success(f"Proyecto '{nombre_p}' creado.")
                        st.rerun()

    with col_del_p:
        with st.expander("🗑️ Borrado Rápido de Proyecto"):
            if not st.session_state.proyectos.empty:
                proy_a_borrar = st.selectbox("Selecciona el proyecto a eliminar:", st.session_state.proyectos["Proyecto"].unique(), key="select_del_proy")
                if st.button("❌ Eliminar Proyecto Seleccionado", key="btn_del_proy"):
                    st.session_state.proyectos = st.session_state.proyectos[st.session_state.proyectos["Proyecto"] != proy_a_borrar].reset_index(drop=True)
                    st.success(f"Proyecto '{proy_a_borrar}' eliminado.")
                    st.rerun()
            else:
                st.info("No hay proyectos para eliminar.")


def mostrar_finanzas():
    st.title("💰 Panel Financiero Transparente")
    st.markdown("Desglose claro de ingresos reales y gastos operativos.")
    
    total_ingresos = st.session_state.facturas["Total (€)"].sum() if not st.session_state.facturas.empty else 0.0
    total_gastos = st.session_state.gastos["Importe (€)"].sum() if not st.session_state.gastos.empty else 0.0
    beneficio_neto = total_ingresos - total_gastos
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Ingresos Totales (Facturas)", formato_euro(total_ingresos))
    col2.metric("Gastos Totales Registrados", formato_euro(total_gastos), delta_color="inverse")
    col3.metric("Beneficio Neto Real", formato_euro(beneficio_neto))
    
    st.divider()
    
    st.subheader("📊 Comparativa Financiera")
    df_comparativa = pd.DataFrame({
        "Concepto": ["Ingresos Facturados", "Gastos Totales", "Beneficio Neto"],
        "Importe (€)": [total_ingresos, total_gastos, beneficio_neto]
    }).set_index("Concepto")
    
    st.bar_chart(df_comparativa, color="#6366f1")
    
    st.divider()
    
    col_a, col_b = st.columns(2, gap="large")
    
    with col_a:
        st.subheader("📥 Origen de Ingresos (Facturas)")
        st.caption("Datos procedentes de 'Facturación PDF'.")
        st.dataframe(st.session_state.facturas[["Número", "Cliente", "Total (€)", "Fecha"]], use_container_width=True, hide_index=True)
        
    with col_b:
        st.subheader("📤 Control de Gastos")
        st.caption("Añade, edita o elimina partidas de gasto.")
        edited_gastos = st.data_editor(st.session_state.gastos, num_rows="dynamic", use_container_width=True, key="editor_gastos")
        st.session_state.gastos = edited_gastos
        
        with st.expander("🗑️ Borrado Rápido de Gasto"):
            if not st.session_state.gastos.empty:
                gasto_a_borrar = st.selectbox("Selecciona el concepto a eliminar:", st.session_state.gastos["Concepto"].unique(), key="select_del_gasto")
                if st.button("❌ Eliminar Gasto Seleccionado", key="btn_del_gasto"):
                    st.session_state.gastos = st.session_state.gastos[st.session_state.gastos["Concepto"] != gasto_a_borrar].reset_index(drop=True)
                    st.success(f"Gasto '{gasto_a_borrar}' eliminado.")
                    st.rerun()

# ==========================================
# MENÚ LATERAL Y NAVEGACIÓN
# ==========================================
with st.sidebar:
    st.markdown("### 🚀 Presencia Web Pro")
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
