# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:\\Users\\diVine\\PycharmProjects\\ThunderTac\\main.py'],
             pathex=['C:\\Users\\diVine\\PycharmProjects\\ThunderTac'],
             binaries=[],
             datas=[('venv\\lib\\site-packages\\imagehash\\VERSION', 'imagehash\\')],
             hiddenimports=[],
             hookspath=['c:\\users\\divine\\pycharmprojects\\thundertac\\venv\\lib\\site-packages\\pyupdater\\hooks'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='win',
          icon='resources\\thundertac.ico',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
