import os
import numpy as np

root = "data_sfm"

print("=" * 80)
print("EXPLORING ALL DATASETS")
print("=" * 80)

# Loop through penetration folders
for folder in sorted(os.listdir(root)):

    folder_path = os.path.join(root, folder)

    if not os.path.isdir(folder_path):
        continue

    print("\n")
    print("=" * 80)
    print("FOLDER :", folder)
    print("=" * 80)

    # Sort run_seed_1, run_seed_2 ... run_seed_20 correctly
    files = sorted(
        [f for f in os.listdir(folder_path) if f.endswith(".npz")],
        key=lambda x: int(x.split("_")[-1].split(".")[0])
    )

    print("Total Files :", len(files))

    for file in files:

        path = os.path.join(folder_path, file)

        data = np.load(path, allow_pickle=True)

        X = data["X"]
        Y = data["Y"]
        metadata = data["metadata"]

        leader_types = set()
        follower_types = set()

        for m in metadata:
            leader_types.update(m["leader"])
            follower_types.update(m["follower"])

        print("\n----------------------------------------")
        print("File Name       :", file)
        print("----------------------------------------")
        print("Arrays Present  :", data.files)
        print("X Shape         :", X.shape)
        print("Y Shape         :", Y.shape)
        print("Metadata Shape  :", metadata.shape)
        print("Windows         :", X.shape[0])
        print("Timesteps       :", X.shape[1])
        print("Features        :", X.shape[2])
        print("Leader Types    :", sorted(leader_types))
        print("Follower Types  :", sorted(follower_types))

print("\n")
print("=" * 80)
print("ALL 60 FILES EXPLORED SUCCESSFULLY")
print("=" * 80)