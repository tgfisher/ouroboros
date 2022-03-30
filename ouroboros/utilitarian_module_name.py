import numpy as np
import matplotlib.pyplot as plt

def hello_world():
    print("hello world")

def make_nXt(n_neurons, n_spikes=5):

    neuronsXtime = np.zeros((n_neurons, n_spikes))
    for neuron in range(n_neurons):
        times = np.random.uniform(size=n_spikes)
        times.sort()
        neuronsXtime[neuron, :] = times

    return neuronsXtime

def some_plot(neuronsXtime):
    fig, ax = plt.subplots()
    ## vv add plotting code below vv ##


CLRS = ['purple','red','green','blue','k']
def twoDvectors(
    vector_array,
    axis_lim,
    size=[3, 3],
    gridstep=1,
    clrs=CLRS,
    axes_handle=None,
    tip_to_tail=False,
):
    """
    draws 2-D vectors. Vectors are provided as an array.
    """

    # check for imag values 
    assert not np.iscomplex(vector_array).any(), "no support for imag plot atm"  #TODO

    f_height, f_width = size

    if (axes_handle == None):
        fig, axes_handle = plt.subplots(figsize=(f_height, f_width))
    else:
        fig = axes_handle.get_figure()



    origin = [0, 0]
    arrow_thickness = max(axis_lim) / 50
    if len(vector_array.shape) == 1:
        vector_count = 1
        dimensions = vector_array.shape[0]
        axes_handle.arrow(
            origin[0],
            origin[1],
            vector_array[0],
            vector_array[1],
            length_includes_head=True,
            width=arrow_thickness,
            color=clrs[0],
        )
    else:
        dimensions, vector_count = vector_array.shape
        for idx in range(vector_count):
            axes_handle.arrow(
                origin[0],
                origin[1],
                vector_array[0, idx],
                vector_array[1, idx],
                length_includes_head=True,
                width=arrow_thickness,
                color=clrs[idx],
            )
            if tip_to_tail:
                origin += vector_array[:,idx]

    ticks = np.arange(axis_lim[0], axis_lim[1] + gridstep, step=gridstep)
    axes_handle.set_xticks(ticks)
    axes_handle.set_yticks(ticks)
    axes_handle.spines["left"].set_position("zero")
    axes_handle.spines["bottom"].set_position("zero")
    axes_handle.spines["right"].set_color("none")
    axes_handle.spines["top"].set_color("none")
    axes_handle.grid(
        True,
        linestyle="dashed",
        clip_on=False, # since the perspective can shift, need grid on the bottom too.
    )
    axes_handle.set_axisbelow(True)
    axes_handle.set_xlim(axis_lim[0], axis_lim[1] * 1.01)
    axes_handle.set_ylim(axis_lim[0], axis_lim[1])

    return fig

if __name__ == "__main__":
    print("yes I'm here")
