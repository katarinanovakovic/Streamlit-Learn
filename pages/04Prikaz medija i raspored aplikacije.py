import streamlit as st
from PIL import Image

st.title("Prikaz medija i raspored aplikacije")

st.markdown(""" 
### Prikaz medija
- na jednostavan način, korištenjem naredbi **st.image()** za slike, **st.video** za video i **st.audio()** za zvuk.
""")

colImage, colVideo, colAudio = st.columns(3)
with colImage:
    st.subheader("St.image()")
    programer=Image.open('programer.jpg')
    st.image(programer)

with colVideo:
    st.subheader("St.video()")
    st.video("https://www.youtube.com/watch?v=qPbS_mBFAkg&list=PLHGu0FqnGwUp25bJWb_IN8TiO_yEGvz9A")

with colAudio:
    st.subheader("St.audio()")
    st.audio("summer-walk-152722.mp3")

st.write("")
st.markdown(""" 
### Raspored             
""")

st.write("")

st.markdown(""" 
#### St.sidebar()
- bočna traka koja određene, manje bitne, elemente koje joj proslijedimo prikvači na lijevu stranu 
""")

st.markdown(""" 
#### St.columns()
- omogućuje korisniku da sadržaj podijeli u više stupaca
""")
col1, col2 = st.columns(2)
with col1:
    st.text_area("Ovo je prvi stupac")

with col2:
    st.text_area("Ovo je drugi stupac")
 
st.markdown(""" 
#### St.tabs()
- raspoređuje spremnike s više elemenata u kartice
""")
tab1, tab2, tab3 = st.tabs(["1.kartica", "2.kartica", "3.kartica"])
with tab1:
    st.text("Ovo je prva kartica")
with tab2:
    st.text("Ovo je druga kartica")
with tab3:
    st.text("Ovo je treća kartica")

st.markdown(""" 
#### St.expander()
- spremnik s više elemenata koji se može proširiti/sažeti
""")

with st.expander("Vidi više"):
    st.write("Često se koristi za detaljnije objašnjena slika, tablica, grafova...")

st.markdown(""" 
#### St.container()
- "nevidljivi" spremnik s više elemenata koji nam omogućuje da dodajemo elemente u aplikaciju bez redoslijeda
""")