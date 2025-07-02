import streamlit as st
import json
from datetime import date

st.set_page_config(page_title="AI Credit Memo Generator", layout="wide")
st.title("🧠 AI Credit Memo Generator")

st.markdown("""
Upload a borrower profile JSON and generate a structured credit memo for internal or investor use.
""")

uploaded_file = st.file_uploader("📂 Upload Borrower JSON File", type="json")

if uploaded_file:
    data = json.load(uploaded_file)
    borrower_name = uploaded_file.name.replace(".json", "")

    st.header(f"📄 Credit Memo: {borrower_name}")

    # 1. Executive Summary
    decision = data['lending_risk']['decision']
    dscr = data['lending_risk'].get('dscr', 'N/A')
    cashflow = data['cashflow'].get('sustainability', 'N/A')
    st.subheader("1. Executive Summary")
    st.markdown(f"""
    - **Decision**: `{decision}`
    - **DSCR**: `{dscr}`
    - **Cash Flow Sustainability**: `{cashflow}`
    - **Date**: {date.today().strftime('%B %d, %Y')}
    """)

    # 2. Risk & Red Flags
    st.subheader("2. Identified Risk Flags")
    red_flags = []
    yellow_flags = []
    for section, content in data.items():
        for f in content.get("flags", []):
            if "⚠️" in f:
                red_flags.append(f"[{section.upper()}] {f}")
            elif "🟡" in f:
                yellow_flags.append(f"[{section.upper()}] {f}")

    if red_flags:
        st.error("🔴 Red Flags")
        for f in red_flags:
            st.markdown(f"- {f}")
    if yellow_flags:
        st.warning("🟡 Yellow Flags")
        for f in yellow_flags:
            st.markdown(f"- {f}")

    # 3. Strengths & Weaknesses (inferred)
    st.subheader("3. Strengths & Weaknesses")
    strengths = []
    weaknesses = []
    if dscr and isinstance(dscr, (int, float)):
        if dscr >= 2:
            strengths.append("Strong debt servicing capability")
        elif dscr < 1.2:
            weaknesses.append("DSCR near or below threshold")
    if cashflow == "Strong":
        strengths.append("Consistent operating cash flows")
    if "Inventory" in str(red_flags):
        weaknesses.append("Inventory management mismatch")

    st.markdown("**✅ Strengths**")
    for s in strengths:
        st.markdown(f"- {s}")

    st.markdown("**⚠️ Weaknesses**")
    for w in weaknesses:
        st.markdown(f"- {w}")

    # 4. Recommendation
    st.subheader("4. Lending Recommendation")
    if decision == "APPROVE":
        st.success("This borrower is suitable for lending based on current indicators. Proceed with documentation.")
    elif decision == "CONDITIONAL":
        st.warning("Conditional approval. Recommend adding covenants or partial disbursement tied to performance milestones.")
    else:
        st.error("Reject lending at this stage. Borrower fails minimum thresholds across key dimensions.")

else:
    st.info("Upload a borrower profile JSON to generate a memo.")
