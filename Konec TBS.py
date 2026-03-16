import streamlit as st

st.image("logo.png", width=200)
st.set_page_config(page_title="Trouble shooting", page_icon="🔧", layout="wide")

st.title("Trouble shooting Tool")

if "step" not in st.session_state:
    st.session_state.step = 0
if "code" not in st.session_state:
    st.session_state.code = None

#Result
if st.session_state.code is not None:

    code = st.session_state.code

    st.success(f"Diagnosis Code: {code}")

    if code == 1:
        st.write("Case closed")

    elif code == 2:
        st.write("Contact Superloop(AP no network)")

    elif code == 3:
        st.write("Contact Konec")

    elif code == 4:
        st.write("Contact the electrician(Might be wiring issue)")

    elif code == 9999999:
        st.write("Case closed")
    
    else:
        st.write("Pending, waiting for update")

    if st.button("Restart"):
        st.session_state.step = 1
        st.session_state.code = None
        st.rerun()

    st.stop()


def next_step(step):
    st.session_state.step = step
    st.rerun()

# Disclaimer
if st.session_state.step == 0:

    st.subheader("Disclaimers")
    
    st.write("")
    st.write("")

    st.write("1. Please follow all instructions carefully and ensure compliance with AS/NZS 3000 and local regulations. Improper installation or modification may void the warranty and result in safety risks. ")
    st.write("2. The information provided in this manual is for general guidance and reference purposes only. Konec Solutions Pty Ltd makes no representations or warranties, express or implied, regarding the completeness, accuracy, or suitability of the content. Product specifications, features, and visuals are subject to change without notice. ")
    st.write("3. To the extent allowed by law, Konec Solutions is not liable for any damage, injury, or loss resulting from the use of this guide or the installation process. ")
    st.write("4. This disclaimer does not affect your rights under the Australian Consumer Law or the New Zealand Consumer Guarantees Act 1993. ")
    st.write("5. This product is designed for professional installation.")
    st.write("6. Disconnect power before starting installation or maintenance.")
    st.write("7. Do not exceed the product's rated electrical capacity.")
    st.write("8. Avoid using power tools unless explicitly specified.")
    st.write("9. Use appropriate personal protective equipment (e.g., gloves, safety glasses).")
    st.write("10. Do not install in areas exposed to water or high humidity unless rated for such conditions.")
    st.write("11. All content in this App including text, images, and graphics—is the property of Konec Solutions. No part may be reproduced, translated, or modified without prior written permission. ")

    st.write("")
    st.write("")

    col1 = st.columns(1)

    if col1.button("I Agree"):
        next_step(1)


# Select device
if st.session_state.step == 1:

    st.subheader("Select the problematic device")

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    if col1.button("Switch"):
        next_step(2)

    if col2.button("Lock"):
        next_step(2)

    if col3.button("HPS"):
        next_step(2)

    if col4.button("GPO"):
        next_step(2)

    if col5.button("A/C Gateway"):
        next_step(2)

    if col6.button("HID Access"):
        next_step(2)


# 
if st.session_state.step == 2:

    st.subheader("Is the device online or offline?")

    col1, col2= st.columns(2)

    if col1.button("Online", key="green_btn"):
        st.session_state.code = 8000000
        st.rerun()

    if col2.button("Offline", key="red_btn"):
        next_step(3)

    st.write("")
        
    st.write("")

    if st.button("Back", key="black_btn"):
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

#待开发
elif st.session_state.step == 9999:
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
