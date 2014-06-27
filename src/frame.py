import wx
import query


# EDIT INFO HERE
PREFS = {
  "host": "127.0.0.1",
  "port": 8000,
  "secret": "abc"
}


class Frame(wx.Frame):
  """ Frame for the application main window """

  # initializer
  def __init__(self, *args, **kwargs):
    super(Frame, self).__init__(size=(250, 200), *args, **kwargs) 
        
    self.InitUI()

  def InitUI(self):

    # manual query
    self.quote = wx.StaticText(self, label="Manual query:", pos=(20, 30))
    self.query = wx.TextCtrl(self, pos=(20, 60), size=(200, 24))
    self.confirm = wx.Button(self, label="Go", pos=(16, 90), size=(120, 24))
    

    # events
    self.confirm.Bind(wx.EVT_BUTTON, self.DoQuery)
    self.query.Bind(wx.EVT_KEY_DOWN, self.KeyDown)


  # do a manual query
  def DoQuery(self, event):
    text = self.query.GetValue()

    # do the query
    q = query.Query(text=text, **PREFS)
    out = q.getResponse()

    # get the first packet
    if len(out):
      response = "Status: %s\nResponse: '%s' \nPlugin's Name: '%s'" % (out[0]["status"], out[0]["text"], out[0]["type"])

      box = wx.MessageDialog(None, str(response), 'Response', wx.OK | wx.ICON_QUESTION)
      box.ShowModal()

      self.query.SetValue("")

  def KeyDown(self, event):
    if event.GetKeyCode() == 13:
      # do query
      self.DoQuery(None)
    elif event.GetKeyCode() == 27:
      # close window
      self.Close()
    else:
      event.Skip()
