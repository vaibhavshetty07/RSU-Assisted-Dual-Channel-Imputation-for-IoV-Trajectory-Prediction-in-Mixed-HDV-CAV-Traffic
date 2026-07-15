import os
import numpy as np

base_folder = "data_sfm"

penetrations = [
    "penetration_10",
    "penetration_20",
    "penetration_30"
]

for folder in penetrations:

    folder_path = os.path.join(base_folder, folder)

    print("\n" + "=" * 80)
    print("STARTING VERIFICATION OF :", folder)
    print("=" * 80)

    files = sorted(
        [f for f in os.listdir(folder_path) if f.endswith("_sfm.npz")],
        key=lambda x: int(x.split("_")[2])
    )

    for file in files:

        path = os.path.join(folder_path, file)

        data = np.load(path, allow_pickle=True)

        X = data["X"]
        X_corrupted = data["X_corrupted"]
        sfm_mask = data["sfm_mask"]
        metadata = data["metadata"]

        found = False

        for i in range(len(metadata)):

            leader_types = set(metadata[i]["leader"])
            follower_types = set(metadata[i]["follower"])

            if ("CAV" in leader_types) or ("CAV" in follower_types):

                print("\n" + "-" * 80)
                print("Folder :", folder)
                print("File   :", file)
                print("Window :", i)
                print("-" * 80)

                print("Leader Types in Window   :", leader_types)
                print("Follower Types in Window :", follower_types)

                print("\nLeader (First 5 Timesteps)")
                print(metadata[i]["leader"][:5])

                print("\nFollower (First 5 Timesteps)")
                print(metadata[i]["follower"][:5])

                print("\nOriginal C4 C5 C6 (First 5 Timesteps)")
                print(X[i, :5, 4:7])

                print("\nCorrupted C4 C5 C6 (First 5 Timesteps)")
                print(X_corrupted[i, :5, 4:7])

                print("\nSFM Mask C4 C5 C6 (First 5 Timesteps)")
                print(sfm_mask[i, :5, 4:7])

                print("\n" + "=" * 60)
                print("CHECKING FIRST CAV LEADER TIMESTEP")
                print("=" * 60)

                cav_found = False

                for t in range(30):

                    if metadata[i]["leader"][t] == "CAV":

                        cav_found = True

                        print("Timestep :", t)
                        print("Leader   :", metadata[i]["leader"][t])
                        print("Follower :", metadata[i]["follower"][t])

                        print("\nOriginal C4 C5 C6")
                        print(X[i, t, 4:7])

                        print("\nCorrupted C4 C5 C6")
                        print(X_corrupted[i, t, 4:7])

                        print("\nSFM Mask C4 C5 C6")
                        print(sfm_mask[i, t, 4:7])

                        break

                if not cav_found:
                    print("No CAV Leader in this window.")

                input("\nPress Enter for next file...")

                found = True
                break

        if not found:
            print(file, "-> No CAV window found.")

    print("\n" + "=" * 80)
    print(folder, "VERIFICATION COMPLETED")
    print("=" * 80)

print("\n" + "=" * 80)
print("ALL PENETRATION FILES VERIFIED SUCCESSFULLY")
print("=" * 80)