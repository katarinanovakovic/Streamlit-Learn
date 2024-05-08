import streamlit as st
import numpy as np
import pandas as pd

st.sidebar.markdown("Prikaz podataka")

st.title("Prikaz podataka")

st.markdown("""
U Streamlit-u postoje različite načini za prikaz podataka i raličite vrste podataka koje možemo koristit. Za primjer ćemo uzeti dvije vrste podataka: višedimenzijski niz i rječnik.
Za početak trebamo definirati višedimenzijski niz i rječnik nad kojima ćemo izvesti naredbe za prikaz podataka.
""")
#Višedimenzijski niz
st.write("Višedimenzijski niz (primjer)")
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
codeArray='''array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])'''
st.code(codeArray, language="python")


#Rječnik
st.write("Rječnik (primjer)")
dic = {
    "name": "Ivan",
    "age": 25, 
    "city": "Split", 
}


codeDic='''dic = {'name': 'Ivan', 'age': 25, 'city': 'Split'}'''
st.code(codeDic, language="python")

st.subheader("Osnovne naredbe za prikaz podataka")

#st.dataframe
st.markdown("""
#### St.dataframe()
- prikazuje podatke u obliku interaktivne tablice.
""")
codeDF1='''st.dataframe(dic)'''
st.code(codeDF1, language="python")
#df=pd.DataFrame(dic)
st.dataframe(dic)

#array1= np.array([1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21])
codeDF2='''st.dataframe(array)'''
st.code(codeDF2, language= "python")
st.dataframe(array)

#st.table
st.markdown("""
#### St.table()
- naredba koja prikazuje sve podatke (nema scroll bar)
- koristi se kao bolja opcija kada imamo manju količinu podataka
""")
codeT1='''st.table(dic)'''
st.code(codeT1, language="python")
st.table(dic)

codeT2='''st.table(array)'''
st.code(codeT2, language="python")
st.table(array)

#st.json
st.markdown(""" 
#### St.json()
- naredba koja se koristi za podatke formatirane kao .JSON
- najbolji primjer za to je rječnik
""")
codeJ1='''st.json(dic)'''
st.code(codeJ1, language="python")
st.json(dic)



#St.write()
st.markdown(""" 

#### St.experimental_data_editor()
- koristi se za uređivanje podataka

""")
codeDE1='''st.experimental_data_editor(dic)'''
st.code(codeDE1, language="python")
st.experimental_data_editor(dic)

codeDE2='''st.experimental_data_editor(array)'''
st.code(codeDE2, language="python")
st.experimental_data_editor(array)