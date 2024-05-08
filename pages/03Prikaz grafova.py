import streamlit as st
import numpy as np
import pandas as pd
import graphviz


st.sidebar.markdown("Prikaz grafova")
st.title("Prikaz grafova")

st.markdown(""" 
Streamlit je odličan alat za prikaz grafova i medija na jednostavan način.
Kako bi prikazali što nam Streamlit omogućuje, uzet ćemo neke random podatke.
""")

data= pd.DataFrame(
    np.random.randn(100,3),
    columns= ['a', 'b', 'c']
)

codeRP=''' data= pd.DataFrame(
    np.random.randn(100,3)
    columns= ('a', 'b', 'c')
)'''
st.code(codeRP, language="python")

#St.line_chart
st.markdown(""" 
#### St.line_chart()
- najjednostavniji oblik vizualizacije podataka
- povezuje niz podatkovnih točaka u liniju
""")
st.line_chart(data, x='a', y=['b', 'c'],width= 50, height=	300)

#st.area_chart
st.markdown(""" 
#### St.area_chart()
""")
st.area_chart(data, width=50, height=300)

#st.bar-chart()
st.markdown(""" 
#### St.bar_chart()
""")
st.bar_chart(data, width=50, height=300)

st.markdown(""" 
Uz ove osnovne naredbe, Streamlit podržava puno biblioteka pomoću kojih se također mogu vizualizirati podatci. 
Neke od najpoznatijih su **MATPLOTLIB** i **ALTAIR** koje možete istražiti na službenoj stranici Streamlit-a.


Pored osnovnih naredbi i biblioteka izvdojit ćemo još dvije jednostavne i zanimljive naredbe:
""")

st.markdown(""" 
#### St.graphviz_chart()
""")

st.graphviz_chart(''' 
digraph {
Stremlit_plot -> line_chart
Stremlit_plot -> bar_chart
Stremlit_plot -> area_chart
}
''')

st.markdown(""" 
#### St.map()
""")
st.map()
