# 6/27/25
# Author: Tony Rahman | https://flyingsalmon.net
# This demonstrates an advanced, interactive map showing parks within 10 miles of 98012 zip code.
# Uses streamlit's pydeck for advanced mapping features, and UI (multiselect, filter)
# *** For simpler interactive maps and charts, see charts_examples.py ***


import streamlit as st
import pandas as pd
import pydeck as pdk

# Parks data
df = pd.DataFrame({
    'Park': [
        'McCollum Pioneer Park', 'Mill Creek Sports Park',
        'Heatherwood Middle School Grounds', 'Henry M Jackson High School Fields',
        'North Creek Park', 'Cedar Grove Park',
        "Miner's Corner",'Tambark Creek Park',
        'Centennial Park', 'Highlands Park',
        
        'Martha Lake Park', 'Thornton Sullivan Park (Silver Lake)',
        'Hauge Homestead Park (Silver Lake)', 'Green Lantern Park (Silver Lake)',
        'Cougar Park', 'Heron Park',
        'Penny Creek Natural Area', 'Cherry Park',
        
        'Mill Creek Town Center N Creek Trail', 'Mill Creek Nature Preserve',
        'North Creek Trail Pond', 'Holly Community Park',
        'Willis Tucker Community Park', 'Lowell Riverfront Trail',
        'Lighthouse Park (Mukilteo)', 'Picnic Point Park (Edmonds)',
        
        'Edmonds - Bracketts Landing N.', 'Boxcar Park (The Muse, Everett)',
        'American Legion Memorial Park (Everett)', 'Meadowdale Beach Park'
    ],
    
    'lat': [47.88015, 47.87239,
            47.87189, 47.87316,
            47.83282, 47.79474,
            47.78995, 47.840177,
            47.809018, 47.851038,
            
            47.850192, 47.894618,
            47.888886, 47.894274,
            47.863699, 47.857897,
            47.870604, 47.868684,
            
            47.856287, 47.856961,
            47.851909, 47.863968,
            47.86338, 47.947293,
            47.951183, 47.880186,
            
            47.813657, 48.000805,
            48.016112, 47.857301
            
            ],
    
    'lon': [-122.22221, -122.21853,
            -122.21196, -122.20525,
            -122.21927, -122.21912,
            -122.17142, -122.182751,
            -122.217086, -122.194391,
            
            -122.244770, -122.213432,
            -122.207205, -122.203053,
            -122.188452, -122.195564,
            -122.183211, -122.200411,
            
            -122.221311, -122.213978,
            -122.221425, -122.213171,
            -122.14152, -122.190930,
            -122.306542, -122.331860,
            
            -122.381559, -122.221843,
            -122.203424, -122.316456
            ],
    
    'features': [
        'Trails, Wetland, Grassy Area, Biking Trail, BMX Track, Playground, Cricket', 'Baseball Field, Skate Park, Playground, Multi-use Sports Field',
        'Tennis Court, Soccer Field, Baseball Field, Basketball Court, Soccer Field, Trails, Track & Field', 'Tennis Court, Football Field, Baseball Field, Basketball Court, Grassy Area',
        'Wetland, Wildlife Watching, Boardwalk, Trails', 'Playground, Picnic Area',
        'Playground, Trails', 'Sports Field, Off-leash Area',
        'Trails, Birdwatching', 'Playground, Tennis Court, Pickleball Court, Basketball Court, BBQ, Restroom',
        
        'Playground, Fishing, Picnic Area, Wetland, Boardwalk, Sailing, Restroom', 'Basketball Court, Trails, Playground, Beach, Volleyball Court, Sailing',
        'BBQ, Picnic Area, Trails, Playground, Fishing, Restroom', 'Grassy Area, Trails',
        'Playground, Restroom', 'Trails, Tennis Court, Pickleball Court, Playground, Restroom',
        'Birdwatching, Trails, Wildlife Watching', 'Trails, Playground',
        
        'Trails, Birdwatching, Biking Trail', 'Trails, Playground, Basketball Court, Grassy Area',
        'Trails, Birdwatching, Biking Trail, Picnic Area', 'Trails, Playground, Grassy Area, Birdwatching',
        'Baseball Field, Playground, Amphitheater, Off-leash Area, Volleyball Court, Grassy Area', 'Birdwatching, Trails, Biking Trail, Hiking',
        'Hiking, Beach, BBQ, Picnic Area, Restroom, Playground, Birdwatching, Wildlife Watching, Gardens', 'Beach, Picnic Area, BBQ',
        
        'Trails, Beach, Picnic Area', 'Picnic Area, Restroom, Grassy Area, Hiking, Biking Trail, Birdwatching, Wildlife Watching',
        'Trails, BBQ, Baseball Field, Basketball Court, Tennis Court, Picnic Area, Restroom, Playground, Gardens, Arboretum',
        'Beach, Picnic Area, Hiking, Trails, Wetlands, Wildlife Watching, Grassy Area'
    ]
})

