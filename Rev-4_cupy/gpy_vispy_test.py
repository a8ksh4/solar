#!/usr/bin/env python
'''foo'''

# import cupy as cp
# import numpy as np
# from vispy import app, visuals, scene

# # Create real-time data in CuPy arrays
# data_size = 1000
# x = cp.random.rand(data_size)
# y = cp.random.rand(data_size)

# # Create a canvas for visualization
# canvas = scene.SceneCanvas(keys='interactive', show=True)
# view = canvas.central_widget.add_view()
# scatter = scene.visuals.Markers()

# # Add scatter plot to the view
# view.add(scatter)

# # Set the view parameters (camera and axes)
# view.camera = 'panzoom'
# scatter.set_gl_state('translucent', depth_test=False)
# scatter.antialias = 0

# # Update the scatter plot with real-time data
# def update(ev):
#     global x, y
#     # Update CuPy arrays with new data
#     x[:] = cp.random.rand(data_size)
#     y[:] = cp.random.rand(data_size)

#     # Use GPU-accelerated data directly in the visualization
#     scatter.set_data(cp.asnumpy(cp.column_stack((x, y))),
#                      dge_color=None,
#                      face_color=(1, 1, 1, 1),
#                      size=5)

# # Timer for real-time updates
# timer = app.Timer(interval=0.1, connect=update, start=True)

# if __name__ == '__main__':
#     app.run()

import numpy as np

import vispy.plot as vp

np.random.seed(2324)
n = 100000
data = np.empty((n, 2))
lasti = 0
for i in range(1, 20):
    nexti = lasti + (n - lasti) // 2
    scale = np.abs(np.random.randn(2)) + 0.1
    scale[1] = scale.mean()
    data[lasti:nexti] = np.random.normal(size=(nexti-lasti, 2),
                                         loc=np.random.randn(2),
                                         scale=scale / i)
    lasti = nexti
data = data[:lasti]


color = (0.3, 0.5, 0.8)
n_bins = 100

fig = vp.Fig(show=False)
line = fig[0:4, 0:4].plot(data, symbol='o', width=0,
                          face_color=color + (0.02,), edge_color=None,
                          marker_size=4)
line.set_gl_state(depth_test=False)
fig[4, 0:4].histogram(data[:, 0], bins=n_bins, color=color, orientation='h')
fig[0:4, 4].histogram(data[:, 1], bins=n_bins, color=color, orientation='v')

if __name__ == '__main__':
    fig.show(run=True)
