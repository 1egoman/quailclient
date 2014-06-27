#!/usr/bin/env python
import wx
from frame import Frame

class App(object):

  def __init__(self):
    self.app = wx.App()

    self.frame = Frame(None, -1, "Basic Quail Client - by Ryan Gaus")
    self.frame.Show()

    self.app.MainLoop()


if __name__ == '__main__':
  App()