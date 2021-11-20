import streamlit as st
from streamlit_autorefresh import st_autorefresh
from gsheetsdb import connect
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
from datetime import datetime


def app(self):
    st.header("Logger")

    # Authorize the API
    scope = [
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.file'
    ]
    file_name = 'client_key.json'
    creds = ServiceAccountCredentials.from_json_keyfile_name(file_name, scope)
    client = gspread.authorize(creds)

    # Fetch the sheet
    try:
        sheet = client.open('parkcorps-master').sheet1
    except:
        pass

    option = 0
    name = st.selectbox('Parking Spot Selection',
                        self.parking_spaces_master['name'])

    st.write('You selected: ', name)

    availability = int(float(GetValue(self, name, 'available')))

    if(availability):
        st.markdown("#### Spot available")
    else:
        st.markdown("#### Spot unavailable")

    st.button('Switch', on_click=BtnUpdateAvailability,
              args=(sheet, name, availability))

    timestamp = GetValue(self, name, 'timestamp')
    timestamp_label = "###### _Updated on " + timestamp + "_"
    st.markdown(timestamp_label)


def BtnUpdateAvailability(sheet, name, availability):
    if(availability):
        UpdateAvailability(sheet, name, 0)
    else:
        UpdateAvailability(sheet, name, 1)


def UpdateAvailability(sheet, name, value):
    UpdateValue(sheet, name, "available", value)
    timestamp = datetime.now().strftime("%m/%d/%Y %I:%M:%S")
    UpdateValue(sheet, name, "timestamp", timestamp)


def UpdateValue(sheet, name, column_name, value):
    cell = sheet.find(str(name), in_column=2)
    row = cell.row
    cell = sheet.find(str(column_name), in_row=1)
    col = cell.col
    sheet.update_cell(row, col, str(value))


def GetValue(self, name, value):
    string = self.parking_spaces_master.loc[self.parking_spaces_master['name']
                                            == name, value].to_string()

    string_array = string.split(' ')

    new_array = []
    for i in string_array[1:]:
        if i != '':
            new_array.append(i)

    return str(" ".join(new_array))
