import streamlit as st


# Create the interface
st.title("YourData X CoursePlus")
st.write('Demo version')
# Show the data as a table
def page_0():
    st.empty()
def page_2():
    st.empty()

def page3():
    st.empty()

def page4():
     st.empty()

page_names_to_funcs = {
    "🏠Home": page_0,
    "Global Picture": page_2,
    "2_Where": page3,
    "cluster" :page4
}




