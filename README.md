Please note that the PowerShell script assumes you have Python and pip installed on your system. If you encounter any issues or have additional questions, feel free to ask!

## POWERSHELL:

1. Open a PowerShell command prompt or PowerShell ISE on your computer.

2. Navigate to the directory where both the PowerShell script (GetFingridDatasetData.ps1) and the Python script (fingrid.py) are located.

3. Run the PowerShell script by entering the following command:

.\GetFingridDatasetData.ps1

If you encounter an execution policy issue, you may need to run the following command with administrator privileges before running the script:

Set-ExecutionPolicy RemoteSigned

If you continue to encounter an execution policy issue, please verify in File Explorer that the file GetFingridDatasetData.ps1 is not locked.

After running the script, you can revert the execution policy to a more restrictive setting:

Set-ExecutionPolicy Restricted

4. The script will prompt you to enter the required information, such as the API key, start date, end date, and dataset ID.

5. Follow the on-screen instructions to provide the necessary input.

6. The script will create a virtual environment, install the required Python packages, and execute the fingrid.py script.

7. Once the script completes, the virtual environment will be deactivated.


CMD:

## CMD:

1. Open a Command Prompt (CMD) window.

2. Navigate to the directory where both the PowerShell script (`GetFingridDatasetData.ps1`) and the Python script (`fingrid.py`) are located. Use the `cd` command to change the directory.

3. Execute the Fingrid Data Retrieval script using the following command:

powershell -File GetFingridDatasetData.ps1

if you encounter "cannot be loaded because running scripts is disabled on this system" you may need to run the following command with administrator privileges before running the script:

powershell Set-ExecutionPolicy RemoteSigned

If you continue to encounter an execution policy issue, please verify in File Explorer that the file GetFingridDatasetData.ps1 is not locked.

4. ## Go to ## POWERSHELL: part 4.


