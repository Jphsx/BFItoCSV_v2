import csv
import sys

csvin = sys.argv[1]
csvout = sys.argv[2]

def BJets1L():
	binmap = {"Ch1L_mum_gold_0j0svS_ge1j0bISR_PTISR1":2
                     , "Ch1L_mum_gold_0j0svS_ge1j0bISR_PTISR1":3}
	return binmap

def BJets2L():
	binmap = {"Ch2L_OSelmu_gold_0j0svS_ge1j0bISR_PTISR1_gamT1":8
                     , "Ch2L_OSmumu_gold_0j0svS_ge1j0bISR_PTISR1_gamT1":8
                     , "Ch2L_OSelel_gold_0j0svS_ge1j0bISR_PTISR1_gamT1":8
                     , "Ch2L_Zstar_gold_1j1bS_ge1j0bISR_PTISR1_gamT1":8
                     , "Ch2L_noZ_gold_1j0bS_ge1j0bISR_PTISR1_gamT1":8
                     , "Ch2L_Zstar_gold_ge2j0bS_ge1j0bISR_PTISR1_gamT1":6}
	return binmap


def BJetsSV():
	binmap = {"Ch0L_0_0jge2svS_ge1jISR_PTISR0_gamT0_SVeta0":2
                     , "Ch0L_0_0jge2svS_ge1jISR_PTISR0_gamT0_SVeta0":3
                     , "Ch1L_lm_gold_0jge1svS_ge1jISR_PTISR0_gamT0_SVeta0":2
                     , "Ch1L_lm_gold_0jge1svS_ge1jISR_PTISR0_gamT0_SVeta0":3
                     , "Ch1L_lpm_gold_1jge1svS_ge1jISR_PTISR0_gamT0_SVeta0":4
                     , "Ch2L_ll_gold_0jge1svS_ge1jISR_PTISR0_gamT0_SVeta0":8}
	return binmap

def BJetsModerate():
	binmap = {"Ch0L_0_4j1bS_ge1j0bISR_PTISR1_gamT0":4
                     , "Ch0L_0_4j1bS_ge1j0bISR_PTISR1_gamT1":4
                     , "Ch0L_0_4jge2bS_ge1jISR_PTISR1_gamT0":4
                     , "Ch0L_0_4jge2bS_ge1jISR_PTISR1_gamT1":4
                     , "Ch0L_0_ge5j1bS_ge1j0bISR_PTISR1_gamT0":4
                     , "Ch0L_0_ge5jge2bS_ge1jISR_PTISR1_gamT0":4
                     , "Ch1L_lpm_gold_2j1bS_ge1j0bISR_PTISR1_gamT1":4
                     , "Ch1L_lpm_gold_2j2bS_ge1jISR_PTISR1_gamT1":4
                     , "Ch1L_lpm_gold_3j1bS_ge1j0bISR_PTISR1_gamT1":4
                     , "Ch1L_lpm_gold_3jge2bS_ge1jISR_PTISR1_gamT1":4
                     , "Ch1L_lpm_gold_ge4j1bS_ge1j0bISR_PTISR1_gamT1":4
                     , "Ch1L_lpm_gold_ge4jge2bS_ge1jISR_PTISR1_gamT1":4
                     , "Ch2L_Zstar_gold_1j0bS_ge1j0bISR_PTISR1_gamT1":8
                     , "Ch2L_Zstar_gold_1j0bS_ge1j0bISR_PTISR1_gamT1":9
                     , "Ch2L_Zstar_gold_1j1bS_ge1j0bISR_PTISR1_gamT1":8
                     , "Ch2L_Zstar_gold_1j1bS_ge1j0bISR_PTISR1_gamT1":9
                     , "Ch2L_Zstar_gold_ge2j0bS_ge1j0bISR_PTISR1_gamT1":6
                     , "Ch2L_Zstar_gold_ge2jge1bS_ge1j0bISR_PTISR1_gamT1":6
                     , "Ch2L_noZ_gold_1j0bS_ge1j0bISR_PTISR1_gamT1":8
                     , "Ch2L_noZ_gold_1j0bS_ge1j0bISR_PTISR1_gamT1":9
                     , "Ch2L_noZ_gold_1j1bS_ge1j0bISR_PTISR1_gamT1":8
                     , "Ch2L_noZ_gold_1j1bS_ge1j0bISR_PTISR1_gamT1":9
                     , "Ch2L_noZ_gold_ge2j0bS_ge1j0bISR_PTISR1_gamT1":6
                     , "Ch2L_noZ_gold_ge2jge1bS_ge1j0bISR_PTISR1_gamT1":6}
	return binmap



