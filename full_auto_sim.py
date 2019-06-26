# Script to run BPM simulations with the beam at multiple points within the BPM
# Written by Nate Klein

import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("BPM Sim")
oDesign = oProject.SetActiveDesign("Maxwell3DDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")

coords = [(0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (1.0, 0.0)]

data = open("sim_data.csv", 'w')

for i in coords:
	# Make the beam
	oEditor.CreateCylinder(
		[
			"NAME:CylinderParameters",
			"XCenter:="		, "50mm",
			"YCenter:="		, str(i[0])+"mm",
			"ZCenter:="		, str(i[1])+"mm",
			"Radius:="		, "2mm",
			"Height:="		, "-100mm",
			"WhichAxis:="		, "X",
			"NumSides:="		, "0"
		], 
		[
			"NAME:Attributes",
			"Name:="		, "Cylinder1",
			"Flags:="		, "",
			"Color:="		, "(143 175 143)",
			"Transparency:="	, 0,
			"PartCoordinateSystem:=", "Global",
			"UDMId:="		, "",
			"MaterialValue:="	, "\"vacuum\"",
			"SurfaceMaterialValue:=", "\"\"",
			"SolveInside:="		, True,
			"IsMaterialEditable:="	, True,
			"UseMaterialAppearance:=", False,
			"IsLightweight:="	, False
		])
	oModule = oDesign.GetModule("BoundarySetup")

	# Assign the beam's charge
	oModule.AssignCharge(
		[
			"NAME:Beam",
			"Objects:="		, ["Cylinder1"],
			"Value:="		, "6e-10"
		])

	# Run analysis
	oDesign.AnalyzeAll()
	oModule = oDesign.GetModule("FieldsReporter")
	oModule.ExportMarkerTable("//Client/E$/SRP/IREAP 2019/voltages.csv")

	# Write data to file
	f = open("//Client/E$/SRP/IREAP 2019/voltages.csv", 'r')
	f.readline()
	voltages = []
	while f.readline() != "":
		voltages += f.readline().split(",")[4]
	f.close()

	data.write(str(i[0])+","+str(i[1])+","+",".join(voltages))

	# Delete the beam
	oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "Cylinder1"
	])

data.close()
