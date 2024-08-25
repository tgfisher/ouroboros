import matplotlib.pyplot as plt

def hello_world():
    
    monitor_scale = .9
    box_x = [-1,-1,1,1,-1,-1]
    box_y = [0,1,1,-1,-1,0]
    inner_box_x = [val * monitor_scale for val in box_x]
    inner_box_y = [val * monitor_scale for val in box_y]
    fig, ax = plt.subplots()
    ax.plot(box_x, box_y, 'grey', linewidth=20)
    ax.fill(inner_box_x, inner_box_y, 'g', linewidth=10, alpha=.5)
    ax.text(
        inner_box_x[1],
        inner_box_y[1] * monitor_scale,
        "In [0]:  simple_hello()\n hello world",
        verticalalignment="top",
    )
    ax.axis("off")
    plt.show()
