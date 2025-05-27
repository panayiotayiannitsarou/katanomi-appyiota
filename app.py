
import streamlit as st
import base64
from PIL import Image

# --- Υποκαρτέλα 1: Σκοπός Εφαρμογής ---
st.header("🎯 Σκοπός της Εφαρμογής")
st.markdown("""
Η εφαρμογή στοχεύει στη δίκαιη και παιδαγωγικά ισορροπημένη κατανομή μαθητών.
""")

# --- Υποκαρτέλα 2: Πηγή Έμπνευσης ---
st.header("🧭 Η Ιστορία της Δημιουργίας & Πηγή Έμπνευσης")
st.markdown("""
Το παιδί δεν είναι απλώς ένα όνομα σε λίστα. Είναι ψυχή, ομάδα, παρουσία.
""")

# --- Τέλος Tabs 1–4 ---
with open("logo.png", "rb") as img_file:
    encoded = base64.b64encode(img_file.read()).decode()

st.markdown(
    f"""
    <div style='position:fixed; bottom:10px; left:50%; transform:translateX(-50%);'>
        <img src='data:image/png;base64,{encoded}' width='130'>
    </div>
    """, unsafe_allow_html=True
)
