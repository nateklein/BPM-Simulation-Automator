import ScriptEnv

# Init stuff
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("BPM Sim")
oDesign = oProject.SetActiveDesign("Maxwell3DDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")

coords = (6.0, -2.0)

try:
	oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "Cylinder1"
	])
except:
	pass

# Make the beam
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, str(coords[0])+"mm",
		"YCenter:="		, str(coords[1])+"mm",
		"ZCenter:="		, "50mm",
		"Radius:="		, "2mm",
		"Height:="		, "-100mm",
		"WhichAxis:="		, "Z",
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

# Assign the beam's charge
oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignCharge(
	[
		"NAME:Beam",
		"Objects:="		, ["Cylinder1"],
		"Value:="		, "6e-10"
	])

# Run analysis
oDesign.AnalyzeAll()

# Get voltage file
oModule = oDesign.GetModule("FieldsReporter")
oModule.SaveFieldsPlots(["Plate Voltages"], "\\\\Client\\E$\\SRP\\IREAP 2019\\voltages_at_"+str(coords[0])+"_"+str(coords[1])+".dsp")

# Write data to file
