:: ENTER PATH WHERE THE script.py IS LOCATED
cd <PATH>

python script.py %1 %2

:: ENTER PATH WHERE YOUR PROJECTS ARE SAVED
:: e.g. C:/User/<USERNAME>/Documents/Projects
cd <PATH>\%1


git init

::ENTER YOUR GIT USERNAME
git remote rm origin
git remote add origin https://github.com/<USERNAME>/%1.git

echo # %1 > README.md
git add .
git commit -m "initial commit"
git push -u origin master

:: OPENS VISUAL STUDIO CODE
code .