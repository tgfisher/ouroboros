import os, types, sys

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

RAW_DATA = os.path.join(os.path.dirname(__file__), os.path.realpath("../notebooks/raw_data"))

def img2bwarray(image_path, resolution_fraction=1):
    """
    Takes an image and returns a black and white image in the form of 
    a numpy array.
    """

    assert (0 < resolution_fraction) and (resolution_fraction <= 1), "resolution fraction must be (0,1]"

    bw_img = Image.open(image_path).convert("L")  # open convert to grey

    final_img_dims = [int(dim * resolution_fraction) for dim in bw_img.size]

    bw_mat = np.asarray(bw_img.resize(final_img_dims, Image.ANTIALIAS))

    return bw_mat

def text_into_array(arr, text_str, loc_tuple, fontsize, font_fill = 255):

    #TODO: normalize array for pil 0-255
    my_img = Image.fromarray(np.uint8(arr), "L")
    try:
        fontstr = "Arial.ttf"
        myfont = ImageFont.truetype(font=fontstr, size=fontsize)
    except OSError as e:
        print(f"You likely need to find a new font because your chosen font, {fontstr}, can't be found.")
        raise e

    draw_it = ImageDraw.Draw(my_img)
    draw_it.text(loc_tuple, text_str, font=myfont, fill = font_fill) 

    #TODO: reverse normalization (See above TODO)
    return np.asarray(my_img)
    
def arr_svd(arr, **kwargs):
    """
    identical to np.linalg.svd except (1) singular values are packaged into
    the appropriately sized matrix (2) it only handles 2D arr.

    see help for numpy.linalg.svd
    """
    assert len(arr.shape) == 2, f"Provided array has {len(arr.shape)} dims. This function is to make 2D svd more convenient, see np.linalg.svd for N-D svd"

    if kwargs.get("compute_uv") is False:
        s = np.linalg.svd(arr, **kwargs)
        S = np.zeros((arr.shape[0], arr.shape[1]))
        S[:s.size, :s.size] = np.diag(s)
        return S
    else:
        U, s, VH = np.linalg.svd(arr, **kwargs)
        S = np.zeros((U.shape[1], VH.shape[0]))
        S[:s.size, :s.size] = np.diag(s)
        return U, S, VH


def lowrank_reconstruct(U, S, VH, *, end_s_vec = None, start_s_vec = 0, alert=True):
    """

    U @ S @ VH = M
    rxn nxm  mxc  rxc

    By dropping rows of columns of U and rows of VH we can get a lowrank reconstruction.
    The best (least squares) approximation of the matrix U @ S @ VH at a particular rank
    will be choosing the columns and vectors associated with the largest singular values
    (e.g. the best rank 2 reconstruction is U[:2,:] @ S[:2,:2] @ VH[:,:2]).

    If S is not square, reconstruction should ignore the "zeroed out" dimensions
    of the larger singular vector matrix.

    n < m 
    uu  sss  vvv
    uu  sss  vvv
             vvv
    --2 < 3, n_svals is 2--

    m < n
    uu  ss  vvv
    uu  ss  vvv
    uu   
    --2 < 3, n_svals is 2--

    """
    # by default there shouldn't be an announcment about slice
    slice_warning = False
    slice_str = f"{start_s_vec}:{end_s_vec}"
    # Shape of U @ S @ VH determines number of singular values
    n_svals = min(U.shape[1], VH.shape[0])
    
    # prevent indexing into "zeroed out" singular vecotors and values
    if start_s_vec < 0:
        start_s_vec = n_svals + start_s_vec
        slice_warning= True

    if end_s_vec is None:
        end_s_vec = n_svals - 1 # counts include zero indes, must be + 1 corrected
    elif end_s_vec < 0:
        end_s_vec = n_svals + end_s_vec - 1
        slice_warning = True

    if alert and slice_warning: 
        print(
            "Assuming you'd like to ignore zeroed out s_vectors, referencing your",
            f"slicing\n\tfrom then_svals available. Selecting [{start_s_vec}:{end_s_vec}]",
            f"from the provided [{slice_str}]."
        )

    lw_arr = np.dot(
        U[:, start_s_vec:end_s_vec + 1],
        np.dot(
            S[start_s_vec:end_s_vec + 1, start_s_vec:end_s_vec + 1],
            VH[start_s_vec:end_s_vec + 1, :],
        ),
    )

    return lw_arr
    
def bw_plot(arr, vmin=None, vmax=None):
    """
    plot an array with gray cmap.

    see matplotlib.pyplot.imshow for vmin, vmax explanation.
    """

    print("Minimum Pixel:", arr.min(), "\nMaximum Pixel:", arr.max())
    fig, ax = plt.subplots()
    ax.imshow(arr, cmap='gray', vmin=vmin, vmax=vmax)
    plt.show()

    return fig, ax

def lr_plot(U, S, VH, end_s_vec = None, start_s_vec=0, vmin=None, vmax=None):
    """
    combine bw_plot and lowrank_reconstruct for oneline reconstruct and plot.

    ** default params **
    see lowrank_reconstruct for end_s_vec and start_s_vec params
    see matplotlib.pyplot.imshow for vmin and vmax params
    """
    lr = lowrank_reconstruct(U, S, VH, end_s_vec=end_s_vec, start_s_vec=start_s_vec)
    fig, ax = bw_plot(lr, vmin=vmin, vmax=vmax)

    return fig, ax

def s_val_plot(*singmats, dim=None):
    """
    make a scree plot of singular values
    """
    fig, ax = plt.subplots()
    for S in singmats:
        sd = np.diag(S)
        if dim is not None:
            ax.plot(sd[:dim])
        else:
            ax.plot(sd)
    plt.show()


