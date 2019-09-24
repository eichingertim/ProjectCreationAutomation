# Project Creation Automation for WINDOWS
## How to install
Goto your command-line (cmd) and navigate to the location where you want to clone this project. Then type:
```bash
git clone git clone "https://github.com/eichingertim/ProjectCreationAutomation.git"
cd ProjectCreationAutomation
pip install -r requirements.txt
```
Then edit the two files **create.bat** (inside batch-folder) and **scripty.py** where necessary (marked and described with comments). 

After that check which version of Google's Chrome Browser you have installed and download the corresponding **webdriver** from the following website (https://sites.google.com/a/chromium.org/chromedriver/downloads) and unzip it.

**IMPORTANT**: Now you have to put the path of the **create.bat**-file (e.g. C:\User\...\ProjectCreationAutomation\batch) and the path of the just downloaded **webdriver** to your SYSTEM-PATH. Here is a short instruction how to do this:
1. type **env** to your windows-search and hit enter. A dialog with system-properties should appear.
2. Click on the Button with **Environment Variables**
3. In the System Variables window, highlight **Path**, and click **Edit**.
4. In the Edit System Variables window, insert the cursor at the end of the Variable value field.
5. If the last character is not a semi-colon (;), add one.
6. After the final semi-colon, type the full path to the file you want to find
7. Click **OK** in each open windows

## How to use it
To create a new project just open your command-line (cmd) and type in a command with the following syntax:
```bash
create <ProjectName> <private/public>
```
* **ProjectName**: Write here your new project's name without space
* **private/public**: Write here if you want your project to be public or private on github.
