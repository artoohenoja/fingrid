# PowerShell script to set up virtual environment, install packages, and run Python script

# Set the path to the Python script
$pythonScriptPath = ".\fingrid.py"

# Set up virtual environment
python -m venv venv

# Activate the virtual environment
$venvPath = ".\venv\Scripts\Activate"
& $venvPath

# Install required packages
pip install requests

# Run the Python script
python $pythonScriptPath

# Deactivate the virtual environment
deactivate
