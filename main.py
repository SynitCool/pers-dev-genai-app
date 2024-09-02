import streamlit as st
from PIL import Image

from generate import generate_output

from utils import create_pdf_file
from utils import create_information_retrieval
from utils import create_feedback_prompt
from utils import create_content_curation_recommendation_prompt
from utils import create_development_opportunities_prompt
from utils import create_evaluation_prompt
from utils import create_learning_path_prompt
from utils import create_skill_gap_prompt
from utils import create_talent_insight_prompt


st.set_page_config(page_title="Personalized Development GenAI App", layout="wide")
st.title("Personalized Development GenAI App")

owner = "Tidak ada nama"
posisi = "Tidak ada posisi"

col1, col2, col3 = st.columns([1, 2, 1])
#-------------------------------
if 'response' not in st.session_state:
    st.session_state.response = "NO ANSWER"


if 'hardskill' not in st.session_state:
    st.session_state.hardskill = []

def remove_hardskill(index):
    if 0 <= index < len(st.session_state.hardskill):
        st.session_state.hardskill.pop(index)
#-------------------------------
if 'softskill' not in st.session_state:
    st.session_state.softskill = []

def remove_softskill(index):
    if 0 <= index < len(st.session_state.softskill):
        st.session_state.softskill.pop(index)
# -------------------------------
if 'keluhan' not in st.session_state:
    st.session_state.keluhan = []

def remove_keluhan(index):
    if 0 <= index < len(st.session_state.keluhan):
        st.session_state.keluhan.pop(index)

# ----------------------- 

def softskill_input():
    # Display a header inside the container
    st.header('Softskill')

    # Create an input box for user text input
    user_input = st.text_input('Softskill yang sudah dikuasai:')

    # Create a slider for rating from 1 to 10
    rating = st.slider('Seberapa baik softskillmu', min_value=0, max_value=10, value=5)

    # Add a button to submit the input and rating
    if st.button('Tambahkan softskill'):
        # Add the user input and rating to the list
        if user_input:
            st.session_state.softskill.append((user_input, rating))
            st.success('softskill sudah ditambahkan!')
        else:
            st.warning('Mohon isi sesuai dengan softskill yang dimiliki anda!')

    st.subheader('softskill yang dimiliki')
    with st.expander('softskill', expanded=False):
        if st.session_state.softskill:
            for i, softskill in enumerate(st.session_state.softskill):
                col1_softskill, col2_softskill = st.columns([6, 1])
                with col1_softskill:
                    st.write(f"**softskill**: {softskill[0]}  | {softskill[1]}")
                with col2_softskill:
                    if st.button('X', key=f'remove_softskill_{i}'):
                        remove_softskill(i)
                        st.rerun()
        else:
            st.write('Tidak ada softskill.')

def keluhan_input():
    # Display a header inside the container
    st.header('Keluhan')

    # Create an input box for user text input
    user_input = st.text_input('Keluhan:')

    # Create a slider for rating from 1 to 10
    rating = st.slider('Seberapa parah keluhanmu', min_value=0, max_value=10, value=5)

    # Add a button to submit the input and rating
    if st.button('Tambahkan keluhan'):
        # Add the user input and rating to the list
        if user_input:
            st.session_state.keluhan.append((user_input, rating))
            st.success('Keluhan sudah ditambahkan!')
        else:
            st.warning('Mohon isi sesuai dengan keluhan yang dimiliki anda!')

    st.subheader('Keluhan yang dimiliki')
    with st.expander('Keluhan', expanded=False):
        if st.session_state.keluhan:
            for i, keluhan in enumerate(st.session_state.keluhan):
                col1_keluhan, col2_keluhan = st.columns([6, 1])
                with col1_keluhan:
                    st.write(f"**Keluhan**: {keluhan[0]}  | {keluhan[1]}")
                with col2_keluhan:
                    if st.button('X', key=f'remove_keluhan_{i}'):
                        remove_keluhan(i)
                        st.rerun()
        else:
            st.write('Tidak ada keluhan.')

