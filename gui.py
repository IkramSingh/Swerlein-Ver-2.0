# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Swerlein
###########################################################################

class Swerlein ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Swerlein (Ver 2.0)", pos = wx.DefaultPosition, size = wx.Size( 526,501 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		gSizer4 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_staticText99 = wx.StaticText( self, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText99.Wrap( -1 )
		self.m_staticText99.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText99.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		
		gSizer4.Add( self.m_staticText99, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.Port = wx.TextCtrl( self, wx.ID_ANY, u"23", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.Port, 0, wx.ALL, 5 )
		
		self.m_staticText106 = wx.StaticText( self, wx.ID_ANY, u"Excel Filename ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText106.Wrap( -1 )
		self.m_staticText106.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText106.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		
		gSizer4.Add( self.m_staticText106, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.Excel_Filename = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.Excel_Filename, 0, wx.ALL, 5 )
		
		self.m_staticText107 = wx.StaticText( self, wx.ID_ANY, u"Number Of Readings", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText107.Wrap( -1 )
		self.m_staticText107.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText107.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		
		gSizer4.Add( self.m_staticText107, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.NumReadings = wx.TextCtrl( self, wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.NumReadings, 0, wx.ALL, 5 )
		
		self.m_staticText108 = wx.StaticText( self, wx.ID_ANY, u"Number Of Harmonics", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText108.Wrap( -1 )
		self.m_staticText108.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText108.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		
		gSizer4.Add( self.m_staticText108, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.Harmonics = wx.TextCtrl( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.Harmonics, 0, wx.ALL, 5 )
		
		self.m_staticText109 = wx.StaticText( self, wx.ID_ANY, u"Number Of Bursts", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText109.Wrap( -1 )
		self.m_staticText109.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText109.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		
		gSizer4.Add( self.m_staticText109, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.Bursts = wx.TextCtrl( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.Bursts, 0, wx.ALL, 5 )
		
		self.m_staticText127 = wx.StaticText( self, wx.ID_ANY, u"Measure Time", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText127.Wrap( -1 )
		self.m_staticText127.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText127.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		
		gSizer4.Add( self.m_staticText127, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.MeasureTime = wx.TextCtrl( self, wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.MeasureTime, 0, wx.ALL, 5 )
		
		gSizer6 = wx.GridSizer( 0, 1, 0, 0 )
		
		self.ACDC = wx.CheckBox( self, wx.ID_ANY, u"ACDC RMS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ACDC.SetValue(True) 
		self.ACDC.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.ACDC.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		
		gSizer6.Add( self.ACDC, 0, wx.ALL, 5 )
		
		self.AC = wx.CheckBox( self, wx.ID_ANY, u"AC RMS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AC.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.AC.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		
		gSizer6.Add( self.AC, 0, wx.ALL, 5 )
		
		self.MEAN = wx.CheckBox( self, wx.ID_ANY, u"MEAN |V|", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.MEAN.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.MEAN.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		
		gSizer6.Add( self.MEAN, 0, wx.ALL, 5 )
		
		
		gSizer4.Add( gSizer6, 1, wx.EXPAND, 5 )
		
		self.RunButton = wx.Button( self, wx.ID_ANY, u"Run", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.RunButton, 0, wx.ALL, 5 )
		
		self.StopButton = wx.Button( self, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.StopButton, 0, wx.ALL, 5 )
		
		gSizer3 = wx.GridSizer( 0, 1, 0, 0 )
		
		self.ForceParameters = wx.CheckBox( self, wx.ID_ANY, u"Force Parameters", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ForceParameters.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.ForceParameters.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		
		gSizer3.Add( self.ForceParameters, 0, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Force Freq", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		
		gSizer3.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.ForceFreq = wx.TextCtrl( self, wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.ForceFreq, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		gSizer4.Add( gSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer4 )
		self.Layout()
		self.MenuBar = wx.MenuBar( 0 )
		self.File = wx.Menu()
		self.About = wx.MenuItem( self.File, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.File.AppendItem( self.About )
		
		self.MenuBar.Append( self.File, u"File" ) 
		
		self.Validation = wx.Menu()
		self.CodeValidate = wx.MenuItem( self.Validation, wx.ID_ANY, u"Code Validate", wx.EmptyString, wx.ITEM_NORMAL )
		self.Validation.AppendItem( self.CodeValidate )
		
		self.MenuBar.Append( self.Validation, u"Validation" ) 
		
		self.SetMenuBar( self.MenuBar )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.RunButton.Bind( wx.EVT_BUTTON, self.RunFunc )
		self.StopButton.Bind( wx.EVT_BUTTON, self.StopFunc )
		self.Bind( wx.EVT_MENU, self.AboutOnMenuSelection, id = self.About.GetId() )
		self.Bind( wx.EVT_MENU, self.QueryValidationOnMenuSelection, id = self.CodeValidate.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def RunFunc( self, event ):
		event.Skip()
	
	def StopFunc( self, event ):
		event.Skip()
	
	def AboutOnMenuSelection( self, event ):
		event.Skip()
	
	def QueryValidationOnMenuSelection( self, event ):
		event.Skip()
	

###########################################################################
## Class About
###########################################################################

class About ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About", pos = wx.DefaultPosition, size = wx.Size( 269,151 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gSizer6 = wx.GridSizer( 0, 1, 0, 0 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Program: Swerlein", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		gSizer6.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Version: 2.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		gSizer6.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Author: Ikram Singh", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		gSizer6.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"MSL @ Callaghan Innovation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		gSizer6.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		
		self.SetSizer( gSizer6 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class CodeValidation
###########################################################################

class CodeValidation ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 204,180 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gSizer4 = wx.GridSizer( 0, 1, 0, 0 )
		
		self.QueryValidate = wx.CheckBox( self, wx.ID_ANY, u"Query Validate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.QueryValidate.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		gSizer4.Add( self.QueryValidate, 0, wx.ALL, 5 )
		
		self.Validate = wx.Button( self, wx.ID_ANY, u"Validate", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.Validate, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		
		self.SetSizer( gSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.CodeValidationOnClose )
		self.Validate.Bind( wx.EVT_BUTTON, self.ValidateOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def CodeValidationOnClose( self, event ):
		event.Skip()
	
	def ValidateOnButtonClick( self, event ):
		event.Skip()
	

