import plotly
import plotly.graph_objs as go
import numpy as np
import panda as pd

fn = 'mt_bruno_elevation.csv'
Z = np.loadtxt(fn,delimiter=',',skiprows=1,usecols=range(1,25))
data = [go.Surface(z = Z)]
fig = go.Figure(data=data)
plotly.offline.plot(fig, filename='elevations-3d-surface.html')