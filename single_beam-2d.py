# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2018.2.0
# 16:12:35  Jul 16, 2019
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("BPM Sim")
oDesign = oProject.SetActiveDesign("Plates Only")
oEditor = oDesign.SetActiveEditor("3D Modeler")

coords = (0.0, 0.0)

# Delete an existing beam if it is there
try:
	oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "Circle1"
	])
except:
	pass

# Make beam
oEditor.CreateCircle(
	[
		"NAME:CircleParameters",
		"IsCovered:="		, True,
		"XCenter:="		, str(coords[0])+"mm",
		"YCenter:="		, str(coords[1])+"mm",
		"ZCenter:="		, "0mm",
		"Radius:="		, "3.7mm",
		"WhichAxis:="		, "Z",
		"NumSegments:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Circle1",
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

# Assign charge density
oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignVolumeChargeDensity(
	[
		"NAME:Beam",
		"Objects:="		, ["Circle1"],
		"Value:="		, "4.392e-09",
		"CoordinateSystem:="	, ""
	])

# Assign boundary
oModule.AssignBalloon(
	[
		"NAME:Balloon1",
		"Edges:="		, [628],
		"IsOfTypeVoltage:="	, True
	])
oModule = oDesign.GetModule("FieldsReporter")

# Run analysis
oDesign.AnalyzeAll()

# Get voltage data
oModule.SaveFieldsPlots(["Plate Voltages"], "\\\\Client\\E$\\SRP\\IREAP 2019\\Simulation Data\\voltages_at_"+str(coords[0])+"_"+str(coords[1])+".dsp")