def hardskill_input():
    # Display a header inside the container
    st.header('Hardskill')

    # Create an input box for user text input
    user_input = st.text_input('Hardskill yang sudah dikuasai:')

    # Create a slider for rating from 1 to 10
    rating = st.slider('Seberapa baik hardskillmu', min_value=0, max_value=10, value=5)

    # Add a button to submit the input and rating
    if st.button('Tambahkan Hardskill'):
        # Add the user input and rating to the list
        if user_input:
            st.session_state.hardskill.append((user_input, rating))
            st.success('Hardskill sudah ditambahkan!')
        else:
            st.warning('Mohon isi sesuai dengan hardskill yang dimiliki anda!')

    st.subheader('Hardskill yang dimiliki')
    with st.expander('Hardskill', expanded=False):
        if st.session_state.hardskill:
            for i, hardskill in enumerate(st.session_state.hardskill):
                col1_hardskill, col2_hardskill = st.columns([6, 1])
                with col1_hardskill:
                    st.write(f"**Hardskill**: {hardskill[0]}  | {hardskill[1]}")
                with col2_hardskill:
                    if st.button('X', key=f'remove_hardskill_{i}'):
                        remove_hardskill(i)
                        st.rerun()
        else:
            st.write('Tidak ada Hardskill.')

with col1:
    with st.container(border=True):
        owner = st.text_input('Nama Anda:')
        st.write(f"Nama: {owner}")
        posisi = st.radio(
            "Pilih posisi", 
            ("Software Engineer", "Project Manager", "Lecture"))
        st.write(f"Posisi: {posisi}")
    with st.container(border=True):
        hardskill_input()
    with st.container(border=True):
        softskill_input()
    with st.container(border=True):
        keluhan_input()
        

with col2:
    with st.container(border=True):
        # Display a header inside the container
        st.header('AI Answer')
        st.write(st.session_state.response)

with col3:
    with st.container(border=True):
        if posisi != "Tidak ada posisi":
            if st.button('Learning Path'):
                information_text = create_information_retrieval(
                    owner, 
                    posisi, 
                    st.session_state.hardskill, 
                    st.session_state.softskill, 
                    st.session_state.keluhan
                    )
                
                pdf_path = create_pdf_file(information_text, "temp")
                st.session_state.response = generate_output(pdf_path, create_learning_path_prompt(owner, posisi))
                st.rerun()
            if st.button('Skill Gap'):
                information_text = create_information_retrieval(
                    owner, 
                    posisi, 
                    st.session_state.hardskill, 
                    st.session_state.softskill, 
                    st.session_state.keluhan
                    )
                
                pdf_path = create_pdf_file(information_text, "temp")
                st.session_state.response = generate_output(pdf_path, create_skill_gap_prompt(owner, posisi))
                st.rerun()
            if st.button('Feedback'):
                information_text = create_information_retrieval(
                    owner, 
                    posisi, 
                    st.session_state.hardskill, 
                    st.session_state.softskill, 
                    st.session_state.keluhan
                )
                
                pdf_path = create_pdf_file(information_text, "temp")
                st.session_state.response = generate_output(pdf_path, create_feedback_prompt(owner, posisi))
                st.rerun()
            if st.button('Evaluation'):
                information_text = create_information_retrieval(
                    owner, 
                    posisi, 
                    st.session_state.hardskill, 
                    st.session_state.softskill, 
                    st.session_state.keluhan
                    )
                
                pdf_path = create_pdf_file(information_text, "temp")
                st.session_state.response = generate_output(pdf_path, create_evaluation_prompt(owner, posisi))
                st.rerun()
            if st.button('Content Curation & Recommendation'):
                information_text = create_information_retrieval(
                    owner, 
                    posisi, 
                    st.session_state.hardskill, 
                    st.session_state.softskill, 
                    st.session_state.keluhan
                    )
                
                pdf_path = create_pdf_file(information_text, "temp")
                st.session_state.response = generate_output(
                    pdf_path, create_content_curation_recommendation_prompt(owner, posisi)
                )
                st.rerun()
            if st.button('Talent Insight'):
                information_text = create_information_retrieval(
                    owner, 
                    posisi, 
                    st.session_state.hardskill, 
                    st.session_state.softskill, 
                    st.session_state.keluhan
                    )
                
                pdf_path = create_pdf_file(information_text, "temp")
                st.session_state.response = generate_output(pdf_path, create_talent_insight_prompt(owner, posisi))
                st.rerun()
            if st.button('Development Opportunities'):
                information_text = create_information_retrieval(
                    owner, 
                    posisi, 
                    st.session_state.hardskill, 
                    st.session_state.softskill, 
                    st.session_state.keluhan
                    )
                
                pdf_path = create_pdf_file(information_text, "temp")
                st.session_state.response = generate_output(
                    pdf_path, create_development_opportunities_prompt(owner, posisi)
                    )
                st.rerun()
