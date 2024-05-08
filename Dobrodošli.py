import streamlit as st
import streamlit_book as stb
from PIL import Image, ImageEnhance

st.set_page_config(
    page_title="StreamLit Learn"
)

with st.sidebar.expander("Što je SL?"):
     st.write("""
        Streamlit Learn je tečaj o izradi web aplikacija pomoću Streamlit-a. Kroz 5 lekcija prikazuje osnovne elemente Streamlit-a, njihovu primjenu, te kroz jednostavne primjere omogućuje korisnicima da na brz i lagan način stvore web aplikaciju. 
        Poželjno bi bilo unaprijed poznavanje programskog jezika Python, ali nije nužno jer je tečaj prilagođen i za početnike.
        
        Nakon pažljivo pročitanih lekcija, svoje znanje možete provjeriti kroz mali kviz koji smo pripremili za Vas.
        Uživajte! :)
     """)

with st.sidebar.expander("O aplikaciji"):
     st.write("""
        Aplikacija je nastala kao ideja za završni rad, studentice treće godine računarstva na Faklutetu elektrotehnike, strojarstva i brodogradnje (FESB) u Splitu.
        Napravljena je u programu Visual Studio Code koristeći isključivo Streamlit.
     """)



#Add the title for the e-tutorial
st.markdown(""" <style> .font {
    font-size:40px ; font-family: 'Cooper Black'; color: #D60000;} 
    </style> """, unsafe_allow_html=True)

col4, col5, col6 =st.columns([3,6,1])
with col4:
    st.write("")
with col5:
    st.markdown('<p class="font">Dobrodošli!</p>', unsafe_allow_html=True)
with col6:
    st.write("")

#Add the cover image for the cover page. Used a little trick to center the image
col1, col2, col3 = st.columns([1,1,60])
with col1:
    st.write("")
with col2:
    image = Image.open(r'mojLogo1novi.png')
    st.image(image, width=600)
with col3:
    st.write("")