import streamlit as st

# Asetukset: Mobiiliystävällinen ja siisti asettelu
st.set_page_config(page_title="Hintalaskuri", layout="centered")

# Turvallinen CSS, joka EI riko Streamlitin omaa dark/light -modea tai rullausta
st.markdown("""
<style>
    /* Piilotetaan turhat yläpalkit ja valikot */
    #MainMenu, header, footer {visibility: hidden;}
    
    /* Mobiilille sopivat fiksut marginaalit */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 480px;
    }

    /* 1. PIILOTETAAN + JA - NAPIT TURVALLISESTI */
    input[type="number"]::-webkit-inner-spin-button, 
    input[type="number"]::-webkit-outer-spin-button {
        -webkit-appearance: none;
        margin: 0;
    }
    
    /* 2. TEHDÄÄN SYÖTTÖKENTÄSTÄ ISO JA CLEAN */
    input[type="number"] {
        -moz-appearance: textfield;
        font-size: 2.2rem !important; /* Erittäin iso teksti */
        text-align: center !important;
        font-weight: 800 !important;
        height: 75px !important;      /* Paksu kenttä, mihin on helppo osua */
        border-radius: 16px !important;
    }

    /* 3. FINTECH-KORTIT (Toimivat aina täydellisesti teemasta riippumatta) */
    .promo-card {
        background-color: #1a0f14; /* Tummansävyinen tausta */
        border: 1px solid #e11d48;
        border-radius: 16px;
        padding: 22px;
        margin-bottom: 16px;
        color: #ffffff; /* Pakotettu valkoinen teksti kortin sisälle */
        box-shadow: 0 4px 15px rgba(225, 29, 72, 0.08);
    }

    .deduct-card {
        background-color: #06180e; /* Tummanvihreä tausta */
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

# Pieni ohjeteksti syöttökentän päälle
st.markdown("<div style='text-align: center; color: #64748b; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px;'>Syötä normaali hinta (€)</div>", unsafe_allow_html=True)

# Itse syöttökenttä (Nyt Streamlit hoitaa dark/light moden värit oikein automaattisesti)
normaali = st.number_input(
    label="Hinta",
    min_value=0.0,
    value=1000.0,
    step=1.0,  # step=None saattaa rikkoa syöttökentän joillain selaimilla, 1.0 on turvallinen
    label_visibility="collapsed"
)

# Laskennat
kampanjahinta = normaali * 0.85

if kampanjahinta > 150:
    vahennys = (kampanjahinta - 150) * 0.35
else:
    vahennys = 0.0

maksettava = kampanjahinta - vahennys

# Tulokset hienoissa Fintech-korteissa
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
