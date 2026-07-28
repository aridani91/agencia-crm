import streamlit as st
import pandas as pd
from datetime import date

# ==========================================
# CONFIGURACIÓN DE PÁGINA Y CSS PREMIUM
# ==========================================
st.set_page_config(
    page_title="Presencia Web Pro - OS",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS avanzados para un aspecto SaaS de alto nivel
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    .stApp {
        background-color: #080b11;
    }
    
    /* Tarjetas de métricas estilizadas */
    .metric-card {
        background: linear-gradient(145deg, #131924 0%, #0d121a 100%);
        border: 1px solid #20293a;
        border-radius: 16px;
        padding: 22px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.35);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    
    .metric-card:hover {
        border-color: #3b82f6;
        transform: translateY(-2px);
    }
    
    .metric-title {
        color: #94a3b8;
        font-size: 12px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 8px;
    }
    
    .metric-value {
        color: #f8fafc;
        font-size: 28px;
        font-weight: 800;
        letter-spacing: -0.5px;
    }
    
    /* Contenedores con estilo */
    .custom-container {
        background-color: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 20px;
    }
    
    /* Badges de estado */
    .badge-emerald {
        background: rgba(16, 185, 129, 0.12);
        color: #10b981;
        border: 1px solid rgba(16, 185, 129, 0.3);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
        display: inline-block;
    }
    
    .badge-indigo {
        background: rgba(99, 102, 241, 0.12);
        color: #818cf8;
        border: 1px solid rgba(99, 102, 241, 0.3);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
        display: inline-block;
    }

    .badge-amber {
        background: rgba(245, 158, 11, 0.12);
        color: #f59e0b;
        border: 1px solid rgba(245, 158, 11, 0.3);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
        display: inline-block;
    }
    
    /* Hero Banner */
    .hero-banner {
        background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 60%, #172554 100%);
        border: 1px solid #312e81;
        border-radius: 20px;
        padding: 26px 30px;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }
    
    /* Botones primarios */
    .stButton>button {
        border-radius: 12px !important;
        font-weight: 700 !important;
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important;
        color: #ffffff !important;
        border: none !important;
        padding: 0.6rem 1.4rem !important;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.35) !important;
        transition: all 0.2s ease !important;
    }
    
    .stButton>button:hover {
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.5) !important;
        transform: translateY(-1px);
    }
    
    /* Tablas data_editor */
    div[data-testid="stDataFrame"] {
        border: 1px solid #1e293b;
        border-radius: 14px;
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

def render_html_clean(html_text):
    clean_text = "\n".join([line.strip() for line in html_text.split("\n")])
    st.markdown(clean_text, unsafe_allow_html=True)

def formato_euro(valor):
    return f"{valor:,.2f} €".replace(",", "X").replace(".", ",").replace("X", ".")

# ==========================================
# INICIALIZACIÓN DE DATOS (PERSISTENCIA)
# ==========================================

# Tareas diarias del Dashboard
if "tareas_diarias" not in st.session_state:
    st.session_state.tareas_diarias = [
        {"tarea": "Llamar a Gimnasio FitLife para revisar propuesta", "hecha": False},
        {"tarea": "Revisar entregable SEO de Clínica Dental Murcia", "hecha": True},
        {"tarea": "Enviar factura FACT-2026-002 al cliente", "hecha": False},
        {"tarea": "Reunión de valoración con Clínica Estética Aura", "hecha": False}
    ]

# CRM - Prospección Comercial (Antes de cobrar)
if "leads" not in st.session_state:
    st.session_state.leads = pd.DataFrame([
        {"Prospecto": "Gimnasio FitLife", "Contacto": "Carlos Gómez", "Teléfono / Email": "carlos@fitlife.es", "Etapa Comercial": "Propuesta Enviada", "Valor Cotizado (€)": 2500.0, "Próximo Contacto": "2026-08-02"},
        {"Prospecto": "Hotel Costa Azul", "Contacto": "Elena Soria", "Teléfono / Email": "info@hotelcosta.com", "Etapa Comercial": "Llamada Inicial", "Valor Cotizado (€)": 1200.0, "Próximo Contacto": "2026-08-01"},
        {"Prospecto": "Clínica Estética Aura", "Contacto": "Dr. Roberto", "Teléfono / Email": "roberto@esteticaaura.com", "Etapa Comercial": "Negociación", "Valor Cotizado (€)": 4800.0, "Próximo Contacto": "2026-07-30"},
        {"Prospecto": "Panadería Gourmet", "Contacto": "Javier López", "Teléfono / Email": "javier@panaderiagourmet.com", "Etapa Comercial": "Propuesta Enviada", "Valor Cotizado (€)": 1500.0, "Próximo Contacto": "2026-08-05"}
    ])

# Proyectos - Producción Operativa (Después de cobrar)
if "proyectos" not in st.session_state:
    st.session_state.proyectos = pd.DataFrame([
        {"Proyecto": "Campaña SEO & Google Ads", "Cliente Activo": "Clínica Dental Murcia S.L.", "Fase Trabajo": "En Desarrollo", "Progreso (%)": 65, "Fecha Entrega": "2026-08-15", "Responsable": "Ana (SEO)"},
        {"Proyecto": "Rediseño Web e-Commerce", "Cliente Activo": "Tech Solutions S.L.", "Fase Trabajo": "Diseño Figma", "Progreso (%)": 30, "Fecha Entrega": "2026-08-28", "Responsable": "David (Dev)"},
        {"Proyecto": "Auditoría de Conversión", "Cliente Activo": "Restaurante El Faro", "Fase Trabajo": "En Revisión", "Progreso (%)": 90, "Fecha Entrega": "2026-08-05", "Responsable": "Ana (SEO)"}
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
        <h1 style="color: #ffffff; font-size: 28px; font-weight: 800; margin: 0 0 6px 0;">⚡ Presencia Web Pro</h1>
        <p style="color: #a5b4fc; font-size: 14px; margin: 0;">Centro de mando operativo, comercial y financiero.</p>
    </div>
    """
    render_html_clean(html_banner)
    
    total_ingresos = st.session_state.facturas["Total (€)"].sum() if not st.session_state.facturas.empty else 0.0
    total_gastos = st.session_state.gastos["Importe (€)"].sum() if not st.session_state.gastos.empty else 0.0
    beneficio = total_ingresos - total_gastos
    valor_pipeline = st.session_state.leads["Valor Cotizado (€)"].sum() if not st.session_state.leads.empty else 0.0
    
    # KPIs visuales
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        render_html_clean(f"""
        <div class="metric-card">
            <div class="metric-title">Facturación Cobrada</div>
            <div class="metric-value">{formato_euro(total_ingresos)}</div>
            <div style="margin-top: 10px;"><span class="badge-emerald">Facturas Emitidas</span></div>
        </div>
        """)
        
    with c2:
        render_html_clean(f"""
        <div class="metric-card">
            <div class="metric-title">Beneficio Neto</div>
            <div class="metric-value" style="color: {'#10b981' if beneficio >= 0 else '#f43f5e'};">{formato_euro(beneficio)}</div>
            <div style="margin-top: 10px;"><span class="badge-indigo">Margen Real</span></div>
        </div>
        """)
        
    with c3:
        render_html_clean(f"""
        <div class="metric-card">
            <div class="metric-title">Pipeline Ventas</div>
            <div class="metric-value">{formato_euro(valor_pipeline)}</div>
            <div style="margin-top: 10px;"><span class="badge-amber">{len(st.session_state.leads)} Prospects</span></div>
        </div>
        """)
        
    with c4:
        render_html_clean(f"""
        <div class="metric-card">
            <div class="metric-title">Proyectos Activos</div>
            <div class="metric-value">{len(st.session_state.proyectos)}</div>
            <div style="margin-top: 10px;"><span class="badge-indigo">En Producción</span></div>
        </div>
        """)
    
    st.write("")
    
    # Grid principal: Checklist de Tareas + Gráfica de Rendimiento
    col_izq, col_der = st.columns([1.3, 1.7], gap="large")
    
    with col_izq:
        st.subheader("✅ Tareas Clave del Día")
        st.caption("Gestiona tus prioridades de hoy directamente desde el Dashboard.")
        
        # Rendimiento interactivo de tareas diarias
        updated_tasks = []
        for i, t in enumerate(st.session_state.tareas_diarias):
            checked = st.checkbox(t["tarea"], value=t["hecha"], key=f"dash_task_{i}")
            updated_tasks.append({"tarea": t["tarea"], "hecha": checked})
        st.session_state.tareas_diarias = updated_tasks
        
        # Añadir nueva tarea rápida al checklist
        with st.popover("➕ Añadir tarea rápida"):
            nueva_t = st.text_input("Nueva tarea para hoy:")
            if st.button("Guardar tarea"):
                if nueva_t:
                    st.session_state.tareas_diarias.append({"tarea": nueva_t, "hecha": False})
                    st.rerun()

    with col_der:
        st.subheader("📈 Rendimiento Financiero")
        df_tendencia = pd.DataFrame({
            "Mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul"],
            "Ingresos (€)": [4200, 5100, 4800, 6200, 5900, 7100, total_ingresos],
            "Gastos (€)": [2100, 2300, 2400, 2900, 2700, 3100, total_gastos]
        }).set_index("Mes")
        st.area_chart(df_tendencia, color=["#6366f1", "#f43f5e"])


def mostrar_crm():
    st.title("🎯 CRM & Prospección Comercial")
    st.markdown("Gestión de contactos comerciales, seguimiento de ofertas y reuniones de venta.")
    
    total_pipeline = st.session_state.leads["Valor Cotizado (€)"].sum() if not st.session_state.leads.empty else 0.0
    leads_count = len(st.session_state.leads)
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Leads en Negociación", f"{leads_count}")
    c2.metric("Valor Total Ofertas", formato_euro(total_pipeline))
    c3.metric("Ticket Medio / Oportunidad", formato_euro(total_pipeline / leads_count if leads_count > 0 else 0))
    
    st.divider()
    
    st.subheader("📞 Embudo Comercial")
    
    edited_leads = st.data_editor(
        st.session_state.leads,
        num_rows="dynamic",
        use_container_width=True,
        key="editor_leads"
    )
    st.session_state.leads = edited_leads
    
    st.divider()
    
    col_add, col_del = st.columns(2, gap="large")
    
    with col_add:
        with st.expander("➕ Registrar Nueva Oportunidad"):
            with st.form("form_nuevo_lead", clear_on_submit=True):
                prospecto = st.text_input("Empresa / Prospecto")
                contacto = st.text_input("Persona de Contacto")
                email = st.text_input("Email / Teléfono")
                etapa = st.selectbox("Etapa Comercial", ["Contacto Inicial", "Reunión Agendada", "Propuesta Enviada", "Negociación", "Cerrado Ganado", "Cerrado Perdido"])
                valor = st.number_input("Valor Cotizado (€)", value=1500.0, step=100.0)
                fecha_c = st.date_input("Fecha Próximo Seguimiento")
                
                if st.form_submit_button("Guardar en CRM"):
                    if prospecto:
                        nuevo_r = pd.DataFrame([{
                            "Prospecto": prospecto,
                            "Contacto": contacto,
                            "Teléfono / Email": email,
                            "Etapa Comercial": etapa,
                            "Valor Cotizado (€)": valor,
                            "Próximo Contacto": str(fecha_c)
                        }])
                        st.session_state.leads = pd.concat([st.session_state.leads, nuevo_r], ignore_index=True)
                        st.success(f"Prospecto '{prospecto}' guardado.")
                        st.rerun()

    with col_del:
        with st.expander("🗑️ Borrado Rápido de Prospecto"):
            if not st.session_state.leads.empty:
                lead_a_borrar = st.selectbox("Selecciona prospecto a eliminar:", st.session_state.leads["Prospecto"].unique(), key="del_lead_select")
                if st.button("❌ Eliminar Prospecto", key="btn_del_lead_act"):
                    st.session_state.leads = st.session_state.leads[st.session_state.leads["Prospecto"] != lead_a_borrar].reset_index(drop=True)
                    st.success(f"'{lead_a_borrar}' eliminado.")
                    st.rerun()


def mostrar_tareas_proyectos():
    st.title("📋 Tareas & Proyectos (Producción)")
    st.markdown("Módulo operativo para **entregar los trabajos** de los clientes activos.")
    
    proyectos_count = len(st.session_state.proyectos)
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Proyectos Activos", f"{proyectos_count}")
    c2.metric("En Desarrollo", f"{len(st.session_state.proyectos[st.session_state.proyectos['Fase Trabajo'] == 'En Desarrollo'])}")
    c3.metric("Listos para Revisión", f"{len(st.session_state.proyectos[st.session_state.proyectos['Fase Trabajo'] == 'En Revisión'])}")
    
    st.divider()
    
    st.subheader("🚀 Seguimiento de Entregables")
    
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
        with st.expander("➕ Alta de Nuevo Proyecto"):
            with st.form("form_nuevo_proy", clear_on_submit=True):
                nombre_p = st.text_input("Nombre del Servicio / Proyecto")
                cliente_p = st.text_input("Cliente Activo (Cobrado)")
                fase_p = st.selectbox("Fase de Trabajo", ["Planificación", "Diseño Figma", "En Desarrollo", "En Revisión", "Entregado"])
                progreso_p = st.slider("Avance Inicial (%)", 0, 100, 10)
                fecha_p = st.date_input("Fecha de Entrega Prometida")
                resp_p = st.text_input("Responsable Asignado", "Equipo Web")
                
                if st.form_submit_button("Crear Proyecto"):
                    if nombre_p:
                        nuevo_p = pd.DataFrame([{
                            "Proyecto": nombre_p,
                            "Cliente Activo": cliente_p,
                            "Fase Trabajo": fase_p,
                            "Progreso (%)": progreso_p,
                            "Fecha Entrega": str(fecha_p),
                            "Responsable": resp_p
                        }])
                        st.session_state.proyectos = pd.concat([st.session_state.proyectos, nuevo_p], ignore_index=True)
                        st.success(f"Proyecto '{nombre_p}' creado.")
                        st.rerun()

    with col_del_p:
        with st.expander("🗑️ Borrado Rápido de Proyecto"):
            if not st.session_state.proyectos.empty:
                proy_a_borrar = st.selectbox("Selecciona proyecto a eliminar:", st.session_state.proyectos["Proyecto"].unique(), key="select_del_p_act")
                if st.button("❌ Eliminar Proyecto", key="btn_del_p_act"):
                    st.session_state.proyectos = st.session_state.proyectos[st.session_state.proyectos["Proyecto"] != proy_a_borrar].reset_index(drop=True)
                    st.success(f"Proyecto '{proy_a_borrar}' eliminado.")
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
            st.success(f"Factura {num_factura} registrada. ¡Impacta en tus Finanzas!")

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


def mostrar_finanzas():
    st.title("💰 Panel Financiero Transparente")
    st.markdown("Visualización de balances y salud financiera en tiempo real.")
    
    total_ingresos = st.session_state.facturas["Total (€)"].sum() if not st.session_state.facturas.empty else 0.0
    total_gastos = st.session_state.gastos["Importe (€)"].sum() if not st.session_state.gastos.empty else 0.0
    beneficio_neto = total_ingresos - total_gastos
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Ingresos Totales", formato_euro(total_ingresos))
    c2.metric("Gastos Totales", formato_euro(total_gastos), delta_color="inverse")
    c3.metric("Beneficio Neto Real", formato_euro(beneficio_neto))
    
    st.divider()
    
    st.subheader("📊 Comparativa de Balance")
    df_comparativa = pd.DataFrame({
        "Concepto": ["Ingresos Facturados", "Gastos Totales", "Beneficio Neto"],
        "Importe (€)": [total_ingresos, total_gastos, beneficio_neto]
    }).set_index("Concepto")
    
    st.bar_chart(df_comparativa, color="#6366f1")
    
    st.divider()
    
    col_a, col_b = st.columns(2, gap="large")
    
    with col_a:
        st.subheader("📥 Registro de Facturas Emitidas")
        st.dataframe(st.session_state.facturas[["Número", "Cliente", "Total (€)", "Fecha"]], use_container_width=True, hide_index=True)
        
    with col_b:
        st.subheader("📤 Control de Gastos Operativos")
        edited_gastos = st.data_editor(st.session_state.gastos, num_rows="dynamic", use_container_width=True, key="editor_gastos")
        st.session_state.gastos = edited_gastos
        
        with st.expander("🗑️ Borrado Rápido de Gasto"):
            if not st.session_state.gastos.empty:
                gasto_a_borrar = st.selectbox("Selecciona concepto a eliminar:", st.session_state.gastos["Concepto"].unique(), key="select_del_gasto")
                if st.button("❌ Eliminar Gasto", key="btn_del_gasto"):
                    st.session_state.gastos = st.session_state.gastos[st.session_state.gastos["Concepto"] != gasto_a_borrar].reset_index(drop=True)
                    st.success(f"Gasto '{gasto_a_borrar}' eliminado.")
                    st.rerun()

# ==========================================
# MENÚ LATERAL Y NAVEGACIÓN
# ==========================================
with st.sidebar:
    st.markdown("### ⚡ Presencia Web Pro")
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
