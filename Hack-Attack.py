#!/usr/bin/env python3

import wx

class haFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Hack-Attack')
        panel = wx.Panel(self)
        srch_sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(panel, pos=(5, 5))
        srch_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        srch_btn = wx.Button(panel, label='Search', pos=(5, 55))
        srch_sizer.Add(srch_btn, 0, wx.ALL | wx.CENTER, 5)        
        panel.SetSizer(srch_sizer)
        
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = haFrame()
    app.MainLoop()