import streamlit as st

from orchestrator import SyntheticDataOrchestrator

# Configure page metadata and wide screen layout
st.set_page_config(page_title="AI Synthetic Data Generator", layout="wide")

st.title("🤖 AI Synthetic Data Generator")

st.markdown(
    """
Generate complete synthetic datasets from a simple business description.
"""
)

# Multi-line input form for gathering user requirements
user_request = st.text_area(
    "Describe your application",
    height=200,
    placeholder="""Examples:

Hospital Management System
Need synthetic data for QA testing.
Doctors: 100
Patients: 1000
Appointments: 5000""",
)

# Trigger execution on button click
if st.button("Generate Dataset"):

    if not user_request.strip():
        st.warning("Please enter a requirement.")

    else:
        # Show loading indicator while orchestrator processes pipeline
        with st.spinner("Generating..."):
            orchestrator = SyntheticDataOrchestrator()
            result = orchestrator.run(user_request)

        # Clear spinner and show final success components
        st.success("Generation Complete")

        st.subheader("Domain")
        st.write(result["requirements"].get("domain"))

        st.subheader("Generation Plan")
        st.json(result["plan"])

        st.subheader("Tables")
        table_names = [
            table["name"] for table in result["schema"]["tables"]
        ]
        st.write(table_names)

        st.subheader("Relationships")
        st.json(result["relationships"])

        st.subheader("Generation Order")
        st.write(result["generation_order"])

        st.subheader("Validation")
        st.json(result["validation"])

        st.success("CSV files saved in outputs/")