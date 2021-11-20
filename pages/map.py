import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk


def app():
    st.header("Map")

    # Compute parking spots coords
    starting_coord = [40.24498472860159, -111.65600451105257]
    ending_coord = [40.24459666714096, -111.65580002369926]
    spots_columns = 18
    spots_rows = 2

    # Create a list of coordinates with the starting point at the top left
    # and the ending point at the bottom right
    location_coords = []
    for i in range(spots_rows):
        for j in range(spots_columns):
            location_coord = []
            location_coord.append(
                starting_coord[0] + (ending_coord[0] - starting_coord[0]) / spots_columns * j)
            location_coord.append(
                starting_coord[1] + (ending_coord[1] - starting_coord[1]) / spots_rows * i)
            location_coords.append(location_coord)

    df = pd.DataFrame(
        location_coords,
        columns=['lat', 'lon'])

    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=location_coords[0][0],
            longitude=location_coords[0][1],
            zoom=20,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'CircleLayer',
                data=df,
                get_position='[lon, lat]',
                radius_scale=1,
                radius=1,
                line_width_min_pixels=1,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=1,
            ),
        ],
    ))
