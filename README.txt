Program makes use of Selenium WebDriver. There is a directory in the source code to chromedriver.exe. 
This has to be updated for the user if the code is to run.
Link to exe: https://chromedriver.storage.googleapis.com/index.html?path=89.0.4389.23/

List of currently working hotels as of 4/5/2021:
Tower Hotel // This website has no anti scraping measures. If tool is run after 3rd June 2021, code will not work as those are the booking dates.
Mayflower // This website will randomly change booking page URL and HTML class for the price, may take more than one try to run, expect error
Mornington // This website will randomly change booking page URL, may take more than one try to run, expect error

EXE file is compiled with pyinstaller library. Can be installed with 'pip install pyinstaller'

If trying to run on your PC, update source code with directory to chromedriver.exe,

Then run pyinstaller --onefile combo.py at directory of file from cmd.