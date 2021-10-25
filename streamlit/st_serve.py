#do streamlit run st_serve.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title('Hello world!')

st.markdown("""
### subheading 

- stuff
- goes
- here

In **fancy** markdown

""")

#means the function won't run for another hour.
#@st.cache(ttl=3600) 
def load_penguins():
    import seaborn as sns
    return sns.load_dataset("penguins")

df = load_penguins()

def make_plot(df):
    fig, ax = plt.subplots()
    df["color"] = df["species"].replace(
        {"Adelie": 1, "Chinstrap": 2, "Gentoo": 3})
    ax.scatter(x=df["bill_depth_mm"], y=df["bill_length_mm"], c=df["color"])
    plt.title("Bill Depth by Bill Length")
    plt.xlabel("Bill Depth (mm)")
    plt.ylabel("Bill Length (mm)")
    return fig

fig = make_plot(df)
st.pyplot(fig)

fig_plotly = px.scatter(
                data_frame=df,
                x="bill_depth_mm",
                y="bill_length_mm",
                color="species",
                title="Bill Depth by Bill Length",
            )
st.plotly_chart(fig_plotly)
    