def s_val_cum_sum(*singmats, dim=None):
    """
    cumulative (for each) scree plot
    """
    fig, ax = plt.subplots()
    for this_singmat in singmats:
        sd = np.diag(this_singmat)
        perc_var = sd / np.sum(sd)
        cum_sum = np.cumsum(perc_var)
        if dim is not None:
            ax.plot(cum_sum[:dim], 'o')
        else:
            ax.plot(cum_sum)
    plt.show()

def swap_s_vecs_top2bottom(Ua, Sa, VHa, Ub, Sb, VHb, swp_from):
    """
    swap top singular vectors of b, with the bottom singular vectors
    of a. The weights must also be properly relative to one another.
    """

    if not sys.warnoptions:
        warn_string = (
                "Note this performs VERY badly if not at all after reconstruction, it is just "
                "a quick (and poor) implementation. The singular vectors\n"
                "getting swapped aren't enforced to be orthogonal so reconstruction "
                "will likely rotate, reorder, and shrink/stretch what you swap in."
        )
        import warnings
        warnings.warn(
            warn_string,
            UserWarning,
            stacklevel = 2,
        )

    assert 0 <= swp_from, "swp_from must be positive"
    assert Ua.shape == Ub.shape, "Left singular vectors (U) dims don't match"
    assert VHa.shape == VHb.shape, "Right singular vectors (VH) dims don't match"

    # shape of U @ S @ VH determines number of singular values
    n_svals = min(Ua.shape[0], VHa.shape[1])
    
    Uout = Ua.copy()
    Sout = Sa.copy()
    VHout = VHa.copy()

    # setup slice variables here b/c this is a little confusing
    # svd for a non-square matrix has som zero-valued singular values
    #   so we must do a little more work here to get the indexing right.
    top_swap_start = 0
    top_swap_end = swp_from

    bottom_swap_start = n_svals - swp_from
    bottom_swap_end = n_svals
    
    # For proper singular vector balance, replaced vectors must be
    # transferred with ratiometrically matching singular values
    # otherwise the reconstruction of those dims won't "look right"
    Sa_vec = np.diag(Sa)
    Sb_vec = np.diag(Sb)
    Sb_swap_vec = Sb_vec.copy()[:top_swap_end] # we care about the top s val ratios of b
    Sb_swap_ratios = Sb_swap_vec / np.sum(Sb_swap_vec)
    
    h = (Sa_vec[bottom_swap_start] - Sa_vec[-1]) / (Sa_vec.size - bottom_swap_start)
    Sa_replace = normalize_shift(Sb_swap_ratios, Sa_vec[bottom_swap_start-1], 0)

    # replace bottom of a with top of b
    Sout[bottom_swap_start:bottom_swap_end, bottom_swap_start:bottom_swap_end] = np.diag(Sa_replace) # replace bottom of a
    Uout[:, bottom_swap_start:bottom_swap_end] = Ub[:, :top_swap_end] 
    VHout[bottom_swap_start:bottom_swap_end, :] = VHb[:top_swap_end, :] 

    return Uout, Sout, VHout

def normalize_shift(values, high, low):
    """
    minmax norm followed by scale and shift
    """

    mmnorm_vals = (values - values.min()) / (values.max() - values.min())
    spread_vals = mmnorm_vals * (high - low)

    return spread_vals + low

def norm_multiplot(*lines, norm=True):
    fig, ax = plt.subplots()
    for a_line in lines:
        if norm:
            norm_line = normalize_shift(a_line, 1, 0)
            ax.plot(norm_line)
        else:
            ax.plot(a_line)
    plt.show()

if __name__ == "__main__":
    hide_start = -1100
    ## get image from provided path argument
    try:
        bw_arr = np.load(os.path.join(RAW_DATA, "bw_arr.npy"))
        bw_loadz = np.load(os.path.join(RAW_DATA, "bw_arr_svd.npz"))
        Ubw, Sbw, VHbw = [bw_loadz[key] for key in ("U","S","VH")]
    except:
        print("loading from scratch, must provide an image path with script call")
        img_path = sys.argv[1]
        bw_arr = img2bwarray(img_path, resolution_fraction=.4)
	np.save(os.path.join(RAW_DATA, "bw_arr.npy"), full_recon)
	print("saved a copy of the array for next time.")
        Ubw, Sbw, VHbw = arr_svd(bw_arr)
	np.savez(os.path.join(RAW_DATA, "bw_arr_svd.npz"), U=Ubw, S=Sbw, VH=VHbw)
	print("saved SVD for next time")

    print("done loading and svd of image")
    
    ## make secret message
    scale = 1
    text_arr = np.random.random(bw_arr.shape) * scale
    text_arr_mask = text_into_array(
        np.zeros(text_arr.shape),
        "You Found Me!",
        (10,100),
        200,
        font_fill = 1,
    ).astype(bool)
    text_arr[text_arr_mask] = -scale
    Utxt, Stxt, VHtxt = arr_svd(text_arr)
    print("done making and svd of message")

    ## hide message at small singular values
    Um, Sm, VHm = swap_s_vecs_top2bottom(Ubw, Sbw, VHbw, Utxt, Stxt, VHtxt, -hide_start)
    full_recon = Um @ Sm @ VHm
    print("done hiding and rebuilding full_recon")

    ## because swap_s_vecs_top2bottom is quick and dirty, we must reconstruct and loose
    ## clarity of message.
    Uh, Sh, Vh = arr_svd(full_recon)
    print("done svd full_recon")

    lr_plot(Uh, Sh, Vh, start_s_vec=hide_start)
    bw_plot(full_recon)
    np.save(os.path.join(RAW_DATA, "bw_arr_pm.npy"), full_recon)
    print("done showing and saving 'bw_arr_pm.npy' for assignment.")
