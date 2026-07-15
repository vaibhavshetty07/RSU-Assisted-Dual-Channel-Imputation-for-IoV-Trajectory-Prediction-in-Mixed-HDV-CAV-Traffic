import numpy as np

def inject_sfm(window, vehicle_types):

    corrupted = window.copy().astype(float)
    sfm_mask = np.ones((30, 7), dtype=float)

    for t in range(30):

        # Column 4 : Gap to Leader
        if vehicle_types["leader"][t] == "none":
            corrupted[t, 4] = np.nan
            sfm_mask[t, 4] = 0

        # Column 5 : Leader Speed
        if vehicle_types["leader"][t] in ["HDV", "none"]:
            corrupted[t, 5] = np.nan
            sfm_mask[t, 5] = 0

        # Column 6 : Follower Speed
        if vehicle_types["follower"][t] in ["HDV", "none"]:
            corrupted[t, 6] = np.nan
            sfm_mask[t, 6] = 0

    return corrupted, sfm_mask