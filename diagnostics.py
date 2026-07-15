import os
import numpy as np

base_folder = "data_sfm"

penetrations = [
    "penetration_10",
    "penetration_20",
    "penetration_30"
]

feature_names = [
    "ego_speed",
    "ego_accel",
    "ego_x",
    "ego_y",
    "gap_to_leader",
    "leader_speed",
    "follower_speed"
]

for penetration in penetrations:

    print("\n" + "=" * 60)
    print(penetration)
    print("=" * 60)

    folder_path = os.path.join(base_folder, penetration)

    files = sorted(
        [f for f in os.listdir(folder_path) if f.endswith("_sfm.npz")],
        key=lambda x: int(x.split("_")[2])
    )

    total_values = np.zeros(7, dtype=int)
    missing_values = np.zeros(7, dtype=int)

    for file in files:

        path = os.path.join(folder_path, file)

        data = np.load(path, allow_pickle=True)

        X = data["X_corrupted"]

        # X shape = (windows, 30, 7)

        for col in range(7):

            values = X[:, :, col]

            total_values[col] += values.size
            missing_values[col] += np.isnan(values).sum()

    for col in range(7):

        percent = (missing_values[col] / total_values[col]) * 100

        print(f"{feature_names[col]:15s}: {percent:.1f}% missing")

print("\n" + "=" * 60)
print("DIAGNOSTICS COMPLETED")
print("=" * 60)