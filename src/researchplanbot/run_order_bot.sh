# Initialize the virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the required packages
python3 -m pip install -r requirements.txt

# Run the Kafka stream
python3 main.py