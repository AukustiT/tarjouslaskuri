import streamlit as st

st.set_page_config(
    page_title="Hintalaskuri",
    page_icon="💳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    /* 1. Pakotetaan koko sivu mahtumaan yhteen ruutuun ilman skrollia */
    html, body, [data-testid="stAppViewContainer"] {
        height: 100vh;
        max-height: 100dvh;
        overflow: hidden !important;
        background-color: #0f172a !important; /* Elegantti tumma slate-tausta */
        color: #f8fafc;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }

    /* Piilotetaan Streamlitin yläpalkki, footer ja valikkonapit */
    header, footer, #MainMenu, [data-testid="stToolbar"] {
        display: none !important;
    }

    /* Nollataan Streamlitin omat massiiviset paddingit */
    .block-container {
        padding: 1.25rem 1rem !important;
        max-width: 420px !important;
        margin: auto;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 100dvh;
        box-sizing: border-box;
    }

    /* 2. Poistetaan Streamlitin omat + / - napit kokonaan */
    [data-testid="stNumberInputStepUp"], 
    [data-testid="stNumberInputStepDown"],
    input[type=number]::-webkit-inner-spin-button, 
    input[type=number]::-webkit-outer-spin-button {
        display: none !important;
        -webkit-appearance: none !important;
        margin: 0 !important;
    }

    /* 3. Iso, puhdas syöttökenttä */
    [data-testid="stTextInputRootElement"], [data-testid="stNumberInputRootElement"] {
        background: transparent !important;
        border: none !important;
    }
    
    div[data-baseweb="input"] {
        background-color: #1e293b !important;
        border: 1px solid #334155 !important;
        border-radius: 18px !important;
        padding: 6px 12px !important;
        transition: all 0.2s ease;
    }

    div[data-baseweb="input"]:focus-within {
        border-color: #38bdf8 !important;
        box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2) !important;
    }

    input[type="number"] {
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        color: #f8fafc !important;
        text-align: center !important;
        padding: 10px 0 !important;
        letter-spacing: -1px;
    }

    /* 4. Tulostuskortit */
    .card-wrap {
        display: flex;
        flex-direction: column;
        gap: 12px;
        margin-top: 14px;
        margin-bottom: 10px;
    }

    .promo-card {
        background: linear-gradient(145deg, #2a1215 0%, #1c0a0c 100%);
        border: 1px solid rgba(244, 63, 94, 0.3);
        border-radius: 20px;
        padding: 18px 20px;
        position: relative;
    }

    .deduct-card {
        background: linear-gradient(145deg, #0d2818 0%, #06180e 100%);
        border: 1px solid rgba(34, 197, 94, 0.35);
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
    }

    .card-label {
        font-size: 0.78rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 4px;
    }

    .promo-label { color: #fb7185; }
    .deduct-label { color: #4ade80; }

    .price-promo {
        font-size: 2.2rem;
        font-weight: 900;
        color: #f43f5e;
        line-height: 1.05;
        letter-spacing: -0.5px;
    }

    .price-deduct {
        font-size: 2.6rem;
        font-weight: 900;
        color: #22c55e;
        line-height: 1.05;
        letter-spacing: -1px;
    }

    .badge {
        display: inline-block;
        padding: 3px 8px;
        border-radius: 999px;
        font-size: 0.7rem;
        font-weight: 800;
        float: right;
    }

    .badge-promo { background: rgba(244, 63, 94, 0.2); color: #f43f5e; }
    .badge-deduct { background: rgba(34, 197, 94, 0.2); color: #4ade80; }

    .info-subtext {
        font-size: 0.8rem;
        color: #94a3b8;
        margin-top: 8px;
        display: flex;
        justify-content: space-between;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        padding-top: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Yläotsikko
st.markdown("""
<div style="text-align: center; margin-top: 4px; margin-bottom: 8px;">
    <span style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; color: #64748b; font-weight: 700;">Syötä hinta</span>
</div>
""", unsafe_allow_html=True)

# Yksinkertainen, suuri syöttökenttä
normaali = st.number_input(
    label="Hinta",
    min_value=0.0,
    value=1200.0,
    step=None,
    label_visibility="collapsed"
)

# Laskentalogiikka
kampanjahinta = normaali * 0.85

if kampanjahinta > 150:
    vahennys = (kampanjahinta - 150) * 0.35
else:
    vahennys = 0.0

maksettava = kampanjahinta - vahennys

# Kortit
st.markdown(f"""
<div class="card-wrap">
    <!-- Kampanjakortti -->
    <div class="promo-card">
        <div>
            <span class="card-label promo-label">Kampanjahinta</span>
            <span class="badge badge-promo">-15%</span>
        </div>
        <div class="price-promo">{kampanjahinta:,.2f}&nbsp;€</div>
    </div>

    <!-- Kotitalousvähennyskortti -->
    <div class="deduct-card">
        <div>
            <span class="card-label deduct-label">Lopullinen oma osuus</span>
            <span class="badge badge-deduct">Kotitalousvähennys</span>
        </div>
        <div class="price-deduct">{maksettava:,.2f}&nbsp;€</div>
        <div class="info-subtext">
            <span>Vähennyksen osuus</span>
            <strong style="color: #cbd5e1;">-{vahennys:,.2f} €</strong>
        </div>
        <div class="info-subtext" style="border: none; padding-top: 2px; margin-top: 0;">
            <span>Omavastuu huomioitu</span>
            <span style="color: #64748b;">150,00 €</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
