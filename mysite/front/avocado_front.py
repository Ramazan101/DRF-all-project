import streamlit as st
import requests
def avocado_chek():
    st.title('Avocado API')

    api_url = 'http://127.0.0.1:8000/en/Avocado/'

    firmness = st.number_input('firmness', min_value=10.0, max_value=100.0, step=0.1)
    hue = st.number_input('hue', min_value=0, max_value=400, step=1)
    saturation = st.number_input('saturation', min_value=30, max_value=100, step=1)
    brightness = st.number_input('brightness', min_value=10, max_value=100, step=1)
    sound_db = st.number_input('sound_db', min_value=30, max_value=79, step=1)
    weight_g = st.number_input('weight_g', min_value=153, max_value=300, step=1)
    size_cm3 = st.number_input('size_cm3', min_value=100, max_value=300, step=1)
    color_category = st.selectbox('Colors', ['dark green', 'green', 'purple'])

    avocado_data = {
        "firmness": firmness,
        "hue": hue,
        "saturation": saturation,
        "brightness": brightness,
        "sound_db": sound_db,
        "weight_g": weight_g,
        "size_cm3": size_cm3,
        "color_category": color_category
    }
    if st.button('Текшеруу'):
        try:
            avocado = requests.post(api_url, json=avocado_data, timeout=10)
            if avocado.status_code == 200:
                result = avocado.json()
                st.json(result)
            else:
                st.error(f'Жанылыштык: {avocado.status_code}')
        except requests.exceptions.RequestException:
            st.error('API ге кошула албадыныз')

