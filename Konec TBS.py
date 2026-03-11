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

    elif code == 9999999:
        st.write("Case closed")
    
    else:
        st.write("Pending, waiting for update")

    if st.button("Restart"):
        st.session_state.step = 0
        st.session_state.code = None
        st.device_num = 0
        st.AP_num = 0
        st.orange_num = 0
        st.rerun()

    st.stop()

def next_step(step):
    st.session_state.step = step
    st.rerun()

# 选择设备
if st.session_state.step == 0:

    st.subheader("Select the problematic device")

    col1, col2, col3, col4, col5 = st.columns(5)

    if col1.button("Switch"):
        st.device_num = 1
        next_step(1)

    if col2.button("Lock"):
        st.device_num = 2
        next_step(1)

    if col3.button("HPS"):
        st.device_num = 3
        next_step(1)

    if col4.button("GPO"):
        st.device_num = 4
        next_step(1)

    if col5.button("AC Gateway"):
        st.device_num = 5
        next_step(1)


# 设备离线
if st.session_state.step == 1:

    st.subheader("Is the device online or offline?")

    col1, col2= st.columns(2)

    if col1.button("Online", key="green_btn"):
        next_step(1000)

    if col2.button("Offline", key="red_btn"):
        next_step(2)

    st.write("")
        
    st.write("")

    if st.button("Back", key="black_btn"):
        next_step(1)


# 所有设备离线
if st.session_state.step == 2:

    st.subheader("Are all devices online or offline?")

    col1, col2= st.columns(2)

    if col1.button("Online", key="green_btn"):
        next_step(9999)

    if col2.button("Offline", key="red_btn"):
        next_step(3)

    st.write("")
        
    st.write("")

    if st.button("Back", key="black_btn"):
        next_step(1)

# 网关离线
if st.session_state.step == 3:

    st.subheader("Are all devices online or offline?")

    col1, col2= st.columns(2)

    if col1.button("Online", key="green_btn"):
        st.session_state.code = 3
        st.rerun()

    if col2.button("Offline", key="red_btn"):
        next_step(4)

    st.write("")
        
    st.write("")

    if st.button("Back", key="black_btn"):
        next_step(2)

# 电闸
if st.session_state.step == 4:

    st.subheader("Is circuit breaker ON/OFF?")

    col1, col2= st.columns(2)

    if col1.button("ON", key="green_btn"):
        next_step(5)

    if col2.button("OFF", key="red_btn"):
        next_step(6)

    st.write("")
        
    st.write("")

    if st.button("Back", key="black_btn"):
        next_step(3)

# 网关离线
if st.session_state.step == 5:

    st.subheader("Are both indicator lights on the AP constantly on?")


    if st.button("No green light on"):
        st.AP_num = 1
        next_step(7)

    if st.button("One green light on"):
        st.session_state.code = 2
        st.rerun()

    if st.button("Both green lights on"):
        st.AP_num = 2
        next_step(9)

    st.write("")

    st.write("")

    if st.button("Back", key="black_btn"):
        next_step(4)
    
    st.image("AP Light.png", width=500)

# 打开电闸
if st.session_state.step == 6:

    st.subheader("Turn on circuit breaker")
    st.subheader("Wait a few minutes")
    st.write("")
    
    st.write("")

    if st.button("Next", key="green_btn"):
        next_step(5)
    
    if st.button("Back", key="black_btn"):
        next_step(4)

# No green light on
if st.session_state.step == 7:

    st.subheader("Switch the ports connected by the blue cable")
    st.subheader("Wait a few minutes")
    st.write("")
    
    st.write("")

    if st.button("Next", key="green_btn"):
        next_step(8)

    if st.button("Back", key="black_btn"):
        next_step(5)    
    
    st.image("AP Light.png", width=500)

# both green light on?
if st.session_state.step == 8:

    st.subheader("Is circuit breaker ON/OFF?")

    col1, col2= st.columns(2)

    if col1.button("Yes", key="green_btn"):
        next_step(9)

    if col2.button("No", key="red_btn"):
        st.session_state.code = 2
        st.rerun()

    st.write("")
        
    st.write("")

    if st.button("Back", key="black_btn"):
        next_step(7)

    st.image("AP Light.png", width=500)

# Is the orange light on？(near the AP network port.)
if st.session_state.step == 9:

    st.subheader("Is the orange light on?(near the AP network port.)")

    col1, col2= st.columns(2)

    if col1.button("Yes", key="green_btn"):
        next_step(10)
        orange_num = 1

    if col2.button("No", key="red_btn"):
        next_step(11)
        orange_num = 2

    st.write("")
        
    st.write("")

    if st.button("Back", key="black_btn"):
        if st.AP_num == 1:
            next_step(8)
        else:
            next_step(5)

    st.image("AP Light.png", width=500)




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














