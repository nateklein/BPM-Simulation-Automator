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

coords = [(0.0, 0.0), (2.0, 0.0), (1.732, 1.0), (1.0, 1.732), (0.0, 2.0), (-1.0, 1.732), (-1.732, 1.0), (-2.0, 0.0), (-1.732, -1.0), (-1.0, -1.732), (-0.0, -2.0), (1.0, -1.732), (1.732, -1.0), (4.0, 0.0), (3.464, 2.0), (2.0, 3.464), (0.0, 4.0), (-2.0, 3.464), (-3.464, 2.0), (-4.0, 0.0), (-3.464, -2.0), (-2.0, -3.464), (-0.0, -4.0), (2.0, -3.464), (3.464, -2.0), (6.0, 0.0), (5.196, 3.0), (3.0, 5.196), (0.0, 6.0), (-3.0, 5.196), (-5.196, 3.0), (-6.0, 0.0), (-5.196, -3.0), (-3.0, -5.196), (-0.0, -6.0), (3.0, -5.196), (5.196, -3.0), (8.0, 0.0), (6.928, 4.0), (4.0, 6.928), (0.0, 8.0), (-4.0, 6.928), (-6.928, 4.0), (-8.0, 0.0), (-6.928, -4.0), (-4.0, -6.928), (-0.0, -8.0), (4.0, -6.928), (6.928, -4.0), (10.0, 0.0), (9.659, 2.588), (8.66, 5.0), (7.071, 7.071), (5.0, 8.66), (2.588, 9.659), (0.0, 10.0), (-2.588, 9.659), (-5.0, 8.66), (-7.071, 7.071), (-8.66, 5.0), (-9.659, 2.588), (-10.0, -0.0), (-9.659, -2.588), (-8.66, -5.0), (-7.071, -7.071), (-5.0, -8.66), (-2.588, -9.659), (-0.0, -10.0), (2.588, -9.659), (5.0, -8.66), (7.071, -7.071), (8.66, -5.0), (9.659, -2.588), (12.0, 0.0), (11.591, 3.106), (10.392, 6.0), (8.485, 8.485), (6.0, 10.392), (3.106, 11.591), (0.0, 12.0), (-3.106, 11.591), (-6.0, 10.392), (-8.485, 8.485), (-10.392, 6.0), (-11.591, 3.106), (-12.0, -0.0), (-11.591, -3.106), (-10.392, -6.0), (-8.485, -8.485), (-6.0, -10.392), (-3.106, -11.591), (-0.0, -12.0), (3.106, -11.591), (6.0, -10.392), (8.485, -8.485), (10.392, -6.0), (11.591, -3.106), (14.0, 0.0), (13.523, 3.623), (12.124, 7.0), (9.899, 9.899), (7.0, 12.124), (3.623, 13.523), (0.0, 14.0), (-3.623, 13.523), (-7.0, 12.124), (-9.899, 9.899), (-12.124, 7.0), (-13.523, 3.623), (-14.0, -0.0), (-13.523, -3.623), (-12.124, -7.0), (-9.899, -9.899), (-7.0, -12.124), (-3.623, -13.523), (-0.0, -14.0), (3.623, -13.523), (7.0, -12.124), (9.899, -9.899), (12.124, -7.0), (13.523, -3.623), (16.0, 0.0), (15.455, 4.141), (13.856, 8.0), (11.314, 11.314), (8.0, 13.856), (4.141, 15.455), (0.0, 16.0), (-4.141, 15.455), (-8.0, 13.856), (-11.314, 11.314), (-13.856, 8.0), (-15.455, 4.141), (-16.0, -0.0), (-15.455, -4.141), (-13.856, -8.0), (-11.314, -11.314), (-8.0, -13.856), (-4.141, -15.455), (-0.0, -16.0), (4.141, -15.455), (8.0, -13.856), (11.314, -11.314), (13.856, -8.0), (15.455, -4.141), (18.0, 0.0), (17.387, 4.659), (15.588, 9.0), (12.728, 12.728), (9.0, 15.588), (4.659, 17.387), (0.0, 18.0), (-4.659, 17.387), (-9.0, 15.588), (-12.728, 12.728), (-15.588, 9.0), (-17.387, 4.659), (-18.0, -0.0), (-17.387, -4.659), (-15.588, -9.0), (-12.728, -12.728), (-9.0, -15.588), (-4.659, -17.387), (-0.0, -18.0), (4.659, -17.387), (9.0, -15.588), (12.728, -12.728), (15.588, -9.0), (17.387, -4.659), (20.0, 0.0), (19.319, 5.176), (17.321, 10.0), (14.142, 14.142), (10.0, 17.321), (5.176, 19.319), (0.0, 20.0), (-5.176, 19.319), (-10.0, 17.321), (-14.142, 14.142), (-17.321, 10.0), (-19.319, 5.176), (-20.0, -0.0), (-19.319, -5.176), (-17.321, -10.0), (-14.142, -14.142), (-10.0, -17.321), (-5.176, -19.319), (-0.0, -20.0), (5.176, -19.319), (10.0, -17.321), (14.142, -14.142), (17.321, -10.0), (19.319, -5.176)]

j = 4306

# Delete an existing beam if it is there
try:
	oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "Circle1"
	])
except:
	pass

for i in coords:
	# Make beam
	oEditor.CreateCircle(
		[
			"NAME:CircleParameters",
			"IsCovered:="		, True,
			"XCenter:="		, str(i[0])+"mm",
			"YCenter:="		, str(i[1])+"mm",
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
			"Edges:="		, [j],
			"IsOfTypeVoltage:="	, True
		])
	j += 6
	oModule = oDesign.GetModule("FieldsReporter")

	# Run analysis
	oDesign.AnalyzeAll()

	# Get voltage data
	oModule.SaveFieldsPlots(["Plate Voltages"], "\\\\Client\\E$\\SRP\\IREAP 2019\\Simulation Data\\voltages_at_"+str(i[0])+"_"+str(i[1])+".dsp")

	# Delete the beam
	oEditor.Delete(
		[
			"NAME:Selections",
			"Selections:="		, "Circle1"
		])