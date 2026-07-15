import os
import numpy as np
from 02_inject_sfm import inject_sfm

base_folder = "data_sfm"

penetrations = [
    "penetration_10",
    "penetration_20",
    "penetration_30"
]

for folder in penetrations:

    folder_path = os.path.join(base_folder, folder)

    print("\n" + "=" * 60)
    print("Processing :", folder)
    print("=" * 60)

    files = sorted(
        [f for f in os.listdir(folder_path)
         if f.endswith(".npz") and "_sfm" not in f],
        key=lambda x: int(x.split("_")[-1].split(".")[0])
    )

    for file_name in files:

        file_path = os.path.join(folder_path, file_name)

        data = np.load(file_path, allow_pickle=True)

        X = data["X"]
        Y = data["Y"]
        metadata = data["metadata"]

        X_corrupted = []
        sfm_mask = []

        for i in range(len(X)):

            corrupted, mask = inject_sfm(X[i], metadata[i])

            X_corrupted.append(corrupted)
            sfm_mask.append(mask)

        X_corrupted = np.array(X_corrupted)
        sfm_mask = np.array(sfm_mask)

        save_name = file_name.replace(".npz", "_sfm.npz")
        save_path = os.path.join(folder_path, save_name)

        np.savez(
            save_path,
            X=X,
            Y=Y,
            metadata=metadata,
            X_corrupted=X_corrupted,
            sfm_mask=sfm_mask
        )

        print("Saved :", save_name)

print("\n" + "=" * 60)
print("ALL 60 FILES PROCESSED SUCCESSFULLY")
print("=" * 60)