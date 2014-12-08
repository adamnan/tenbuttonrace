#! /usr/bin/env python

import wx
import time
import random

class TenButtonFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Ten Button Race", size=(800, 600))
		
		#Make a new Panel
		self.panel = wx.Panel(self)
		#Make the start button
		self.btnstart = wx.Button(self.panel, label="Click to start", pos=(350, 15))
		#Make the other ten buttons
		self.Button = []
		i = 0
		while i < 10:
			self.btn = wx.Button(self.panel, label="Catch Me!!", pos=(random.randint(0,700),random.randint(0,600)))
			self.btn.Bind(wx.EVT_BUTTON, self.Onbtn)
			self.btn.Show(False)
			self.Button.append(self.btn)
			i += 1
		
		#Bind all the buttons to their event handlers
		self.btnstart.Bind(wx.EVT_BUTTON, self.OnStart)
	# Event handler for the start button
	def OnStart(self, e):
		#Make the start button disappear
		self.btnstart.Show(False)
		self.startTime = time.time()
		#Make Button One appear
		self.Button[1].Show(True)
	#Other event handlers here
	def Onbtn(self, e):
		clickedButton = e.GetEventObject()
		clickedIndex = self.Button.index(clickedButton)
		self.Button[clickedIndex].Show(False)
		try:
			self.Button[clickedIndex + 1].Show(True)
		except IndexError:
			self.endTime = time.time()
			self.heading = wx.StaticText(self.panel, label="Your time is {}s".format(self.endTime-self.startTime), pos=(200, 30))
	#Remember the last event handler needs to print the final time.
	
	
# -------- Main Program Below ------------

app = wx.App(False)
frame = TenButtonFrame(None)
frame.Show()
app.MainLoop()