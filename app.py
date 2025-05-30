
import streamlit as st
import base64
from PIL import Image

# --- Αρχική Σελίδα (Πριν από τα Tabs) ---
st.title("Ψηφιακή Εφαρμογή Κατανομής Μαθητών Α’ Δημοτικού")
st.markdown("""
<center>
    «Για μια Παιδεία που βλέπει το Φως στα Παιδιά,<br>
    ακόμη κι εκεί όπου άλλοι βλέπουν Σκιές.»
</center>

<center>
    Δημιουργός: Παναγιώτα Γιαννιτσάρου  
    Email: yiannitsaroupanayiota.katanomi@gmail.com  
    Έκδοση Πιλοτική — 2025
</center>
""", unsafe_allow_html=True)

# --- Tabs Εισαγωγής ---
intro1, intro2 = st.tabs(["🎯 Σκοπός της Εφαρμογής", "🧭 Πηγή Έμπνευσης"])

with intro1:
    st.markdown("""
    Η εφαρμογή στοχεύει στη δίκαιη και παιδαγωγικά ισορροπημένη κατανομή μαθητών.
    """)

with intro2:
    st.markdown("""
    Το παιδί δεν είναι απλώς ένα όνομα σε λίστα. Είναι ψυχή, ομάδα, παρουσία.
    """)

# --- Tab 2: Κατανομή Μαθητών ---
st.header("🧮 Tab 2 – Κατανομή Μαθητών")

uploaded_file = st.file_uploader("Ανέβασε το αρχείο Excel", type=[".xlsx"])

if uploaded_file:
    st.success("Το αρχείο ανέβηκε με επιτυχία!")
    st.markdown("Προεπισκόπηση αρχείου (ενδεικτικά):")
    import pandas as pd
    df = pd.read_excel(uploaded_file)
    st.dataframe(df.head())

    if st.button("Εκτέλεση Κατανομής"):
        st.info("[Η λογική κατανομής θα εφαρμοστεί εδώ]")
        st.success("Η κατανομή ολοκληρώθηκε επιτυχώς!")
        st.download_button("Κατέβασε Αρχείο Κατανομής (Excel)", data=b"", file_name="katanomi.xlsx")

# --- Tab 3: Συχνές Ερωτήσεις (FAQ) ---
st.header("📚 Tab 3 – Συχνές Ερωτήσεις (FAQ)")
st.markdown("""
**1. Πώς ανεβάζω το αρχείο Excel;**  
Μέσα από την καρτέλα «Κατανομή Μαθητών», υπάρχει επιλογή «Ανέβασε το αρχείο Excel».

**2. Ποιες είναι οι αποδεκτές τιμές στα πεδία;**  
Όλες οι τιμές πρέπει να είναι με ελληνικά κεφαλαία: Ν (Ναι), Ο (Όχι), Α (Αγόρι), Κ (Κορίτσι).

**3. Πόσα τμήματα δημιουργεί η εφαρμογή;**  
Η εφαρμογή υπολογίζει αυτόματα πόσα τμήματα χρειάζονται, με μέγιστο 25 μαθητές ανά τμήμα.

**4. Ποια είναι τα στάδια κατανομής;**  
1. Παιδιά Εκπαιδευτικών  
2. Ζωηροί Μαθητές  
3. Παιδιά με Ιδιαιτερότητες  
4. Παιδιά με Γλωσσική Αδυναμία  
5. Αμοιβαίες Φιλίες  
6. Υπόλοιποι Μαθητές

**5. Πώς λειτουργούν οι φιλίες και οι συγκρούσεις;**  
– Φιλία λαμβάνεται υπόψη μόνο αν είναι αμοιβαία.  
– Συγκρούσεις: Οι μαθητές δεν θα τοποθετηθούν στο ίδιο τμήμα.

**6. Τι σημαίνει ισορροπία φύλου με ανοχή ±3;**  
Η εφαρμογή εξασφαλίζει ότι η διαφορά αγοριών-κοριτσιών ανά τμήμα δεν ξεπερνά τους 3.

**7. Πώς κατεβάζω τα αποτελέσματα;**  
Μόλις ολοκληρωθεί η κατανομή, εμφανίζεται κουμπί «Κατέβασε Αρχείο Κατανομής».

**8. Ποιος έχει δικαίωμα χρήσης;**  
Η χρήση επιτρέπεται μόνο με ρητή γραπτή άδεια από τη δημιουργό.

**📄 Αρχεία Υποστήριξης:**
- [Πρότυπο Κενό.xlsx](#)
- [Παράδειγμα.xlsx](#)
""")

# --- Tab 4: Επικοινωνία ---
st.header("📬 Tab 4 – Επικοινωνία")
st.markdown("""
**Email δημιουργού:** yiannitsaroupanayiota.katanomi@gmail.com  
**Υπογραφή:** Παναγιώτα Γιαννιτσάρου  
📣 *Δήλωση για πιλοτική λειτουργία*  
⚖️ *Νομική επισήμανση:*  
– Απαγορεύεται η χρήση χωρίς ρητή άδεια  
– Όλα τα δικαιώματα ανήκουν στη δημιουργό
""")

# --- Λογότυπο κάτω κεντρικά ---
with open("ef0084f5-8d56-46fb-a67c-250997f72f5c.png", "rb") as img_file:
    encoded = base64.b64encode(img_file.read()).decode()

st.markdown(
    f"""
    <div style='position:fixed; bottom:10px; left:50%; transform:translateX(-50%);'>
        <img src='data:image/png;base64,{encoded}' width='130'>
    </div>
    """, unsafe_allow_html=True
)
