import streamlit as st

st.sidebar.markdown("Prikaz teksta")

st.title("Prikaz teksta")

st.markdown("""
Streamlit aplikacije obično započinju s pozivom naredbe za naslov - **st.title()**
Pored glavnog naslova, koriste se i dvije razine naslova koje se dobiju korištenjem  naredbi **st.header** i **st.subheader**


""")
if st.button('Vidi primjer'):
    st.title("Glavni naslov")
    st.header("Naslov")
    st.subheader("Podnaslov")
else:
    st.write("")

#St.text()
st.markdown(""" 
#### St.text()
- koristi se za unaprijed formatirani tekst fiksne širine
- nije moguće mijenjati tekst (stil, boju, font)
""")
codeText='''st.text("Primjer")'''
st.code(codeText, language="python")
if st.button('Vidi rezultat'):
    st.text("Primjer")
else:
    st.write("")

#St.markdown()
st.markdown(""" 
#### St.markdown()
- jedini alat za prilagođeni HTML
- omogućuje uređivanje teksta
""")
codeMD='''st.markdown(""":red[Primjer]""")'''
st.code(codeMD, language="python")

if st.button('Vidi rezultat', key='1'):
    st.markdown(""":red[Primjer]""")
else:
    st.write("")

st.markdown(""" 
#### St.code()
- za prikaz teksta u obliku blok koda s dodatnim označavanje sintakse

""")
codeC='''st.code("st.title("Kod")")'''
st.code(codeC, language="python")

if st.button('Vidi rezultat', key='2'):
    st.code('st.title("Kod")')
else:
    st.write("")

st.markdown(""" 
#### St.latex()
- koristi se za matematičke izraze
""")
codeL='''st.latex("c^2 = a^2 + b^2)'''
st.code(codeL, language="python")

if st.button('Vidi rezultat', key='3'):
    st.latex("c^2 = a^2 + b^2")
else:
    st.write("")