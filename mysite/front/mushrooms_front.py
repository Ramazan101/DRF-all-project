import streamlit as st
import requests


def mushrooms_chek():
    st.title('Mushroom API')

    api_url = 'http://127.0.0.1:8000/en/Mushroom/'

    cap_shape = st.selectbox('Cap Shape:', ['b', 'c', 'f', 'k', 's', 'x'])
    cap_surface = st.selectbox('Cap Surface:', ['f', 'g', 's', 'y'])
    cap_color = st.selectbox('Cap Color:', ['n', 'y', 'w', 'g', 'e', 'p', 'b', 'u', 'c', 'r'])
    bruises = st.selectbox('Bruises:', ['t', 'f'])
    odor = st.selectbox('Odor:', ['p', 'a', 'l', 'n', 'f', 'c', 'y', 's', 'm'])
    gill_attachment = st.selectbox('Gill attachment:', ['f', 'a'])
    gill_spacing = st.selectbox('Gill spacing:', ['c', 'w'])
    gill_size = st.selectbox('Gill size:', ['n', 'b'])
    gill_color = st.selectbox('Gill color:', ['k', 'n', 'g', 'p', 'w', 'h', 'u', 'e', 'b', 'r', 'y', 'o'])
    stalk_shape = st.selectbox('Stalk shape:', ['e', 't'])
    stalk_root = st.selectbox('Stalk root:', ['e', 'c', 'b', 'r'])
    stalk_surface_above_ring = st.selectbox('Stalk surface above ring:', ['s', 'f', 'k', 'y'])
    stalk_surface_below_ring = st.selectbox('Stalk surface below ring:', ['s', 'f', 'y', 'k'])
    stalk_color_above_ring = st.selectbox('Stalk color above ring:', ['w', 'g', 'p', 'n', 'b', 'e', 'o', 'c', 'y'])
    stalk_color_below_ring = st.selectbox('Stalk color below ring:', ['w', 'p', 'g', 'b', 'n', 'e', 'y', 'o', 'c'])
    veil_color = st.selectbox('Veil color:', ['w', 'n', 'o', 'y'])
    veil_type = st.selectbox('Veil type:', ['p'])
    ring_number = st.selectbox('Ring number:', ['o', 't', 'n'])
    ring_type = st.selectbox('Ring type:', ['p', 'e', 'l', 'f', 'n'])
    spore_print_color = st.selectbox('Spore print color:', ['k', 'n', 'u', 'h', 'w', 'r', 'o', 'y', 'b'])
    population = st.selectbox('Population:', ['s', 'n', 'a', 'v', 'y', 'c'])
    habitat = st.selectbox('Habitat:', ['u', 'g', 'm', 'd', 'p', 'w', 'l'])


    mushroom_data = {
        "cap_shape": cap_shape,
        "cap_surface": cap_surface,
        "cap_color": cap_color,
        "bruises": bruises,
        "odor": odor,
        "gill_attachment": gill_attachment,
        "gill_spacing": gill_spacing,
        "gill_size": gill_size,
        "gill_color": gill_color,
        "stalk_shape": stalk_shape,
        "stalk_root": stalk_root,
        "stalk_surface_above_ring": stalk_surface_above_ring,
        "stalk_surface_below_ring": stalk_surface_below_ring,
        "stalk_color_above_ring": stalk_color_above_ring,
        "stalk_color_below_ring": stalk_color_below_ring,
        "veil_color": veil_color,
        "veil_type": veil_type,
        "ring_number": ring_number,
        "ring_type": ring_type,
        "spore_print_color": spore_print_color,
        "population": population,
        "habitat": habitat
    }

    if st.button('Текшеруу'):
        try:
            answer = requests.post(api_url, json=mushroom_data, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.json(result)
            else:
                st.error(f"Жанылыштык: {answer.status_code}")
        except requests.exceptions.RequestException:
            st.error('Сиз API ге кошула албадыныз ')