# Flatten all unique features into a 1D array: e.g. ['ADA Accessible', 'Baseball Field',..., 'Trails', 'Wetland']
all_features = sorted(set(
    feature.strip()
    for feature_list in df['features']
    for feature in feature_list.split(',')
))

# print(all_features)

st.write("### Parks & Recreation Areas within 10 miles of 98012")

# Multiselect UI (dropdown and each selection is placed in the field one by one)
selected_features = st.multiselect(
    "Filter parks by features:",
    options=all_features, # items in the dropdown list
    default=[]
)

# Filter function
def has_selected_features(features_cell, selected):
    features_set = set(f.strip() for f in features_cell.split(','))
    return any(f in features_set for f in selected)

# Filter DataFrame based on selected features
if selected_features: # if any feature is selected from dropdown by user
    filtered_df = df[df['features'].apply(lambda x: has_selected_features(x, selected_features))]
else:
    filtered_df = df # if nothing is specified in filter, show all

# Display number of parks
st.subheader(f"Showing {len(filtered_df)} park(s)")



# Pydeck map
# Get the token from toml file
mapbox_token = st.secrets["mapbox_token"]
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/outdoors-v11',
    initial_view_state=pdk.ViewState(
        latitude=47.87,
        longitude=-122.215,
        zoom=10,
        pitch=30
    ), 
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=filtered_df,
            get_position='[lon, lat]',
            get_fill_color='[34, 139, 34, 180]',
            get_radius=400, # size of the markers
            pickable=True
        )
    ],
    tooltip={
        "html": "<b>{Park}</b><br/>{features}",
        #"html": "<b>{Park}</b><br/>{features}<br/><a href='{url}' target='_blank'>🧭 Get Directions</a>",
        "style": {"backgroundColor": "ivory", "color": "black", "fontSize": "16px"}
    },
  
   api_keys={"mapbox": mapbox_token}
))


# Add a href link using streamlit. For UI help for example.
# This is useful to link to an external page (not a subpage) and control if it should open in a new tab or current tab.
# url = "http://flyingsalmon.net"
# link_text = "Click here for map UI navigation tips"
# st.markdown(
#     f'<a href="{url}" target="_blank">🌐 {link_text}</a>',
#     unsafe_allow_html=True
# )

# To create a clickable href link to subpage 1_UIGuide.py—as inside a pages/ directory:
# st.markdown("[📘 Map UI Navigation Help](?page=1_UI_Guide)", unsafe_allow_html=True)  # works but currently commented

# The file to navigate to is in /pages/1_UI_Guide.py but the display in the sidebar menu will be automatically shown as: UI Guide (underscores replaced by spaces)
# And to refer to it as a link with st.markdown, remove the extension (.py) when specifying the parameter above but keep the underscores as in original file name!

# st.divider() # horizontal light gray line

# Following block of code for dropdown list of parks and dynamic directions url is now in 1_Park_Directions.py file:
# selected_park = st.selectbox("Get info & directions to a specific park:", sorted(df['Park']))
# park_row = df[df['Park'] == selected_park].iloc[0]
# 
# st.markdown(
#     f"Selected: 📍{selected_park}| {park_row['features']} 🚗 [🧭 Directions](https://www.google.com/maps/search/?api=1&query={park_row['lat']},{park_row['lon']})",
#     unsafe_allow_html=True
# )


# NOTE: Google Maps shows coordinates in Degrees, Minutes, Seconds (DMS) format, but our dataframe needs Decimal Degrees (DD).
# To get DD format from Google maps, locate in maps, right-click on the pin marker to see the DD values (drag mouse until next row in the popup to copy the coordinates text).
# Or better: right-click and Share...a popup window opens where the DD format is shown that can be highlighted and copied with ctrl-c
# Other tools:
# 	https://latlongdata.com/lat-long-converter/
# 	https://www.gps-coordinates.net/gps-coordinates-converter
# 🗺 💡 🧭 🚗 🔐
###