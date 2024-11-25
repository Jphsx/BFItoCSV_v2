
import ROOT as rt
import csv
import sys





def GetListOfCat( f ):
	tlist = f.GetListOfKeys()
	catlist=[]
	for key in tlist:
	#print(key.GetName())
		if (key.GetName() == "Process"):
			continue
		if (key.GetName() == "Category"):
			continue
		catlist.append(key.GetName())

	return catlist



def ProcessCat( f, cat, writer ):
	
	tdir = f.GetDirectory(cat)
	tlist = tdir.GetListOfKeys()
	d = {'Category':'cat','Process':'proc','BinN':0,'Yield':0,'Error':0}
	for key in tlist:
		#print(key.GetName())
		h = tdir.Get(key.GetName())
		nbinsx = h.GetNbinsX()
		for i in range(1,nbinsx+1):
			#print(h.GetBinContent(i), h.GetBinError(i))
			d['Category'] = cat
			d['Process'] = key.GetName()
			d['BinN'] = i
			d['Yield'] = h.GetBinContent(i)
			d['Error'] = h.GetBinError(i)
			writer.writerow(d)
	

#filename = "../9-1-23/BFI_B20-101-debug_debug1_Ldef.root"
#csvname = "B20-101_debug1.csv"
filename = sys.argv[1]
csvname = sys.argv[2]


f = rt.TFile.Open(filename)
catlist = GetListOfCat(f)

csvfile = open(csvname, 'w', newline='')
fieldnames = ['Category', 'Process','BinN','Yield','Error']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=' ')
#testdict = {'Category': "abc", 'Process':'123', 'Bin':1, 'Yield':100, 'Error':10}
writer.writeheader()
#writer.writerow(testdict)
#csvfile.close()


for cat in catlist:
#	print(cat)
	ProcessCat(f,cat,writer)

#print("process cat 0", catlist[0])
#ProcessCat(f, catlist[0])

csvfile.close()


