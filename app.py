import streamlit as st

# Asetukset: Mobiiliystävällinen ja siisti asettelu
st.set_page_config(page_title="Hintalaskuri", layout="centered")

# Alustetaan muuttuja, jotta kenttä on oletuksena TYHJÄ
if "hinta" not in st.session_state:
    st.session_state.hinta = None

# Funktio, joka tyhjentää kentän
def tyhjenna():
    st.session_state.hinta = None

# Turvallinen CSS
st.markdown("""
<style>
    #MainMenu, header, footer {visibility: hidden;}
    
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 480px;
    }

    input[type="number"]::-webkit-inner-spin-button, 
    input[type="number"]::-webkit-outer-spin-button {
        -webkit-appearance: none;
        margin: 0;
    }
    
    input[type="number"] {
        -moz-appearance: textfield;
        font-size: 2.2rem !important;
        text-align: center !important;
        font-weight: 800 !important;
        height: 75px !important;
        border-radius: 16px !important;
    }

    /* Tyylikäs tyhjennysnappi mobiiliin */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 50px;
        font-weight: 700;
        font-size: 1rem;
        background-color: transparent;
        border: 1px solid #475569;
        color: #94a3b8;
        margin-bottom: 20px;
        transition: all 0.2s;
    }
    .stButton > button:active {
        background-color: #334155;
        color: white;
    }

    .promo-card {
        background-color: #1a0f14;
        border: 1px solid #e11d48;
        border-radius: 16px;
        padding: 22px;
        margin-bottom: 16px;
        color: #ffffff;
        box-shadow: 0 4px 15px rgba(225, 29, 72, 0.08);
    }

    .deduct-card {
        background-color: #06180e;
        border: 1px solid #16a34a;
        border-radius: 16px;
        padding: 22px;
        color: #ffffff;
        box-shadow: 0 4px 15px rgba(22, 163, 74, 0.08);
    }

    .card-title {
        font-size: 0.85rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }

    .promo-title { color: #fb7185; }
    .deduct-title { color: #4ade80; }

    .price {
        font-size: 2.8rem;
        font-weight: 900;
        margin: 5px 0;
        line-height: 1.1;
        letter-spacing: -1px;
    }
    
    .promo-price { color: #f43f5e; }
    .deduct-price { color: #22c55e; }

    .sub-info {
        font-size: 0.85rem;
        color: #94a3b8;
        display: flex;
        justify-content: space-between;
        margin-top: 14px;
        padding-top: 14px;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div style='text-align: center; color: #64748b; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px;'>Syötä normaali hinta (€)</div>", unsafe_allow_html=True)

# Itse syöttökenttä, linkitetty session_stateen (aloittaa aina tyhjänä)
normaali = st.number_input(
    label="Hinta",
    min_value=0.0,
    step=1.0,
    placeholder="Esim. 1500",
    label_visibility="collapsed",
    key="hinta"
)

# Nollaa-nappi syöttökentän alle
st.button("🔄 Nollaa kenttä", on_click=tyhjenna)

# Laskennat näytetään vain, jos kentässä on joku luku
if normaali is not None and normaali > 0:
    kampanjahinta = normaali * 0.85

    if kampanjahinta > 150:
        vahennys = (kampanjahinta - 150) * 0.35
    else:
        vahennys = 0.0

    maksettava = kampanjahinta - vahennys

    st.markdown(f"""
    <div class="promo-card">
        <div class="card-title promo-title">Kampanjahinta (-15%)</div>
        <div class="price promo-price">{kampanjahinta:,.2f} €</div>
    </div>

    <div class="deduct-card">
        <div class="card-title deduct-title">Lopullinen hinta</div>
        <div class="price deduct-price">{maksettava:,.2f} €</div>
        <div class="sub-info">
            <span>Kotitalousvähennys</span>
            <strong style="color: #f8fafc;">-{vahennys:,.2f} €</strong>
        </div>
        <div class="sub-info" style="border: none; padding-top: 6px; margin-top: 0;">
            <span>Omavastuu huomioitu</span>
            <span style="color: #cbd5e1;">150,00 €</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
