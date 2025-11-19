'''import streamlit as st
import datetime 
if st.button('Current Time'):
    st.write(datetime.datetime.now())
if st.button("use me to start"):
    st.write("hello harini")'''

'''import streamlit as st
import requests

st.header("guess age by name")
name=st.text_input("Name in capital")
if name:
    r=requests.get(f'https://api.agify.io/?name={name}').json()
    st.write(f'your age is predicted to be {r["age"]}')'''
    
import streamlit as st, requests

st.header("Pokemon Image")
mypokemon=['pikachu','charizard','eevee','snorlax','garchomp','lucario']
pokemon=st.selectbox("select a pokemon",mypokemon)
if pokemon:
    r=requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}').json()
    for img in r['sprites'].values():
        if img is not None:
            if str(img) [-4:] == '.png':
                st.image(img)