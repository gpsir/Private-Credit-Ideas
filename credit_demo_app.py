
import streamlit as st
import json
from unified_decision_engine import unified_decision_engine

st.set_page_config(page_title="Private Credit AI Engine", layout="wide")
st.title("📊 Private Credit Underwriting Demo")

st.markdown("""
This app runs the unified decision engine on real or simulated borrower profiles.
Select a borrower profile to load their data, run the engine, and view the underwriting decision.
""")

uploaded_file = st.file_uploader("📂 Upload Borrower JSON Profile", type=["json"])

if uploaded_file:
    borrower_data = json.load(uploaded_file)

    st.subheader("📥 Borrower Profile Loaded")
    st.json(borrower_data)

    if st.button("🚀 Run Credit Engine"):
        output = unified_decision_engine(borrower_data)

        st.subheader("✅ Underwriting Decision")
        st.write(f"**Decision:** {output['final_decision']}")
        st.write(f"**Red Flags:** {output['red_flags']} | **Yellow Flags:** {output['yellow_flags']}")

        st.markdown("---")
        st.subheader("⚠️ Flags Summary")
        for flag in output['flag_summary']:
            st.markdown(f"- {flag}")

        st.markdown("---")
        st.success("You can now export this summary or try with another profile.")

else:
    st.info("Please upload a borrower JSON file to begin.")
