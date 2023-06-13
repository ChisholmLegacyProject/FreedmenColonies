import streamlit as st
import pandas as pd
import geopandas as gpd
import requests
import folium
from streamlit_folium import folium_static

url = 'https://raw.githubusercontent.com/ChisholmLegacyProject/FreedmenColonies/main/FC.geojson'
response = requests.get(url)
data = response.json()

def main():
    # Load GeoJSON data into a GeoDataFrame
    geodata = gpd.GeoDataFrame.from_features(data['features'])

    # Set app title
    st.title('Interactive Dashboard and Map')

    # Display the GeoDataFrame
    st.subheader('GeoJSON Data')
    st.write(geodata)

    # Display map
    st.subheader('Map')
    folium_map = folium.Map(location=[0, 0], zoom_start=2)

    for feature in data['features']:
        properties = feature['properties']
        name = properties['name']
        total_population = properties['total_popu']
        male_population = properties['male_popul']
        female_population = properties['female_pop']
        black_population = properties['black']
        latino_population = properties['latino']
        poverty = properties['poverty']
        prime_name = properties['Prime_name']
        other_name = properties['Other_name']
        risk_score = properties['RISK_SCORE']
        sovi_score = properties['SOVI_SCORE']

        popup_text = f'''
            Name: {name}<br>
            Total Population: {total_population}<br>
            Male Population: {male_population}<br>
            Female Population: {female_population}<br>
            Black Population: {black_population}<br>
            Latino Population: {latino_population}<br>
            Poverty: {poverty}<br>
            Prime Name: {prime_name}<br>
            Other Name: {other_name}<br>
            Risk Score: {risk_score}<br>
            SOVI Score: {sovi_score}
        '''

        folium.Marker(
            location=(feature['geometry']['coordinates'][1], feature['geometry']['coordinates'][0]),
            popup=folium.Popup(popup_text, max_width=250),
            icon=folium.Icon(icon='info-sign')
        ).add_to(folium_map)

        folium.Marker(
            location=(feature['geometry']['coordinates'][1], feature['geometry']['coordinates'][0]),
            icon=folium.DivIcon(
                html=f'<div style="font-weight: bold; text-align: center;">{prime_name}</div>',
                icon_size=(100, 20),
                icon_anchor=(50, 0)
            )
        ).add_to(folium_map)

    folium_static(folium_map)

    # Display individual variables
    st.subheader('Individual Variables')
    for feature in data['features']:
        properties = feature['properties']
        name = properties['name']
        total_population = properties['total_popu']
        male_population = properties['male_popul']
        female_population = properties['female_pop']
        black_population = properties['black']
        latino_population = properties['latino']
        poverty = properties['poverty']
        prime_name = properties['Prime_name']
        other_name = properties['Other_name']
        risk_score = properties['RISK_SCORE']
        sovi_score = properties['SOVI_SCORE']

        st.write(f'Name: {name}')
        st.write(f'Total Population: {total_population}')
        st.write(f'Male Population: {male_population}')
        st.write(f'Female Population: {female_population}')
        st.write(f'Black Population: {black_population}')
        st.write(f'Latino Population: {latino_population}')
        st.write(f'Poverty: {poverty}')
        st.write(f'Prime Name: {prime_name}')
        st.write(f'Other Name: {other_name}')
        st.write(f'Risk Score: {risk_score}')
        st.write(f'SOVI Score: {sovi_score}')
        st.write('---')

if __name__ == '__main__':
    main()
