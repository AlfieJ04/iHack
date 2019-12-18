import wx

class haFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Hack-Attack')
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = haFrame()
    app.MainLoop()