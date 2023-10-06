import streamlit as st
from PIL import Image
from pathlib import Path
import pandas as pd
import altair as alt


def getPathInStreamlitDir():
    return Path(__file__).parents[1] / str('Streamlit/')


st.title('This is a test of Streamlit cloud from Deepnote through Github in OH today')

st.markdown('Hello World!')

img_name = 'smile.jpg'
img_path = getPathInStreamlitDir() / str('assets/' + img_name)
image = Image.open(img_path)


st.image(image)

st.markdown('The dataframe below is from a csv file that lives in `Streamlit/data`.')

csv_path = getPathInStreamlitDir() / str('data/IRIS.csv')

df_iris = pd.read_csv(csv_path)

st.dataframe(df_iris)

st.markdown("Now let's make an Altair plot for another example.")

plot = alt.Chart(df_iris).mark_point().encode(
  # Map the sepalLength to x-axis
    x = 'sepalLength',
  # Map the petalLength to y-axis
    y = 'petalLength',
    color = 'variety'
)

st.altair_chart(plot)