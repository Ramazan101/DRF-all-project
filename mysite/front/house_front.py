import streamlit as st
import requests

def house_chek():
    api_pyti = 'http://127.0.0.1:8000/en/House/'
    st.title('House API')

    area = st.number_input('GrLivArea: ', min_value=0, step=1)
    built = st.number_input('Year Built: ', min_value=0, step=1)
    cars = st.number_input('Garage Cars: ', min_value=0, step=1)
    bsmt_sf = st.number_input('Total Bsmt: ', min_value=0, step=1)
    full_bath = st.number_input('Full Bath: ', min_value=0, step=1)
    overall_qual = st.number_input('Overall Qual: ', min_value=0, step=1)
    neighborhood = st.selectbox('Neighborhood: ', ['Blmngtn', 'Blueste',
                                                   'BrDale', 'BrkSide', 'ClearCr', 'CollgCr',
                                                   'Crawfor', 'Edwards', 'Gilbert',
                                                   'IDOTRR', 'MeadowV', 'Mitchel',
                                                   'NAmes', 'NPkVill', 'NWAmes',
                                                   'NoRidge', 'NridgHt', 'OldTown',
                                                   'SWISU', 'Sawyer', 'SawyerW',
                                                   'Somerst', 'StoneBr', 'Timber',
                                                   'Veenker'])

    house_db = {
      "GrLivArea": area,
      "YearBuilt": built,
      "GarageCars": cars,
      "TotalBsmtSF": bsmt_sf,
      "FullBath": full_bath,
      "OverallQual": overall_qual,
      "Neighborhood": neighborhood
    }
    if st.button('Текшеруу'):
        try:
            house = requests.post(api_pyti, json=house_db, timeout=10)
            if house.status_code == 200:
                result = house.json()
                st.json(result)
            else:
                st.error(f'Жанылыштык: {house.status_code}')
        except requests.exceptions.RequestException:
            st.error('API ге кошула албадыныз')