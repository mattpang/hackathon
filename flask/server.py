from flask import Flask, render_template

app = Flask(__name__)
names={0:'default',1:'Matt',2:'Talia',3:'Toby',4:'Ben'}

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/profile')
@app.route('/profile/<id>')
def render_profile(id=0):
    return render_template('profile.html',name=names[int(id)])

#app.run(debug=True)
# showing the plotting parts:

import plotly
import plotly.express as px
import seaborn as sns
import json
df = sns.load_dataset("penguins")

def make_plotly_plot(df):
    fig = px.scatter(
                data_frame=df,
                x="bill_depth_mm",
                y="bill_length_mm",
                color="species",
                title="Bill Depth by Bill Length",
            )
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

@app.route("/plots")
def plotter():
    return render_template('plot.html',graphJSON=make_plotly_plot(df))

app.run(debug=True)