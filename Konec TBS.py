import streamlit as st

st.set_page_config(page_title="Trouble shooting", page_icon="🔧")

st.title("Trouble shooting Tool")

if "step" not in st.session_state:
    st.session_state.step = 0
if "code" not in st.session_state:
    st.session_state.code = None


if st.session_state.code is not None:

    code = st.session_state.code

    st.success(f"Diagnosis Code: {code}")

    if code == 1:
        st.write("AP / Internet issue")

    elif code == 2:
        st.write("Check Automation")

    elif code == 3:
        st.write("IP Issue")

    elif code == 4:
        st.write("IP Issue")

    elif code == 5:
        st.write("Internet Issue")

    elif code == 6:
        st.write("Cooktop damage not switch related issue")

    elif code == 7:
        st.write("Switch damage please contact professional for repair or replacement")

    elif code == 8:
        st.write("Please open the breaker")

    elif code == 9999999:
        st.write("Done!")
    
    else:
        st.write("Pending, waiting for update")

    if st.button("Restart"):
        st.session_state.step = 0
        st.session_state.code = None
        st.rerun()

    st.stop()

def next_step(step):
    st.session_state.step = step
    st.rerun()

# Select Product
if st.session_state.step == 0:

    st.subheader("Select the problematic device")

    col1, col2, col3, col4, col5 = st.columns(5)

    if col1.button("Switch"):
        next_step(1)

    if col2.button("Lock"):
        next_step(501)

    if col3.button("HPS"):
        next_step(1001)

    if col4.button("GPO"):
        next_step(1501)

    if col5.button("AC Gateway"):
        next_step(2001)


# Switch 
# Step 1 Which Switch
if st.session_state.step == 1:

    st.subheader("Which switch is experiencing the problem?")

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    if col1.button("Entry"):
        next_step(2)

    if col2.button("Bathroom"):
        next_step(101)

    if col3.button("Kitchen"):
        next_step(201)

    if col4.button("Cooktop"):
        next_step(301)

    if col5.button("Desk"):
        next_step(401)

    st.write("")

    if col6.button("Back", key="black_btn"):
        next_step(0)


# Entry Switch Common Issue
elif st.session_state.step == 2:

    st.subheader("Common Issue")

    col1, col2, col3, col4 = st.columns(4)

    if col1.button("Issue1", key="red_btn"):
        st.session_state.code = 8000000
        st.rerun()

    if col2.button("Issue2", key="green_btn"):
        st.session_state.code = 8000000
        st.rerun()

    if col3.button("Issue3"):
        st.session_state.code = 8000000
        st.rerun()

    if col4.button("Back", key="black_btn"):
        next_step(1)

# Bathroom Switch Common Issue
elif st.session_state.step == 101:

    st.subheader("Common Issue")

    col1, col2, col3, col4 = st.columns(4)

    if col1.button("Issue1"):
        st.session_state.code = 8000000
        st.rerun()

    if col2.button("Issue2"):
        st.session_state.code = 8000000
        st.rerun()

    if col3.button("Issue3"):
        st.session_state.code = 8000000
        st.rerun()

    if col4.button("Back", key="black_btn"):
        next_step(1)

# Kitchen Switch Common Issue
elif st.session_state.step == 201:

    st.subheader("Common Issue")

    col1, col2, col3, col4 = st.columns(4)

    if col1.button("Issue1"):
        st.session_state.code = 8000000
        st.rerun()

    if col2.button("Issue2"):
        st.session_state.code = 8000000
        st.rerun()

    if col3.button("Issue3"):
        st.session_state.code = 8000000
        st.rerun()

    if col4.button("Back", key="black_btn"):
        next_step(1)

# Cooktop Switch Common Issue
elif st.session_state.step == 301:

    st.subheader("Common Issue")

    col1, col2, col3, col4 = st.columns(4)

    if col1.button("Issue1"):
        st.session_state.code = 8000000
        st.rerun()

    if col2.button("Issue2"):
        st.session_state.code = 8000000
        st.rerun()

    if col3.button("Issue3"):
        st.session_state.code = 8000000
        st.rerun()

    if col4.button("Back", key="black_btn"):
        next_step(1)

# Desk Switch Common Issue
elif st.session_state.step == 401:

    st.subheader("Common Issue")

    col1, col2, col3, col4 = st.columns(4)

    if col1.button("Issue1"):
        st.session_state.code = 8000000
        st.rerun()

    if col2.button("Issue2"):
        st.session_state.code = 8000000
        st.rerun()

    if col3.button("Issue3"):
        st.session_state.code = 8000000
        st.rerun()

    if col4.button("Back", key="black_btn"):
        next_step(1)

    


# Lock
elif st.session_state.step == 501:

    st.subheader("Common Issue")

    col1, col2, col3, col4 = st.columns(4)

    if col1.button("Issue1"):
        st.session_state.code = 8000000
        st.rerun()

    if col2.button("Issue2"):
        st.session_state.code = 8000000
        st.rerun()

    if col3.button("Issue3"):
        st.session_state.code = 8000000
        st.rerun()

    if col4.button("Back", key="black_btn"):
        next_step(1)


# HPS
elif st.session_state.step == 1001:
        st.session_state.code = 8000000
        st.rerun()


# GPO
elif st.session_state.step == 1501:
        st.session_state.code = 8000000
        st.rerun()


# AC Gateway
elif st.session_state.step == 2001:
        st.session_state.code = 8000000
        st.rerun()


st.html("""
    <style>

        .st-key-black_btn button {
            background-color: #000000 !important;
            color: white !important;
            border: none;
        }
        .st-key-black_btn button:hover {
            background-color: #000000 !important;
            border: none;
        }

        .st-key-green_btn button {
            background-color: #88ff91 !important;
            color: black !important;
            border: none;
        }
        .st-key-green_btn button:hover {
            background-color: #3bcf45 !important;
            border: none;
        }
        
        .st-key-red_btn button {
            background-color: #ff8888 !important;
            color: black !important;
            border: none;
        }
        .st-key-red_btn button:hover {
            background-color: #ff4444 !important;
            border: none;
        }

        div.stButton > button {
        width: 100%;
        }
        
    </style>
""")




