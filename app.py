import streamlit as st
from homeworkWizard import generate_feedback
from homeworkWizard import load_student_homework
from homeworkWizard import create_prompt_template

def process_uploaded_file(uploaded_file):
    homework_text = load_student_homework(uploaded_file)
    prompt_template = create_prompt_template()
    feedback = generate_feedback(prompt_template, homework_text)
    return feedback

def main():

    st.set_page_config(page_title="homeWork-WizardX")
    st.title("Feedback Generator")
    st.write("Generate feed back from all your assignments.")

    st.sidebar.header("Upload File")
    uploaded_file = st.sidebar.file_uploader("Choose a file", type=["docx", "pdf", "pptx"])

    if uploaded_file is not None:
        st.sidebar.subheader("File Details:")
        file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
        st.sidebar.write(file_details)

        if st.sidebar.button("Generate Feedback"):
            feedback = process_uploaded_file(uploaded_file)
            st.success("Feedback Generated:")
            st.write(feedback)

if __name__ == "__main__":
    main()