def Electroweak():
	binmap = {"Ch2L_OSmumu_gold_0j0svS_ge1j0bISR_PTISR1_gamT1":8
                     , "Ch2L_OSelel_gold_0j0svS_ge1j0bISR_PTISR1_gamT1":8
                     , "Ch2L_Zstar_gold_1j0bS_ge1j0bISR_PTISR1_gamT0":8
                     , "Ch2L_Zstar_gold_1j0bS_ge1j0bISR_PTISR1_gamT0":9
                     , "Ch2L_Zstar_gold_ge2j0bS_ge1j0bISR_PTISR1_gamT0":6
                     , "Ch2L_Zstar_gold_1j0bS_ge1j0bISR_PTISR1_gamT1":8
                     , "Ch2L_Zstar_gold_1j0bS_ge1j0bISR_PTISR1_gamT1":9
                     , "Ch2L_Zstar_gold_ge2j0bS_ge1j0bISR_PTISR1_gamT1":6}
	return binmap

def OSSF():
	binmap = {"Ch2L_OSmumu_gold_0j0svS_ge1j0bISR_PTISR1_gamT0":8
                     , "Ch2L_OSmumu_gold_0j0svS_ge1j0bISR_PTISR1_gamT1":8
                     , "Ch2L_OSelel_gold_0j0svS_ge1j0bISR_PTISR1_gamT0":8
                     , "Ch2L_OSelel_gold_0j0svS_ge1j0bISR_PTISR1_gamT1":8}
	return binmap

def ThreeL():
	binmap = {"Ch3L_Zstar_gold_0jS_ge1jISR_PTISR0":3
                     , "Ch3L_Zstar_gold_ge1jS_ge1jISR_PTISR0":2
                     , "Ch3L_noZ_gold_0jS_ge1jISR_PTISR0":3
                     , "Ch3L_noZ_gold_ge1jS_ge1jISR_PTISR0":2
                     , "Ch3L_SS_gold_inclS_ge1jISR_PTISR0":3}
	return binmap

def sliceSuperBins( binmap, csvdata, mapname ):
	csvslice=[]
	header = csvdata[0]
	csvslice.append(header)
	for key in binmap:
		#print(key, binmap[key])
		for row in csvdata:
			#print("Analyzing row: ",row)
			if( (key == row[0]) and ((binmap[key]+1)==int(row[2])) ):
				csvslice.append(row)
		#break
	#for row in csvslice:
	#	print(row)
	global csvout
	out = csvout+"_"+mapname+".csv"
	with open( out, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerows(csvslice)
		csvfile.close()
	

csvdata = list(csv.reader(open( csvin , "r"), delimiter = ' '))
#print(csv)
sliceSuperBins( BJets1L(), csvdata, "BJets1L")
sliceSuperBins( BJets2L(), csvdata, "BJets2L")
sliceSuperBins( BJetsSV(), csvdata, "BJetsSV")
sliceSuperBins( BJetsModerate(), csvdata, "BJetsModerate")
sliceSuperBins( Electroweak(), csvdata, "Electroweak")
sliceSuperBins( OSSF(), csvdata, "OSSF")
sliceSuperBins( ThreeL(), csvdata, "ThreeL")
	
			
#print( ThreeL(1) )

