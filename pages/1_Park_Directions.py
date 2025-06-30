# This is a supplmentary page to Home_MC_Parks_Map.py app because it's under /pages/ subdir and is prefixed with "1_<scriptFile>.py" in that subdir
# which makes streamlit automatically add it as a page and its link on a sidebar menu from the main Home_MC_Parks_Map.py page.
# Its purpose is to allow getting directions to a selected park (from dropdown list).
# The dataframe is the same as in Home_MC_Parks_Map.py

# IMPORTANT: This script and image are in inside pages/ subdir but since it's made a page of the main Home_MC_Parks_Map.py page which is in the root directory we need to specify
# the pages/ path for the image from here!

import streamlit as st
import pandas as pd

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
        'American Legion Memorial Park (Everett)'
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
            48.016112
            
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
            -122.203424
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
        'Trails, BBQ, Baseball Field, Basketball Court, Tennis Court, Picnic Area, Restroom, Playground, Gardens, Arboretum'
    ]
})


st.write("### Directions to Parks & Recreation Areas")

selected_park = st.selectbox(f"Select a park, then click its Directions link below: {len(df)} locations", sorted(df['Park']))
park_row = df[df['Park'] == selected_park].iloc[0]

st.markdown(
    f"Selected: 📍{selected_park}| {park_row['features']} 🚗 [🧭 Directions](https://www.google.com/maps/search/?api=1&query={park_row['lat']},{park_row['lon']})",
    unsafe_allow_html=True
)

# NOTE: Google Maps shows coordinates in Degrees, Minutes, Seconds (DMS) format, but our dataframe needs Decimal Degrees (DD).
# To get DD format from Google maps, locate in maps, right-click on the pin marker to see the DD values (drag mouse until next row in the popup to copy the coordinates text).
# Or better: right-click and Share...a popup window opens where the DD format is shown that can be highlighted and copied with ctrl-c
# Other tools:
# 	https://latlongdata.com/lat-long-converter/
# 	https://www.gps-coordinates.net/gps-coordinates-converter