"""
Usage: python3 reunionHousing.py
@author Estelle Bayer, 01/19

A script designed to generate the necessary spreadsheets to track Reunion housing.

First, run this program by typing the usage statement above into the command line. When prompted for a masterList file, input the name of the file ResLife provides. I recommend making a copy of it in the same folder this program resides in and naming it with no spaces.

Second, once the program has terminated (indicated by an “All done!” message in the terminal window), import the generated CSV files into an excel workbook or Google Sheet (“file” > “import” > “upload”), along with the masterList. This should create the necessary spreadsheets to assign and track Reunion housing. You will still have to manually copy any sheets whose buildings were not provided by ResLife, e.g. AGH.

In order to adjust this program for future use, update ONLY the class years in the data structures named “housingKeyDict” and “areaList”. It is vital that the values after colons (:) in housingKeyDict and the items in areaList match each other EXACTLY, or the program will encounter errors and will stop running.

Additionally, the column names used by ResLife in the masterList must remain the same from year to year in order for this to work, unless someone correctly updates those values in the writerow line.
"""


import csv

"""
@arg areaList: a list of strings corresponding to the names of areas

Creates a new CSV file for each area and writes a header row to each one.
"""
def createCSV(areaList):

  	#Information we need to track as columns in our new spreadsheets
	fieldnames = ["Code", "Building", "Room", "Room Type", "Capacity", "Guest",
				"Notes", "Adj Rm", "Room Key", "Outside Key", "Keycard #",
				"Card Returned", "Key Returned", "Key Notes"]

	for housingArea in areaList:
		with open(housingArea+'.csv', 'w') as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()

"""
@arg masterListCSV: a CSV file provided by ResLife containing information on all of the housing used for Reunion

Iterates through every room in the master file and adds it to the CSV corresponding to the appropriate area. Rooms are added as many times as they have capacity to house (e.g. a double will be added twice, a triple three times, etc.)
"""
def extractRoomData(masterListCSV):

  	#Only update the appropriate years in this list
	housingKeyDict = {"ALLE":"Unassigned", "BENT":"Benton,Huntington \'08",
					"BERG":"Berg \'08,Hunt Cottage \'93", "BRKS":"North TH \'84, \'94",
					"BURT":"Burton \'94", "CASS":"Cassat \'79, \'69, \'99",
					"CHAN":"Fac Club,Chaney \'08", "CLWL":"South TH \'74",
					"COLR":"North TH \'84, \'94", "DAVI":"Davis \'54, \'59",
					"DIXN":"South TH \'74", "DOUG":"Parish,Douglas \'09",
					"DOWH":"South TH \'74", "EUGS":"North TH \'84, \'94",
					"EVAN":"Evans \'04", "FACL":"Fac Club,Chaney \'08",
					"FARM":"Unassigned", "GFRT":"Unassigned", "GHUE":"Goodhue \'14",
					"HALL":"North TH \'84, \'94", "HCTG":"Berg \'08,Hunt Cottage \'93",
					"HNRK":"South TH \'74", "HNTH":"South TH \'74",
					"HUNT":"Benton,Huntington \'08", "JEWE":"Jewett,Page W,Rice,Wade \'09",
					"JMES":"James \'99", "MUSS":"Musser - Student Housing",
					"MYER":"Myers \'89", "NASN":"North TH \'84, \'94",
					"NOUR":"Nourse \'64, \'69", "OWNS":"North TH \'84, \'94",
					"PAGE":"Unassigned", "PAGW":"Jewett,Page W,Rice,Wade \'09",
					"PARR":"Unassigned", "PREN":"Unassigned", "PRSH":"Parish,Douglas \'09",
					"RICE":"Jewett,Page W,Rice,Wade \'09", "SCOT":"North TH \'84, \'94",
					"SEVY":"Sevy \'94", "STIM":'Unassigned',
					"WADE":"Jewett,Page W,Rice,Wade \'09", "WATS":"Watson \'69",
					"WILM":"Unassigned", "WILS":"Unassigned"}

  	#Information we need to track as columns in our new spreadsheets
	fieldnames = ["Code", "Building", "Room", "Room Type", "Capacity", "Guest",
				"Notes", "Adj Rm", "Room Key", "Outside Key", "Keycard #",
				"Card Returned", "Key Returned", "Key Notes"]


	with open(masterListCSV, 'r') as masterFile:
		reader = csv.DictReader(masterFile)
		for room in reader:
		  	#Find the appropriate spreadsheet to add this room to
			areaName = housingKeyDict[room['Building Code']]
			#Figure out how many times this room needs to be added to the spreadsheet
			capacity = int(room['Capacity'])
			with open(areaName+'.csv', 'a') as subFile:
				writer = csv.DictWriter(subFile, fieldnames=fieldnames)
				for i in range(capacity):
					writer.writerow({"Code":room["Bldg/Room"], "Building":room["Building Code"],
										"Room":room["Bldg/Room"][5:], "Room Type":room["Room Type"],
										"Capacity":capacity, "Adj Rm":room["Adjoining Rooms"],
										"Room Key":room["Room Key"], "Outside Key":room["Outside Key"]})


def main():

	#Only change the years in this list
	areaList = ["Unassigned", "Benton,Huntington \'08", "Berg \'08,Hunt Cottage \'93",
				"North TH \'84, \'94", "Burton \'94", "Cassat \'79, \'69, \'99", "Fac Club,Chaney \'08",
				"South TH \'74", "Davis \'54, \'59", "Parish,Douglas \'09", "Evans \'04", "Goodhue \'14",
				"Jewett,Page W,Rice,Wade \'09", "James \'99", "Musser - Student Housing", "Myers \'89",
				"Nourse \'64, \'69", "Sevy \'94", "Watson \'69"]

	createCSV(areaList)

	masterListCSV = input("Enter the exact name of the master list file (e.g. \"reslife_room_list.csv\"). Make sure it is in CSV format and is in the same folder as this program: ")
	extractRoomData(masterListCSV)
	print("All done!")

if __name__ == "__main__":
	main()
