import os
import unittest
from __main__ import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging
import numpy

#
# T1_Mapping_QTIM
#

class T1_Mapping_QTIM(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "T1_Mapping_QTIM" # TODO make this more human readable by adding spaces
    self.parent.categories = ["Examples"]
    self.parent.dependencies = []
    self.parent.contributors = ["Xiao Da (MGH)"] # replace with "Firstname Lastname (Organization)"
    self.parent.helpText = """
    Estimate effective T1 from multi-spectral FLASH MRI scans with different flip angles.
    """
    self.parent.acknowledgementText = """
    This file was originally developed by Xiao Da, Massachusetts General Hospital.
    """ # replace with organization, grant and thanks.
    self.parent = parent
#
# T1_Mapping_QTIMWidget
#

class T1_Mapping_QTIMWidget(ScriptedLoadableModuleWidget):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def setup(self):
    #ScriptedLoadableModuleWidget.setup(self)

    # Instantiate and connect widgets ...

    #
    # Parameters Area
    #
    parametersCollapsibleButton = ctk.ctkCollapsibleButton()
    parametersCollapsibleButton.text = "Parameters"
    self.layout.addWidget(parametersCollapsibleButton)

    # Layout within the dummy collapsible button
    parametersFormLayout = qt.QFormLayout(parametersCollapsibleButton)

    #
    # 1st input volume selector
    #
    self.inputSelector1 = slicer.qMRMLNodeComboBox()
    self.inputSelector1.nodeTypes = ( ("vtkMRMLScalarVolumeNode"), "" )
    self.inputSelector1.addAttribute( "vtkMRMLScalarVolumeNode", "LabelMap", 0 )
    self.inputSelector1.selectNodeUponCreation = True
    self.inputSelector1.addEnabled = False
    self.inputSelector1.removeEnabled = False
    self.inputSelector1.noneEnabled = False
    self.inputSelector1.showHidden = False
    self.inputSelector1.showChildNodeTypes = False
    self.inputSelector1.setMRMLScene( slicer.mrmlScene )
    self.inputSelector1.setToolTip( "Pick the input to the algorithm." )
    parametersFormLayout.addRow("Input Volume1: ", self.inputSelector1)
    #
    # Flip Angle 1
    #
    self.imageThresholdSliderWidget1 = ctk.ctkSliderWidget()
    self.imageThresholdSliderWidget1.singleStep = 0.1
    self.imageThresholdSliderWidget1.minimum = 0
    self.imageThresholdSliderWidget1.maximum = 360
    self.imageThresholdSliderWidget1.value = 0.5
    self.imageThresholdSliderWidget1.setToolTip("Set threshold value for computing the output image. Voxels that have intensities lower than this value will set to zero.")
    parametersFormLayout.addRow("Flip Angle 1", self.imageThresholdSliderWidget1)
    #
    # 2nd input volume selector
    #
    self.inputSelector2 = slicer.qMRMLNodeComboBox()
    self.inputSelector2.nodeTypes = ( ("vtkMRMLScalarVolumeNode"), "" )
    self.inputSelector2.addAttribute( "vtkMRMLScalarVolumeNode", "LabelMap", 0 )
    self.inputSelector2.selectNodeUponCreation = True
    self.inputSelector2.addEnabled = False
    self.inputSelector2.removeEnabled = False
    self.inputSelector2.noneEnabled = False
    self.inputSelector2.showHidden = False
    self.inputSelector2.showChildNodeTypes = False
    self.inputSelector2.setMRMLScene( slicer.mrmlScene )
    self.inputSelector2.setToolTip( "Pick the input to the algorithm." )
    parametersFormLayout.addRow("Input Volume2: ", self.inputSelector2)
    #
    # Flip Angle 2
    #
    self.imageThresholdSliderWidget2 = ctk.ctkSliderWidget()
    self.imageThresholdSliderWidget2.singleStep = 0.1
    self.imageThresholdSliderWidget2.minimum = 0
    self.imageThresholdSliderWidget2.maximum = 360
    self.imageThresholdSliderWidget2.value = 0.5
    self.imageThresholdSliderWidget2.setToolTip("Set threshold value for computing the output image. Voxels that have intensities lower than this value will set to zero.")
    parametersFormLayout.addRow("Flip Angle 2", self.imageThresholdSliderWidget2)
    #
    # 3rd input volume selector
    #
    self.inputSelector3 = slicer.qMRMLNodeComboBox()
    self.inputSelector3.nodeTypes = ( ("vtkMRMLScalarVolumeNode"), "" )
    self.inputSelector3.addAttribute( "vtkMRMLScalarVolumeNode", "LabelMap", 0 )
    self.inputSelector3.selectNodeUponCreation = True
    self.inputSelector3.addEnabled = False
    self.inputSelector3.removeEnabled = False
    self.inputSelector3.noneEnabled = False
    self.inputSelector3.showHidden = False
    self.inputSelector3.showChildNodeTypes = False
    self.inputSelector3.setMRMLScene( slicer.mrmlScene )
    self.inputSelector3.setToolTip( "Pick the input to the algorithm." )
    parametersFormLayout.addRow("Input Volume3: ", self.inputSelector3)
    #
    # Flip Angle 3
    #
    self.imageThresholdSliderWidget3 = ctk.ctkSliderWidget()
    self.imageThresholdSliderWidget3.singleStep = 0.1
    self.imageThresholdSliderWidget3.minimum = 0
    self.imageThresholdSliderWidget3.maximum = 360
    self.imageThresholdSliderWidget3.value = 0.5
    self.imageThresholdSliderWidget3.setToolTip("Set threshold value for computing the output image. Voxels that have intensities lower than this value will set to zero.")
    parametersFormLayout.addRow("Flip Angle 3", self.imageThresholdSliderWidget3)
    #
    # 4th input volume selector
    #
    self.inputSelector4 = slicer.qMRMLNodeComboBox()
    self.inputSelector4.nodeTypes = ( ("vtkMRMLScalarVolumeNode"), "" )
    self.inputSelector4.addAttribute( "vtkMRMLScalarVolumeNode", "LabelMap", 0 )
    self.inputSelector4.selectNodeUponCreation = True
    self.inputSelector4.addEnabled = False
    self.inputSelector4.removeEnabled = False
    self.inputSelector4.noneEnabled = False
    self.inputSelector4.showHidden = False
    self.inputSelector4.showChildNodeTypes = False
    self.inputSelector4.setMRMLScene( slicer.mrmlScene )
    self.inputSelector4.setToolTip( "Pick the input to the algorithm." )
    parametersFormLayout.addRow("Input Volume4: ", self.inputSelector4)
    #
    # Flip Angle 4
    #
    self.imageThresholdSliderWidget4 = ctk.ctkSliderWidget()
    self.imageThresholdSliderWidget4.singleStep = 0.1
    self.imageThresholdSliderWidget4.minimum = 0
    self.imageThresholdSliderWidget4.maximum = 360
    self.imageThresholdSliderWidget4.value = 0.5
    self.imageThresholdSliderWidget4.setToolTip("Set threshold value for computing the output image. Voxels that have intensities lower than this value will set to zero.")
    parametersFormLayout.addRow("Flip Angle 4", self.imageThresholdSliderWidget4)
    #
    # 5th input volume selector
    #
    self.inputSelector5 = slicer.qMRMLNodeComboBox()
    self.inputSelector5.nodeTypes = ( ("vtkMRMLScalarVolumeNode"), "" )
    self.inputSelector5.addAttribute( "vtkMRMLScalarVolumeNode", "LabelMap", 0 )
    self.inputSelector5.selectNodeUponCreation = True
    self.inputSelector5.addEnabled = False
    self.inputSelector5.removeEnabled = False
    self.inputSelector5.noneEnabled = False
    self.inputSelector5.showHidden = False
    self.inputSelector5.showChildNodeTypes = False
    self.inputSelector5.setMRMLScene( slicer.mrmlScene )
    self.inputSelector5.setToolTip( "Pick the input to the algorithm." )
    parametersFormLayout.addRow("Input Volume5: ", self.inputSelector5)
    #
    # Flip Angle 5
    #
    self.imageThresholdSliderWidget5 = ctk.ctkSliderWidget()
    self.imageThresholdSliderWidget5.singleStep = 0.1
    self.imageThresholdSliderWidget5.minimum = 0
    self.imageThresholdSliderWidget5.maximum = 360
    self.imageThresholdSliderWidget5.value = 0.5
    self.imageThresholdSliderWidget5.setToolTip("Set threshold value for computing the output image. Voxels that have intensities lower than this value will set to zero.")
    parametersFormLayout.addRow("Flip Angle 5", self.imageThresholdSliderWidget5)
    
    #
    # output volume selector
    #
    self.outputSelector = slicer.qMRMLNodeComboBox()
    self.outputSelector.nodeTypes = ( ("vtkMRMLScalarVolumeNode"), "" )
    self.outputSelector.addAttribute( "vtkMRMLScalarVolumeNode", "LabelMap", 0 )
    self.outputSelector.selectNodeUponCreation = True
    self.outputSelector.addEnabled = True
    self.outputSelector.removeEnabled = True
    self.outputSelector.noneEnabled = True
    self.outputSelector.showHidden = False
    self.outputSelector.showChildNodeTypes = False
    self.outputSelector.setMRMLScene( slicer.mrmlScene )
    self.outputSelector.setToolTip( "Pick the output to the algorithm." )
    parametersFormLayout.addRow("Output Volume: ", self.outputSelector)

    #
    # Repetion Time
    #
    self.imageThresholdSliderWidget6 = ctk.ctkSliderWidget()
    self.imageThresholdSliderWidget6.singleStep = 0.1
    self.imageThresholdSliderWidget6.minimum = 0
    self.imageThresholdSliderWidget6.maximum = 1000
    self.imageThresholdSliderWidget6.value = 0.5
    self.imageThresholdSliderWidget6.setToolTip("Set threshold value for computing the output image. Voxels that have intensities lower than this value will set to zero.")
    parametersFormLayout.addRow("Repetion Time", self.imageThresholdSliderWidget6)

    #
    # Apply Button
    #
    self.applyButton = qt.QPushButton("Apply T1 mapping")
    self.applyButton.toolTip = "Run the algorithm."
    self.applyButton.enabled = True
    parametersFormLayout.addRow(self.applyButton)

    # connections
    self.applyButton.connect('clicked(bool)', self.onApplyButton)
    

    # Add vertical spacer
    self.layout.addStretch(1)

    # Refresh Apply button state
    self.onSelect()

  def cleanup(self):
    pass

#  def onSelect(self):
#    self.applyButton.enabled = self.inputSelector.currentNode() and #self.outputSelector.currentNode()

  def onApplyButton(self):
    inputVolume1 = self.inputSelector1.currentNode()
    inputVolume2 = self.inputSelector2.currentNode()
    inputVolume3 = self.inputSelector3.currentNode()
    inputVolume4 = self.inputSelector4.currentNode()
    inputVolume5 = self.inputSelector5.currentNode()
    outputVolume = self.outputSelector.currentNode()
    FA1 = int(self.imageThresholdSliderWidget1.value)
    FA2 = int(self.imageThresholdSliderWidget2.value)
    FA3 = int(self.imageThresholdSliderWidget3.value)
    FA4 = int(self.imageThresholdSliderWidget4.value)
    FA5 = int(self.imageThresholdSliderWidget5.value)
    TR = self.imageThresholdSliderWidget6.value
    if not (inputVolume1 and inputVolume2 and inputVolume3 and inputVolume4 and inputVolume5 and outputVolume):
      qt.QMessageBox.critical(
          slicer.util.mainWindow(),
          'T1 Mapping', 'Input and output volumes are required for T1 Mapping')
      return
# run T1Mapping
    s1=slicer.util.array(inputVolume1.GetID())
    s2=slicer.util.array(inputVolume2.GetID())
    s3=slicer.util.array(inputVolume3.GetID())
    s4=slicer.util.array(inputVolume4.GetID())
    s5=slicer.util.array(inputVolume5.GetID())

# create the result output array which has the same dimension as the input images 
    d=s1.shape
    o=numpy.zeros(d,dtype=numpy.float)

# convert degrees to radians
    rdg1=numpy.radians(FA1)
    rdg2=numpy.radians(FA2)
    rdg3=numpy.radians(FA3)
    rdg4=numpy.radians(FA4)
    rdg5=numpy.radians(FA5)

# calculate the slope of the linear regression
    s1sin=s1/numpy.sin(rdg1)
    s2sin=s2/numpy.sin(rdg2)
    s3sin=s3/numpy.sin(rdg3)
    s4sin=s4/numpy.sin(rdg4)
    s5sin=s5/numpy.sin(rdg5)
    s1tan=s1/numpy.tan(rdg1)
    s2tan=s2/numpy.tan(rdg2)
    s3tan=s3/numpy.tan(rdg3)
    s4tan=s4/numpy.tan(rdg4)
    s5tan=s5/numpy.tan(rdg5)
    O=numpy.zeros(d,dtype=numpy.float)
    for k in range(0,d[0]):
      ss1sin=s1sin[k,:,:]
      ss2sin=s2sin[k,:,:]
      ss3sin=s3sin[k,:,:]
      ss4sin=s4sin[k,:,:]
      ss5sin=s5sin[k,:,:]
      ss1tan=s1tan[k,:,:]
      ss2tan=s2tan[k,:,:]
      ss3tan=s3tan[k,:,:]
      ss4tan=s4tan[k,:,:]
      ss5tan=s5tan[k,:,:]
      o=numpy.zeros((1,d[1],d[2]))
      a1=numpy.zeros((1,d[1],d[2]))
      a2=numpy.zeros((1,d[1],d[2]))
      a3=numpy.zeros((1,d[1],d[2]))
      a4=numpy.zeros((1,d[1],d[2]))
      a5=numpy.zeros((1,d[1],d[2]))
      b1=numpy.zeros((1,d[1],d[2]))
      b2=numpy.zeros((1,d[1],d[2]))
      b3=numpy.zeros((1,d[1],d[2]))
      b4=numpy.zeros((1,d[1],d[2]))
      b5=numpy.zeros((1,d[1],d[2]))
      a1[0,:,:]=ss1sin[:,:]
      a2[0,:,:]=ss2sin[:,:]
      a3[0,:,:]=ss3sin[:,:]
      a4[0,:,:]=ss4sin[:,:]
      a5[0,:,:]=ss5sin[:,:]
      b1[0,:,:]=ss1tan[:,:]
      b2[0,:,:]=ss2tan[:,:]
      b3[0,:,:]=ss3tan[:,:]
      b4[0,:,:]=ss4tan[:,:]
      b5[0,:,:]=ss5tan[:,:]
      stan=numpy.vstack((b1,b2,b3,b4,b5))
      ssin=numpy.vstack((a1,a2,a3,a4,a5))
      for i in range(0,d[1]):
        for j in range(0,d[2]):
          [coef,res]=numpy.polyfit(stan[:,i,j],ssin[:,i,j],1)
          o[0,i,j]=coef
      O[k,:,:]=o

# compute the real T1    
    T1=TR/numpy.log(O)*(-1)
    T1=numpy.uint16(T1)
    importer = vtk.vtkImageImport()
    data_string = T1.tostring() 
    importer.CopyImportVoidPointer(data_string, len(data_string)) 
    setDataType = 'importer.SetDataScalarTypeTo' + 'UnsignedShort' + '()' 
    eval(setDataType) 
    importer.SetNumberOfScalarComponents(1) 
    importer.SetWholeExtent(0,T1.shape[2]-1,0,T1.shape[1]-1,0,T1.shape[0]-1) 
    importer.SetDataExtentToWholeExtent() 
    print importer.GetDataExtent() 
    importer.Update() 
    ijkToRAS = vtk.vtkMatrix4x4() 
    inputVolume1.GetIJKToRASMatrix(ijkToRAS) 
    outputVolume.SetIJKToRASMatrix(ijkToRAS) 
    outputVolume.SetAndObserveImageData(importer.GetOutput())
    slicer.mrmlScene.AddNode(volume)
    volumeDisplayNode = slicer.vtkMRMLScalarVolumeDisplayNode() 
    slicer.mrmlScene.AddNode(volumeDisplayNode) 
    greyColorTable = slicer.util.getNode('Grey') 
    volumeDisplayNode.SetAndObserveColorNodeID(greyColorTable.GetID())
# make the output volume appear in all the slice views
    #selectionNode = slicer.app.applicationLogic().GetSelectionNode()
    #selectionNode.SetReferenceActiveVolumeID(outputVolume.GetID())
    #slicer.app.applicationLogic().PropagateVolumeSelection(0) 

