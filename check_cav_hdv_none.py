import os
import numpy as np

base_folder = "data_sfm"

penetrations = [
    "penetration_10",
    "penetration_20",
    "penetration_30"
]

print("=" * 90)
print("CHECKING LEADER AND FOLLOWER TYPES IN ALL FILES")
print("=" * 90)

for folder in penetrations:

    print("\n" + "=" * 90)
    print("FOLDER :", folder)
    print("=" * 90)

    folder_path = os.path.join(base_folder, folder)

    files = sorted(
        [f for f in os.listdir(folder_path) if f.endswith("_sfm.npz")],
        key=lambda x: int(x.split("_")[2])
    )

    for file in files:

        path = os.path.join(folder_path, file)

        data = np.load(path, allow_pickle=True)

        metadata = data["metadata"]

        leader_types = set()
        follower_types = set()

        for m in metadata:
            leader_types.update(m["leader"])
            follower_types.update(m["follower"])

        print("\n----------------------------------------")
        print("File :", file)
        print("----------------------------------------")
        print("Leader Types   :", sorted(leader_types))
        print("Follower Types :", sorted(follower_types))

print("\n" + "=" * 90)
print("CHECK COMPLETED")
print("=" * 90)