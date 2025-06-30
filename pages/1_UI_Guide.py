# This is a supplmentary page to Home_MC_Parks_Map.py app because it's under /pages/ subdir and is prefixed with "1_<scriptFile>.py" in that subdir
# which makes streamlit automatically add it as a page and its link on a sidebar menu from the main Home_MC_Parks_Map.py page.
# Its purpose is to show an image for the users with UI navigation tips of the main map.

# IMPORTANT: This script and image are in inside pages/ subdir but since it's made a page of the main Home_MC_Parks_Map.py page which is in the root directory we need to specify
# the pages/ path for the image from here!

import streamlit as st

# Page title
st.write("## How to navigate the interactive map")

# Show image from a local file
st.image("pages/parks_map_UI.jpg", caption="Map UI Navigation", use_column_width=True) 

# Optional text
# st.write("This interactive map showcases community parks, markets, and more!")
# Show image from a web URL
#st.image("https://example.com/image.jpg", caption="Online Image Example", use_column_width=True)

st.write("You can also double-click/tap a location on the interactive map to zoom in.")
st.markdown("[⬅️ 🗺 Back to Map](Home_MC_Parks_Map)", unsafe_allow_html=True)
# NOTE: Home_MC_Parks_Map.py is the actual root page file name, so we specify without the py extension here.
# Also, the side bar item will appear as Home MC Parks Map...spaces instead of underscores in the UI display automatically by streamlit.
# And to refer to it as a link with st.markdown, remove any prefix number and extension (.py) but keep the underscores as in original file name!


