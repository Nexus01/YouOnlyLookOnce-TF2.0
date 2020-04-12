# Automatically setup for CrowdHuman dataset
pip install -r requirements.txt

# Download CrowdHuman dataset
cd data


# Unzip


# Generate CrowdHuman lists

python crowdhuman_train_anno.py

# Generate PASCAL lists for YOLO
cd ../tool
python preprocess_crowdhuman.py

# Finish
cd ../src

# Start Training
# python main.py
