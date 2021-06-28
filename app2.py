#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 14:05:05 2019

@author: eslam
"""

import sys
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QMainWindow, QApplication
from myGui2 import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import vtk
from pydicom import dcmread
from pydicom.data import get_testdata_file
from vtk import vtkDICOMImageReader
from vtk import vtkImageShiftScale
from vtk import vtkPNGWriter
import vtk
from vtk.util import numpy_support
import numpy
surfaceExtractor = vtk.vtkContourFilter()
    
class AppWindow(QMainWindow):
    def slider_SLOT(self,val):
        surfaceExtractor.SetValue(0, val)
        iren.update()
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.horizontalSlider.valueChanged.connect(self.slider_SLOT)
        self.ui.horizontalSlider_2.sliderReleased.connect(self.ray_cast_rendring)
        self.ui.Red.sliderReleased.connect(self.ray_cast_rendring)
        self.ui.green.sliderReleased.connect(self.ray_cast_rendring)
        self.ui.blue.sliderReleased.connect(self.ray_cast_rendring)
        self.ui.surfaceRendring.clicked.connect(self.surface_rendring)
        self.ui.raycasting.clicked.connect(self.ray_cast_rendring)
        self.ui.open_DICOM.triggered.connect(self.get_data)
        self.show()  
    

        
    def remap(self, x, oMin, oMax, nMin, nMax ):

    #range check

        #check reversed input range
        reverseInput = False
        oldMin = min( oMin, oMax )
        oldMax = max( oMin, oMax )
        if not oldMin == oMin:
            reverseInput = True

        #check reversed output range
        reverseOutput = False   
        newMin = min( nMin, nMax )
        newMax = max( nMin, nMax )
        if not newMin == nMin :
            reverseOutput = True

        portion = (x-oldMin)*(newMax-newMin)/(oldMax-oldMin)
        if reverseInput:
            portion = (oldMax-x)*(newMax-newMin)/(oldMax-oldMin)

        result = portion + newMin
        if reverseOutput:
            result = newMax - portion

        return result
    def vtk_rendering(self):
        global renWin
        renWin = iren.GetRenderWindow()
        self.aRenderer = vtk.vtkRenderer()
        renWin.AddRenderer(self.aRenderer)

        
    def get_data(self):
        global reader
        # PathDicom = QtGui.QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QtGui.QFileDialog.ShowDirsOnly)
        # PathDicom = "C:/Users/Hp/Downloads/3rd_year_biomedical_Semester2/Computer Graphics/task3/cg-task3-team-17-1/Part2/data/Ankle"
        # PathDicom = QFileDialog.getOpenFileName(None, 'Open dicom ', '/home', "dicom (*.dcm)")[0]
        PathDicom = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select project folder:', 'F:\\', QtWidgets.QFileDialog.ShowDirsOnly)
        reader = vtk.vtkDICOMImageReader()
        reader.SetDirectoryName(PathDicom)
        reader.Update()
        # # Read Dataset using vtkVolume16Reader 
        # v16 = vtk.vtkVolume16Reader()
        # v16.SetDataDimensions(64, 64)
        # v16.SetDataByteOrderToLittleEndian()
        # v16.SetFilePrefix(dataDir)
        # v16.SetImageRange(1, 93)
        # v16.SetDataSpacing(3.2, 3.2, 1.5)        
        # An isosurface, or contour value of 500 is known to correspond to the
    def surface_rendring(self):
        surfaceExtractor.SetInputConnection(reader.GetOutputPort())
        surfaceExtractor.SetValue(0, 500)
        surfaceNormals = vtk.vtkPolyDataNormals()
        surfaceNormals.SetInputConnection(surfaceExtractor.GetOutputPort())
        surfaceNormals.SetFeatureAngle(60.0)
        surfaceMapper = vtk.vtkPolyDataMapper()
        surfaceMapper.SetInputConnection(surfaceNormals.GetOutputPort())
        surfaceMapper.ScalarVisibilityOff()
        surface = vtk.vtkActor()
        surface.SetMapper(surfaceMapper)
        
        aCamera = vtk.vtkCamera()
        aCamera.SetViewUp(0, 0, -1)
        aCamera.SetPosition(0, 1, 0)
        aCamera.SetFocalPoint(0, 0, 0)
        aCamera.ComputeViewPlaneNormal()
        
        self.aRenderer.AddActor(surface)
        self.aRenderer.SetActiveCamera(aCamera)
        self.aRenderer.ResetCamera()
        
        self.aRenderer.SetBackground(0, 0, 0)
        
        self.aRenderer.ResetCameraClippingRange()
        
        # Interact with the data.
        iren.Initialize()
        renWin.Render()
        iren.Start()
        iren.show()
    def ray_cast_rendring(self):
        ren = vtk.vtkRenderer()
        renWin = vtk.vtkRenderWindow()
        renWin.AddRenderer(ren)
        iren = vtk.vtkRenderWindowInteractor()
        iren.SetRenderWindow(renWin)
        # The volume will be displayed by ray-cast alpha compositing.
        # A ray-cast mapper is needed to do the ray-casting, and a
        # compositing function is needed to do the compositing along the ray.
    
        volumeMapper = vtk.vtkGPUVolumeRayCastMapper()
        volumeMapper.SetInputConnection(reader.GetOutputPort())
        volumeMapper.SetBlendModeToComposite()

        # The color transfer function maps voxel intensities to colors.
        # It is modality-specific, and often anatomy-specific as well.
        # The goal is to one color for flesh (between 500 and 1000)
        # and another color for bone (1150 and over)
        red = self.remap( float(self.ui.Red.value()), 0, 100, 0, 1 )
        green = self.remap( float(self.ui.green.value()), 0, 100, 0, 1 )
        blue = self.remap( float(self.ui.blue.value()), 0, 100, 0, 1 )
        volumeColor = vtk.vtkColorTransferFunction()
        volumeColor.AddRGBPoint(0,    0.0, 0.0, 0.0)
        volumeColor.AddRGBPoint(500,  red, green , blue)
        volumeColor.AddRGBPoint(1000, 1.0, 0.5, 0.3)
        volumeColor.AddRGBPoint(1150, 1.0, 1.0, 0.9)

        # The opacity transfer function is used to control the opacity
        # of different tissue types.
        opacity = self.remap( float(self.ui.horizontalSlider_2.value()), 0, 100, 0, 1 )
        volumeScalarOpacity = vtk.vtkPiecewiseFunction()
        volumeScalarOpacity.AddPoint(0,    0.00)
        volumeScalarOpacity.AddPoint(500,  opacity)
        volumeScalarOpacity.AddPoint(1000, 0.15)
        volumeScalarOpacity.AddPoint(1150, 0.85)
        
        print(opacity)
        # The gradient opacity function is used to decrease the opacity
        # in the "flat" regions of the volume while maintaining the opacity
        # at the boundaries between tissue types.  The gradient is measured
        # as the amount by which the intensity changes over unit distance.
        # For most medical data, the unit distance is 1mm.
        volumeGradientOpacity = vtk.vtkPiecewiseFunction()
        volumeGradientOpacity.AddPoint(0,   0.0)
        volumeGradientOpacity.AddPoint(90,  0.5)
        volumeGradientOpacity.AddPoint(100, 1.0)

        # The VolumeProperty attaches the color and opacity functions to the
        # volume, and sets other volume properties.  The interpolation should
        # be set to linear to do a high-quality rendering.  The ShadeOn option
        # turns on directional lighting, which will usually enhance the
        # appearance of the volume and make it look more "3D".  However,
        # the quality of the shading depends on how accurately the gradient
        # of the volume can be calculated, and for noisy data the gradient
        # estimation will be very poor.  The impact of the shading can be
        # decreased by increasing the Ambient coefficient while decreasing
        # the Diffuse and Specular coefficient.  To increase the impact
        # of shading, decrease the Ambient and increase the Diffuse and Specular.
        volumeProperty = vtk.vtkVolumeProperty()
        volumeProperty.SetColor(volumeColor)
        volumeProperty.SetScalarOpacity(volumeScalarOpacity)
        volumeProperty.SetGradientOpacity(volumeGradientOpacity)
        volumeProperty.SetInterpolationTypeToLinear()
        volumeProperty.ShadeOn()
        volumeProperty.SetAmbient(0.4)
        volumeProperty.SetDiffuse(0.6)
        volumeProperty.SetSpecular(0.2)

        # The vtkVolume is a vtkProp3D (like a vtkActor) and controls the position
        # and orientation of the volume in world coordinates.
        volume = vtk.vtkVolume()
        volume.SetMapper(volumeMapper)
        volume.SetProperty(volumeProperty)

        # Finally, add the volume to the renderer
        ren.AddViewProp(volume)

        # Set up an initial view of the volume.  The focal point will be the
        # center of the volume, and the camera position will be 400mm to the
        # patient's left (which is our right).
        camera =  ren.GetActiveCamera()
        c = volume.GetCenter()
        camera.SetFocalPoint(c[0], c[1], c[2])
        camera.SetPosition(c[0] + 400, c[1], c[2])
        camera.SetViewUp(0, 0, -1)

        # Increase the size of the render window
        renWin.SetSize(640, 480)

        # Interact with the data.
        iren.Initialize()
        renWin.Render()
        iren.Start()
    


app = QApplication(sys.argv)
# The class that connect Qt with VTK
iren = QVTKRenderWindowInteractor()
w = AppWindow()
w.vtk_rendering()
w.show()
sys.exit(app.exec_())
    # Start the event loop.
