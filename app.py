import streamlit as st

# Asetukset: mobiilioptimoitu asettelu
st.set_page_config(page_title="Hintalaskuri", layout="centered")

st.markdown("""
<style>
    /* 1. PIILOTETAAN + JA - NAPIT KOKONAAN */
    [data-testid="stNumberInputStepUp"], [data-testid="stNumberInputStepDown"] {
        display: none !important;
    }
    
    /* 2. TEHDÄÄN SYÖTTÖKENTÄSTÄ MASSIVINEN */
    input[type="number"] {
        font-size: 2.5rem !important;  /* Jättimäinen teksti */
        font-weight: 800 !important;
        padding: 20px !important;      /* Paksu kenttä, helppo osua sormella */
        text-align: center;
        border-radius: 12px !important;
    }

    /* 3. MOBIILIN REUNUKSET JA YLIMÄÄRÄINEN TILA POIS */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 1rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 500px;
    }
    header, footer {visibility: hidden;}
    
    /* 4. TULOSKORTIT ISOMMAKSI JA KESKITETYKSI */
    .card {
        padding: 20px 15px;
        border-radius: 12px;
        margin-bottom: 15px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .camp-card {
        background-color: #fff0f0;
        border: 2px solid #ffcccc;
    }
    .tax-card {
        background-color: #f0f8ff;
        border: 2px solid #cce5ff;
    }
    .title-text {
        font-size: 1rem;
        color: #555;
        margin-bottom: 5px;
        text-transform: uppercase;
        font-weight: 700;
        letter-spacing: 0.5px;
    }
    .red-price {
        color: #d9383a;
        font-size: 2.2rem;
        font-weight: 900;
        line-height: 1.1;
    }
    .green-price {
        color: #1a7f37;
        font-size: 2.2rem;
        font-weight: 900;
        line-height: 1.1;
    }
    .tax-subtext {
        font-size: 0.85rem;
        color: #666;
        margin-top: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Iso oma otsikko syöttökentälle
st.markdown("<h3 style='text-align: center; color: #333; margin-bottom: -15px;'>Syötä normaali hinta (€)</h3>", unsafe_allow_html=True)

# Syöttökenttä (step=None varmistaa, ettei nappeja ilmesty taustalla)
normaali_hinta = st.number_input(
    "Otsikko piilossa", 
    min_value=0.0, 
    value=1000.0, 
    step=None, 
    label_visibility="collapsed" 
)

# Laskentalogiikka
kampanjahinta = normaali_hinta * 0.85

if kampanjahinta > 150:
    vahennys = (kampanjahinta - 150) * 0.35
else:
    vahennys = 0.0

lopullinen_hinta = kampanjahinta - vahennys

# Kampanjahinta (punaisella)
st.markdown(f"""
<div class="card camp-card">
    <div class="title-text">Kampanjahinta (-15%)</div>
    <div class="red-price">{kampanjahinta:,.2f} €</div>
</div>
""", unsafe_allow_html=True)

# Hinta kotitalousvähennyksellä (vihreällä)
st.markdown(f"""
<div class="card tax-card">
    <div class="title-text">Hinta kotitalousvähennyksellä</div>
    <div class="green-price">{lopullinen_hinta:,.2f} €</div>
    <div class="tax-subtext">Vähennys: -{vahennys:,.2f} € (sis. 150 € omavastuu)</div>
</div>
""", unsafe_allow_html=True)
