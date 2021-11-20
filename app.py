from os import write
import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
import streamlit.components.v1 as components
import hydralit as hy
# from computervision.motiontracker import VideoProcessor
import pandas as pd
import numpy as np


from pages.multipage import MultiPage
from pages import database, map

# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Park Corps")

app.add_page("Raw Database", database.app)
app.add_page("Map", map.app)
# app.add_page("Machine Learning", machine_learning.app)
# app.add_page("Data Analysis",data_visualize.app)
# app.add_page("Y-Parameter Optimization",redundant.app)

app.run()


# # Set up RTC config for https protocol
# RTC_CONFIGURATION = RTCConfiguration(
#     {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
# )

# # Set title
# app = hy.HydraApp(title='Park Corps')


# @app.addapp(title='Home')
# def Home():
#     st.header("Park Corps")


# @app.addapp(title='Database')
# def Models():
#     st.header("Database")


# @app.addapp(title='Map')
# def Demo():
#     st.header("Map")

#     # webrtc_ctx = webrtc_streamer(
#     #     key="motion-tracker",
#     #     mode=WebRtcMode.SENDRECV,
#     #     rtc_configuration=RTC_CONFIGURATION,
#     #     video_processor_factory=VideoProcessor,
#     #     media_stream_constraints={"video": True, "audio": False},
#     #     async_processing=True,
#     # )


# app.run()
