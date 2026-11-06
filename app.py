import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="EduKlusive AI Co-Teacher", page_icon="🎓", layout="centered")

# Header Section
st.title("🎓 EduKlusive AI Co-Teacher")
st.subheader("Powered by the C.L.A.S.S. Prompting Framework™")
st.markdown("Fill out the C.L.A.S.S. fields below to generate a highly customized, classroom-ready lesson plan or professional document.")

# Sidebar Branding (No API Key input needed)
with st.sidebar:
    st.header("⚙️ App Info")
    st.markdown("This tool utilizes the EduKlusive C.L.A.S.S. Framework to assist educators and professionals.")
    st.markdown("---")
    st.markdown("**EduKlusive Consulting & Services**")

# The C.L.A.S.S. Framework Inputs
st.header("C — Context & Background")
context = st.text_area("What is the current situation, topic, or curriculum standard?")

st.header("L — Lead Persona")
persona = st.selectbox("What expert identity should the AI assume?", 
                      ["Low Income Community Teacher / TFN Fellow", "Master Educator", "Literacy Specialist", "STEM Master Teacher", "Career Coach"])

st.header("A — Action & Audience")
action_audience = st.text_area("What is the exact task, and who will consume it?")

st.header("S — Scope & Constraints")
constraints = st.text_area("What are the strict rules and boundaries?")

st.header("S — Structural Output")
output_format = st.selectbox("How must the final result be formatted?", 
                            ["5-Step Lesson Plan", "3-Column Table", "Rubric Grid", "Bulleted Guide", "Official Memo"])

# Generation Logic
if st.button("🚀 Generate EduKlusive Plan"):
    if not context or not action_audience:
        st.warning("Please fill out at least the Context and Action fields to generate a plan.")
    else:
        try:
            # Automatically retrieve API key from Streamlit Secrets
            api_key = st.secrets["GEMINI_API_KEY"]
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-3.8-flash')
            
            master_prompt = f"""
            You are operating under the EduKlusive C.L.A.S.S. Prompting Framework.
            [C - Context & Background]: {context}
            [L - Lead Persona]: Act as an expert {persona}.
            [A - Action & Audience]: {action_audience}
            [S - Scope & Constraints]: {constraints}
            [S - Structural Output]: Format the response EXACTLY as a {output_format}.
            Execute strictly according to constraints. No generic disclaimers.
            """
            
            with st.spinner("🧠 Generating your EduKlusive plan..."):
                response = model.generate_content(master_prompt)
                
            st.success("✅ Generation Complete!")
            st.markdown("### Your Custom Output:")
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"An error occurred: {e}. Please ensure your GEMINI_API_KEY is configured in Streamlit Cloud Secrets.")
