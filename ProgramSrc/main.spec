# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[("commData.xlsx","."), ("shelData.xlsx","."),("map.html","."),("ICONS","ICONS"),("tutorial","tutorial"),("allocation_results.xlsx","."),("modelCommData.xlsx","."),("modelShelData.xlsx","."),("modelPerformanceResult.txt","."),("distance_matrix.xlsx","."),("modelParam.xlsx","."),("ReportTemplate.xlsx",".") ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Shelter Allocation',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='ICONS/logo.png',
)