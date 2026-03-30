import sys, os
sys.path.insert(0, os.path.dirname(__file__))

import streamlit as st
import time

st.set_page_config(
    page_title="IntelGraph | Sovereign Engine",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.stApp {
    background: linear-gradient(135deg, #0a0e1a 0%, #0d1529 40%, #0a1628 100%);
    color: #e2e8f0;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f1923 0%, #111d2e 100%);
    border-right: 1px solid rgba(255,165,0,0.15);
}
[data-testid="stSidebar"] .stMarkdown p { color: #94a3b8; }

.main-header {
    background: linear-gradient(135deg, #0f1923 0%, #1a2744 50%, #0f1923 100%);
    border: 1px solid rgba(255,165,0,0.25);
    border-radius: 16px;
    padding: 2rem 2.5rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}
.main-header::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at 30% 50%, rgba(255,140,0,0.06) 0%, transparent 60%),
                radial-gradient(circle at 70% 50%, rgba(59,130,246,0.06) 0%, transparent 60%);
    pointer-events: none;
}
.main-header h1 { font-size: 2rem; font-weight: 700; color: #f8fafc; margin: 0; letter-spacing: -0.5px; }
.main-header p  { color: #94a3b8; margin: 0.4rem 0 0; font-size: 0.9rem; }
.header-badge {
    display: inline-block;
    background: linear-gradient(135deg, rgba(255,140,0,0.2), rgba(255,140,0,0.05));
    border: 1px solid rgba(255,140,0,0.4);
    color: #ffa500;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 1px;
    margin-bottom: 0.8rem;
}

.agent-stream-container {
    background: rgba(15,25,35,0.8);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px;
    padding: 1.2rem 1.5rem;
    margin-bottom: 1rem;
}
.agent-header {
    display: flex;
    align-items: center;
    gap: 0.7rem;
    margin-bottom: 0.6rem;
}
.agent-badge {
    display: inline-flex;
    align-items: center;
    background: rgba(255,140,0,0.12);
    border: 1px solid rgba(255,140,0,0.3);
    color: #ffa500;
    padding: 3px 10px;
    border-radius: 6px;
    font-size: 0.75rem;
    font-weight: 600;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 0.5px;
}
.agent-log {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    color: #64748b;
    line-height: 1.7;
}
.agent-log .log-line { margin-bottom: 2px; }
.agent-insight {
    font-size: 0.85rem;
    color: #cbd5e1;
    line-height: 1.75;
    margin-top: 0.6rem;
    padding-top: 0.6rem;
    border-top: 1px solid rgba(255,255,255,0.06);
}

.report-container {
    background: linear-gradient(135deg, #0f1923 0%, #121d2e 100%);
    border: 1px solid rgba(255,140,0,0.25);
    border-radius: 16px;
    padding: 2rem 2.5rem;
    position: relative;
    overflow: hidden;
}
.report-container::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 3px;
    background: linear-gradient(90deg, #ff8c00, #3b82f6, #ff8c00);
}
.report-section-header {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 2px;
    color: #ffa500;
    margin: 1.5rem 0 0.4rem;
    padding: 0.3rem 0;
    border-bottom: 1px solid rgba(255,140,0,0.2);
}
.report-section-header:first-child { margin-top: 0; }
.report-body {
    color: #cbd5e1;
    font-size: 0.88rem;
    line-height: 1.85;
    white-space: pre-wrap;
}

.critique-box {
    background: rgba(239,68,68,0.05);
    border: 1px solid rgba(239,68,68,0.25);
    border-left: 3px solid #ef4444;
    border-radius: 8px;
    padding: 1rem 1.2rem;
    margin: 1rem 0;
    font-size: 0.85rem;
    color: #fca5a5;
    line-height: 1.75;
}

.metric-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 10px;
    padding: 1rem;
    text-align: center;
}
.metric-value {
    font-size: 1.6rem;
    font-weight: 700;
    color: #ffa500;
    font-family: 'JetBrains Mono', monospace;
}
.metric-label {
    font-size: 0.72rem;
    color: #64748b;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-top: 0.2rem;
}

.status-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: rgba(34,197,94,0.1);
    border: 1px solid rgba(34,197,94,0.3);
    color: #86efac;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.72rem;
    font-weight: 600;
}
.status-pill.pending {
    background: rgba(234,179,8,0.1);
    border-color: rgba(234,179,8,0.3);
    color: #fde047;
}

.stButton > button {
    background: linear-gradient(135deg, #ff8c00, #e07000) !important;
    color: #000 !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.6rem 2rem !important;
    font-size: 0.9rem !important;
    letter-spacing: 0.5px !important;
    transition: all 0.3s ease !important;
    width: 100% !important;
}
.stButton > button:hover { opacity: 0.9; transform: translateY(-1px); }

.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 8px !important;
    color: #e2e8f0 !important;
}

hr { border-color: rgba(255,255,255,0.07) !important; }
.stSpinner > div > div { border-top-color: #ffa500 !important; }
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(255,140,0,0.3); border-radius: 3px; }
</style>
""", unsafe_allow_html=True)

AGENT_META = {
    "artha":      {"role": "Artha — Economic Affairs",      "color": "#22c55e"},
    "raksha":     {"role": "Raksha — Defence & Security",   "color": "#3b82f6"},
    "shakti":     {"role": "Shakti — Energy & Power",        "color": "#eab308"},
    "yantra":     {"role": "Yantra — Technology & Industry", "color": "#a855f7"},
    "samaj":      {"role": "Samaj — Social Welfare",         "color": "#ec4899"},
    "vikriti":    {"role": "Vikriti — Adversarial Probe",   "color": "#ef4444"},
    "supervisor": {"role": "Samanvaya — Chief Coordinator", "color": "#ffa500"},
}

TASK_META = {
    "Goal":   {"desc": "Long-term national objective analysis & implementation roadmap"},
    "Policy": {"desc": "Policy impact prediction, SWOT & stress-test evaluation"},
    "Crisis": {"desc": "Emergency response, damage control & escalation assessment"},
}


def render_header():
    st.markdown("""
    <div class="main-header">
        <div class="header-badge">CLASSIFIED — SOVEREIGN INTELLIGENCE SYSTEM</div>
        <h1>IntelGraph Sovereign Engine</h1>
        <p>Multi-agent strategic intelligence for India's national policy analysis &amp; decision support</p>
    </div>
    """, unsafe_allow_html=True)


def render_agent_card(name: str, logs: list, insight: str):
    meta = AGENT_META.get(name.lower(), {"role": name, "color": "#94a3b8"})
    is_vikriti = name.lower() == "vikriti"

    log_html = "".join(
        f'<div class="log-line">&gt; {log}</div>' for log in logs
    )

    card_style = "border-left: 3px solid #ef4444;" if is_vikriti else ""
    badge_style = (
        "background:rgba(239,68,68,0.15);border-color:rgba(239,68,68,0.4);color:#fca5a5;"
        if is_vikriti else ""
    )

    st.markdown(f"""
    <div class="agent-stream-container" style="{card_style}">
        <div class="agent-header">
            <span class="agent-badge" style="{badge_style}">{meta['role']}</span>
        </div>
        <div class="agent-log">{log_html}</div>
        {"<div class='critique-box'>" + insight + "</div>" if is_vikriti and insight else
         ("<div class='agent-insight'>" + insight + "</div>" if insight else "")}
    </div>
    """, unsafe_allow_html=True)


def render_report(report: str, task_type: str):
    if not report:
        st.warning("No report was generated.")
        return

    meta = TASK_META.get(task_type, {"desc": ""})
    lines = report.split("\n")
    sections: list[tuple[str, str]] = []
    current_header = None
    buffer: list[str] = []

    for line in lines:
        stripped = line.strip()
        if (stripped.endswith(":") and stripped == stripped.upper()
                and len(stripped) > 3 and not stripped.startswith("HTTP")):
            if current_header is not None:
                sections.append((current_header, "\n".join(buffer).strip()))
            current_header = stripped.rstrip(":")
            buffer = []
        else:
            buffer.append(line)

    if buffer:
        sections.append((current_header or "REPORT", "\n".join(buffer).strip()))

    sections_html = ""
    for header, body in sections:
        if header:
            sections_html += f'<div class="report-section-header">{header}</div>'
        if body:
            sections_html += f'<div class="report-body">{body}</div>'

    st.markdown(f"""
    <div class="report-container">
        <div style="display:flex;align-items:center;gap:0.8rem;margin-bottom:1.5rem;">
            <div>
                <div style="font-size:1rem;font-weight:700;color:#f8fafc;">Strategic Intelligence Report</div>
                <div style="font-size:0.78rem;color:#64748b;margin-top:2px;">{task_type} Mode — {meta['desc']}</div>
            </div>
            <div style="margin-left:auto;" class="status-pill">CLASSIFIED</div>
        </div>
        {sections_html}
    </div>
    """, unsafe_allow_html=True)


with st.sidebar:
    st.markdown("""
    <div style="text-align:center;padding:1.2rem 0 0.5rem;">
        <div style="font-weight:700;font-size:0.95rem;color:#f1f5f9;">IntelGraph</div>
        <div style="font-size:0.72rem;color:#64748b;letter-spacing:1.5px;">SOVEREIGN ENGINE v2026</div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown('<div style="font-size:0.7rem;font-weight:700;color:#64748b;letter-spacing:1.5px;margin-bottom:0.6rem;">MISSION MODE</div>', unsafe_allow_html=True)
    task_type = st.radio(
        "Select Mission Mode",
        options=["Goal", "Policy", "Crisis"],
        label_visibility="collapsed",
        index=0,
    )
    st.markdown(f'<div style="font-size:0.78rem;color:#64748b;margin-top:0.3rem;padding:0.5rem;background:rgba(255,255,255,0.03);border-radius:6px;">{TASK_META[task_type]["desc"]}</div>', unsafe_allow_html=True)

    st.divider()

    st.markdown('<div style="font-size:0.7rem;font-weight:700;color:#64748b;letter-spacing:1.5px;margin-bottom:0.6rem;">ACTIVE AGENTS</div>', unsafe_allow_html=True)
    for key, meta in AGENT_META.items():
        st.markdown(f'<div style="font-size:0.8rem;color:#94a3b8;padding:3px 0;">{meta["role"]}</div>', unsafe_allow_html=True)

    st.divider()

    st.markdown('<div style="font-size:0.7rem;font-weight:700;color:#64748b;letter-spacing:1.5px;margin-bottom:0.4rem;">ENGINE STATUS</div>', unsafe_allow_html=True)
    st.markdown('<div class="status-pill">LLaMA 3.1 — 8B (Groq)</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.68rem;color:#475569;text-align:center;">IntelGraph · Jalwaysontop<br>Strategic Intelligence Division</div>', unsafe_allow_html=True)


render_header()

col_q, col_btn = st.columns([4, 1])

with col_q:
    user_query = st.text_area(
        "Strategic Query",
        placeholder="e.g. How can India achieve 100 GW solar energy by 2030?",
        height=100,
        label_visibility="collapsed",
    )

with col_btn:
    st.markdown("<br>", unsafe_allow_html=True)
    analyze_clicked = st.button("Analyze", use_container_width=True)

sample_prompts = {
    "Goal":   "How can India achieve 100 GW solar energy capacity by 2030?",
    "Policy": "What are the economic impacts of GST reform on small businesses?",
    "Crisis": "India faces a severe drought affecting 40% of agricultural land. Response plan?",
}

st.markdown('<div style="font-size:0.75rem;color:#475569;margin-bottom:0.5rem;">Try a sample query:</div>', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
for col, (mode, prompt) in zip([c1, c2, c3], sample_prompts.items()):
    if col.button(mode, use_container_width=True, key=f"sample_{mode}"):
        st.session_state["sample_query"] = prompt
        st.session_state["sample_task"] = mode
        st.rerun()

if "sample_query" in st.session_state:
    user_query = st.session_state.pop("sample_query")
    task_type  = st.session_state.pop("sample_task")

if analyze_clicked and user_query:
    st.divider()

    m1, m2, m3, m4 = st.columns(4)
    m1.markdown('<div class="metric-card"><div class="metric-value">6</div><div class="metric-label">Active Agents</div></div>', unsafe_allow_html=True)
    m2.markdown(f'<div class="metric-card"><div class="metric-value">{task_type[:3].upper()}</div><div class="metric-label">Mission Mode</div></div>', unsafe_allow_html=True)
    m3.markdown('<div class="metric-card"><div class="metric-value">8B</div><div class="metric-label">LLM Parameters</div></div>', unsafe_allow_html=True)
    m4.markdown('<div class="metric-card"><div class="metric-value status-pill pending">LIVE</div><div class="metric-label">Engine Status</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.7rem;font-weight:700;color:#64748b;letter-spacing:2px;margin-bottom:1rem;">LIVE AGENT INTELLIGENCE STREAM</div>', unsafe_allow_html=True)

    from graph import sutra_engine

    initial_state = {
        "query": user_query,
        "task_type": task_type,
        "messages": [],
        "raw_data": {},
        "agent_insights": {},
        "risk_scores": {},
        "thinking_logs": {},
        "adversary_critique": "",
        "final_report": "",
    }

    agent_placeholders = {}
    agent_order = ["artha", "raksha", "shakti", "yantra", "samaj", "vikriti", "supervisor"]

    for agent in agent_order:
        agent_placeholders[agent] = st.empty()

    final_state_data = None
    start_time = time.time()

    with st.spinner("Sutra Engine is processing your request..."):
        try:
            for output in sutra_engine.stream(initial_state):
                for node_name, value in output.items():
                    agent_key = node_name.lower()
                    logs    = value.get("thinking_logs", {}).get(node_name, [])
                    logs   += value.get("thinking_logs", {}).get(node_name.capitalize(), [])
                    logs   += value.get("thinking_logs", {}).get(agent_key.capitalize(), [])
                    seen = set(); unique_logs = []
                    for l in logs:
                        if l not in seen:
                            seen.add(l); unique_logs.append(l)

                    insight_key_options = [node_name, node_name.capitalize(), agent_key.capitalize()]
                    insight = ""
                    insights_dict = value.get("agent_insights", {})
                    for k in insight_key_options:
                        if k in insights_dict:
                            insight = insights_dict[k]; break

                    if agent_key == "supervisor":
                        final_state_data = value
                        report_preview = value.get("final_report", "")
                        insight = report_preview[:300] + "..." if len(report_preview) > 300 else report_preview
                    elif agent_key == "vikriti":
                        insight = value.get("adversary_critique", insight)

                    with agent_placeholders.get(agent_key, st.empty()):
                        render_agent_card(node_name, unique_logs, insight)

        except Exception as e:
            st.error(f"Engine error: {e}")
            st.stop()

    elapsed = time.time() - start_time

    st.divider()
    st.markdown('<div style="font-size:0.7rem;font-weight:700;color:#64748b;letter-spacing:2px;margin-bottom:1rem;">FINAL STRATEGIC REPORT</div>', unsafe_allow_html=True)

    if final_state_data:
        final_report = final_state_data.get("final_report", "")
        render_report(final_report, task_type)

        st.markdown("<br>", unsafe_allow_html=True)
        col_d1, col_d2, col_d3 = st.columns([2, 1, 2])
        with col_d2:
            st.download_button(
                label="Download Report",
                data=f"INTERGRAPH SOVEREIGN REPORT\nMode: {task_type}\nQuery: {user_query}\n\n{'='*60}\n\n{final_report}",
                file_name=f"intergraph_report_{task_type.lower()}.txt",
                mime="text/plain",
                use_container_width=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)
    s1, s2 = st.columns(2)
    s1.markdown(f'<div class="metric-card"><div class="metric-value">{elapsed:.1f}s</div><div class="metric-label">Total Processing Time</div></div>', unsafe_allow_html=True)
    s2.markdown('<div class="metric-card"><div class="metric-value status-pill">DONE</div><div class="metric-label">Engine Status</div></div>', unsafe_allow_html=True)

elif analyze_clicked and not user_query:
    st.warning("Please enter a strategic query before running the analysis.")

else:
    st.divider()
    st.markdown('<div style="font-size:0.7rem;font-weight:700;color:#64748b;letter-spacing:2px;margin-bottom:1.2rem;">SOVEREIGN CABINET — AGENT ROSTER</div>', unsafe_allow_html=True)

    cols = st.columns(3)
    for i, (key, meta) in enumerate(AGENT_META.items()):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="agent-stream-container" style="text-align:center;padding:1.5rem;">
                <div style="font-weight:600;font-size:0.85rem;color:#e2e8f0">{meta['role']}</div>
                <div style="font-size:0.72rem;color:#64748b;margin-top:0.3rem">
                    {"Adversarial Red-Team Probing" if key=="vikriti" else
                     "Chief Synthesis & Coordination" if key=="supervisor" else
                     "Strategic Intelligence Node"}
                </div>
            </div>
            """, unsafe_allow_html=True)
