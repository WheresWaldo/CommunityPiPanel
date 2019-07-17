#!/usr/bin/python

# kivy imports
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import RoundedRectangle
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import Window
from kivy.utils import get_color_from_hex as rgb
from kivy.garden.graph import Graph, MeshLinePlot, SmoothLinePlot

# other imports
from pconsole import pconsole
from .. import roboprinter
from multiprocessing import Process
import time
import os
from math import sin, cos
import requests
import json
import ConfigParser
import sys
from subprocess import *
import pprint

DEFAULT_FONT = 'Roboto'

class MainScreen(Screen):
    """
    Represents the the main screen template with 3 tab buttons on the top bar: Files, Printer, and Settings

    Is in charge of orchestrating content update for all 3 tabs
    """
    lang = roboprinter.lang

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)        


    def query_eeprom(self):
        if not roboprinter.printer_instance._printer.is_printing():

            pconsole.query_eeprom()  

    def update_file_sizes(self):
        self.ids.files_content.update_file_sizes()      

    
    def open_tab(self, tab_id):
        t = self.ids[tab_id]
        #Logger.info('Tab: {}'.format(t))
        self.ids.mstp.switch_to(t)


    def update_tab(self,tab):
        roboprinter.open_tab = tab

class MainScreenTabbedPanel(TabbedPanel):
    """
    Represents the tabbed panels. Handles toggling between FilesTab, PrinterStatusTab and SettingsTab
    """

    def __init__(self, **kwargs):
        super(MainScreenTabbedPanel, self).__init__(**kwargs)
