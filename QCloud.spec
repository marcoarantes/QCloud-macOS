block_cipher = None
app_name = 'QCloud'
mac_icon = 'assets/QCloud.icns'
added_files = [
    ('assets/*.png', 'assets'),
    ('assets/*.ico', 'assets'),
    ('config.ini', '.')
]

a = Analysis(['./main.py'],
             pathex=[],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['_tkinter', 'Tkinter', 'enchant', 'twisted'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name=app_name,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False)

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name=app_name)

app = BUNDLE(coll,
             name=app_name + '.app',
             icon=mac_icon,
             bundle_identifier=None,
             version='3.3')