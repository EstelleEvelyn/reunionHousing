# reunionHousing

A script designed to generate the necessary spreadsheets to track Reunion housing. 

First, run this program by typing the usage statement above into the command line. When prompted for a masterList file, input the name of the file ResLife provides. I recommend making a copy of it in the same folder this program resides in and naming it with no spaces. 

Second, once the program has terminated (indicated by an “All done!” message in the terminal window), import the generated CSV files into an excel workbook or Google Sheet (“file” > “import” > “upload”), along with the masterList. This should create the necessary spreadsheets to assign and track Reunion housing. You will still have to manually copy any sheets whose buildings were not provided by ResLife, e.g. AGH.

In order to adjust this program for future use, update ONLY the class years in the data structures named “housingKeyDict” and “areaList”. It is vital that the values after colons (:) in housingKeyDict and the items in areaList match each other EXACTLY, or the program will encounter errors and will stop running.

Additionally, the column names used by ResLife in the masterList must remain the same from year to year in order for this to work, unless someone correctly updates those values in the writerow line.
