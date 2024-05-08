import streamlit as st
import streamlit_book as stb
import numpy as np
import pandas as pd


with st.sidebar.form(key='columns_in_form',clear_on_submit=True): 
    rating=st.slider("Ocijenite aplikaciju :) ", min_value=1, max_value=5, value=5,help='Povucite klizač da ocijenite aplikaciju. Ovo je ljestvica ocjenjivanja od 1 do 5 gdje je 5 najviša ocjena.')
    text=st.text_input(label='Ostavite svoj komentar')
    submitted = st.form_submit_button('Pošalji')
    if submitted:
      st.write('Hvala!')



st.header("Provjera znanja")
st.write(" ")
 

stb.single_choice(question ="1.Je li Streamlit otvorenog ili zatvorenog koda?", 
                  options= ["Otvorenog", "Zatvorenog"],
                  answer_index= 0, success= "Točno!", error= "Netočno", button= "Rezultat")


stb.single_choice(question= "2.Koje programske jezike podržava Streamlit?", options= ["Sve programske jezike", "Java i Python", "Samo Python"],
                  answer_index= 2, success= "Točno!", error= "Netočno", button= "Rezultat" )
stb.single_choice(question= "3.Streamlit se najčešće koristi za: ", options= ["Strojno učenje", "Programiranje igrica", "Programiranje softvera"],
                  answer_index= 0, success= "Točno!", error= "Netočno", button= "Rezultat" )
stb.single_choice(question= "4.Zašto je naredba st.markown() posebna? ", options= ["Pruža nam unaprijed formatiran teks", "Koristi se za pisanje matematičkih izraza", "Omogućuje mjenjanje stila, fonta i boje"],
                  answer_index= 2, success= "Točno!", error= "Netočno", button= "Rezultat" )
stb.single_choice(question= "5.Za što služi naredba st.conatiner()?", options= ["Za detaljno objašnjenje prikazanog", "Za umetanje lemenata bez redoslijeda", "Za prikaz uokvirenog teksa"],
                  answer_index= 1, success= "Točno!", error= "Netočno", button= "Rezultat" )
stb.single_choice(question= "6.Koju vrstu grafa daje naredba st.graphvizchart()? ", options= ["a)", "b)", "c)"],
                  answer_index= 1, success= "Točno!", error= "Netočno", button= "Rezultat" )

data= pd.DataFrame(
    np.random.randn(100,3),
    columns= ['x', 'y', 'z']
)
col1, col2, col3= st.columns(3)
with col1:
    st.subheader("a)")
    st.bar_chart(data)
with col2:
    st.subheader("b)")
    st.graphviz_chart(''' 
    digraph {
    A -> B
    A -> C
    B -> D
    C -> D

    }
    ''')
with col3:
    st.subheader("c)")
    st.area_chart(data)

