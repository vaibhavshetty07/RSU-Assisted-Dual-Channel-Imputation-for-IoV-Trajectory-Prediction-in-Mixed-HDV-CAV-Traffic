# RSU-Assisted-Dual-Channel-Imputation-for-IoV-Trajectory-Prediction-in-Mixed-HDV-CAV-Traffic
# SUMO IOV

## Overview
This repository contains a SUMO (Simulation of Urban Mobility) based Internet of Vehicles (IoV) project for generating and processing traffic simulation data. The project prepares Spatio-Temporal Feature Matrix (SFM) datasets for Connected and Autonomous Vehicle (CAV) research.

## Project Structure

```
SUMO IOV/
│── data_sfm/
│   ├── penetration_10/
│   ├── penetration_20/
│   └── penetration_30/
│
├── check_cav_hdv_none.py
├── delete_sfm_files.py
├── diagnostics.py
├── explore_dataset.py
├── inject_sfm.py
├── process_all_files.py
├── verify_sfm_files.py
└── README.md
```

## Features

- SUMO traffic simulation
- IoV scenario generation
- SFM dataset creation
- Different CAV penetration levels (10%, 20%, 30%)
- Dataset verification and diagnostics
- Data preprocessing utilities

## Requirements

- Python 3.x
- SUMO
- NumPy
- Pandas

## Usage

1. Generate SUMO simulation data.
2. Process the simulation files.
3. Verify the generated datasets.
4. Use the processed SFM data for further analysis or machine learning.

## Author

Vaibhav Shetty
