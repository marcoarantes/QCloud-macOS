# -*- mode: python ; coding: utf-8 -*-
added_files = [
    ( 'assets/*.png', '.' ),
    ( 'assets/*.ico', '.' ),
    ( 'assets', 'assets' ),
]

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='QCloud',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets/QCloud.icns'],
)
app = BUNDLE(
    exe,
    name='QCloud.app',
    icon='assets/QCloud.icns',
    bundle_identifier=None,
)
