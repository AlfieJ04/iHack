#!/usr/bin/env python3

import wx

class UpdatePanel(wx.Panel):    
    def __init__(self, parent):
        super().__init__(parent)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.row_obj_dict = {}

        self.list_ctrl = wx.ListCtrl(
            self, size=(-1, 100), 
            style=wx.LC_REPORT | wx.BORDER_SUNKEN
        )
        self.list_ctrl.InsertColumn(0, 'Application', width=140)
        self.list_ctrl.InsertColumn(1, 'Location', width=240)
        self.list_ctrl.InsertColumn(2, 'Version', width=100)
        main_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)        
        update_button = wx.Button(self, label='Update')
        update_button.Bind(wx.EVT_BUTTON, self.on_update)
        main_sizer.Add(update_button, 0, wx.ALL | wx.CENTER, 5)        
        self.SetSizer(main_sizer)

    def on_update(self, event):
        print('in on_update')

    def update_apps(self, folder_path):
        print(folder_path)


class HAFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None,
                         title='Hack-Attack')
        self.panel = UpdatePanel(self)
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = HAFrame()
    app.MainLoop()