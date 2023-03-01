import streamlit as st

st.title("Innomatics Data App")
st.header('Hello folks!! This is shireesha...This is my first DataApp Creation')
st.snow()

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :cry:")
    st.balloons()