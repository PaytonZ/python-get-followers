# -*- mode: python -*-
a = Analysis(['MainGUi.py', 'getFollowers.py', 'accountManager.py', 'main.py', 'GuiGenerated.py', 'images_rc.py'],
             pathex=['C:\\Users\\Daniel\\Documents\\GitHub\\python-get-followers'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='MainGUi.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='MainGUi')
