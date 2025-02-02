import streamlit as st

st.set_page_config(page_title="Be My Valentine?")

st.title("Will You Be My Valentine?")

st.write("Roses are red,\nviolets are blue,\nI'm sorry that I mess up sometimes\nand smell just like poo")

yes_clicked = st.button("Yes!")

if yes_clicked:
    st.balloons()
    st.success("sowwy it took so long for me to ask 😅. I love you!!")

st.image("love-mochi.gif", use_container_width=True)
