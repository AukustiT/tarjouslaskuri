import streamlit as st

# Asetukset: piilotetaan valikot ja tyhjät ylämarginaalit, jotta mahtuu kännykän ruudulle
st.set_page_config(page_title="Hintalaskuri", layout="centered")

st.markdown("""
<style>
    /* Minimaaliset marginaalit mobiilinäkymää varten */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0.5rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 480px;
    }
    #MainMenu, header, footer {visibility: hidden;}
    
    .card {
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    .camp-card {
        background-color: #fff0f0;
        border: 1px solid #ffcccc;
    }
    .tax-card {
        background-color: #f0f8ff;
        border: 1px solid #cce5ff;
    }
    .title-text {
        font-size: 0.85rem;
        color: #555;
        margin-bottom: 2px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .red-price {
        color: #d9383a;
        font-size: 1.8rem;
        font-weight: 700;
        line-height: 1.1;
    }
    .green-price {
        color: #1a7f37;
        font-size: 1.8rem;
        font-weight: 700;
        line-height: 1.1;
    }
    .tax-subtext {
        font-size: 0.75rem;
        color: #666;
        margin-top: 3px;
    }
</style>
""", unsafe_allow_html=True)

# 1. Normaali hinta -syöte
normaali_hinta = st.number_input(
    "Normaali hinta (€)", 
    min_value=0.0, 
    value=1000.0, 
    step=50.0,
    format="%.2f"
)

# 2. Laskentalogiikka
# Kampanjahinta: -15%
kampanjahinta = normaali_hinta * 0.85

# Kotitalousvähennys: 35 % osuudesta, joka ylittää 150 € omavastuun
if kampanjahinta > 150:
    vahennys = (kampanjahinta - 150) * 0.35
else:
    vahennys = 0.0

lopullinen_hinta = kampanjahinta - vahennys

# 3. Kampanjahinta (punaisella)
st.markdown(f"""
<div class="card camp-card">
    <div class="title-text">Kampanjahinta (-15%)</div>
    <div class="red-price">{kampanjahinta:,.2f} €</div>
</div>
""", unsafe_allow_html=True)

# 4. Hinta kotitalousvähennyksellä
st.markdown(f"""
<div class="card tax-card">
    <div class="title-text">Hinta kotitalousvähennyksellä</div>
    <div class="green-price">{lopullinen_hinta:,.2f} €</div>
    <div class="tax-subtext">Vähennys: -{vahennys:,.2f} € (sis. 150 € omavastuu)</div>
</div>
""", unsafe_allow_html=True)
