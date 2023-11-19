# MyTest appliaction

## Project is based on Studies in DSW University 
### I would like to present schema of Maciej 43125 app
```
├── build
│   └── main
│       ├── Analysis-00.toc
│       ├── base_library.zip
│       ├── EXE-00.toc
│       ├── localpycs
│       │   ├── pyimod01_archive.pyc
│       │   ├── pyimod02_importers.pyc
│       │   ├── pyimod03_ctypes.pyc
│       │   └── struct.pyc
│       ├── main.pkg
│       ├── PKG-00.toc
│       ├── PYZ-00.pyz
│       ├── PYZ-00.toc
│       ├── warn-main.txt
│       └── xref-main.html
├── dist
│   └── main
├── main.py
└── main.spec
```


## Description

[//]: # "Please check LAB 1 and LAB2"

## Table of Contents

- [Technologies Used](#technologies-used)
- [Installation](#installation)

## Technologies Used

- [Technology 1](#) - Python
- [Technology 2](#) - C++

[//]: # "Project will contain tests"

## Installation

## Please remeber to edit ~/.bashrc

!/bin/bash
sudo apt-get update
sudo apt-get install -f
sudo apt-get install python3-pip
sudo pip3 install psutil
sudo pip3 install PyQt5

### In Linux environment you can use also terminal instead using console ! 
### Windows application also have the same functionality (CMD), please use python3 first.  
## HOW TO OPEN THE APP ? JUST DOUBLE CLICK ON APP IMAGE



##### SCHEMA FOR WHOLE PROJECT

```
├── LAB1
│   ├── Exercise_1
│   │   ├── calculator.py
│   │   └── tests_calculator
│   │       ├── __init__.py
│   │       ├── test_calculator_add.py
│   │       ├── test_calculator_divide.py
│   │       ├── test_calculator_multiply.py
│   │       └── test_calculator_subtract.py
│   ├── Exercise_2
│   │   ├── fibonacci.py
│   │   ├── fib_recursive.py
│   │   └── fib_tests
│   │       ├── __init__.py
│   │       ├── test_fibonacci.py
│   │       └── test_fib_recursive.py
│   ├── Exercise_3
│   │   ├── factorial
│   │   │   ├── iterative.py
│   │   │   └── recursive.py
│   │   └── factorial_tests
│   │       ├── __init__.py
│   │       ├── test_iterative.py
│   │       └── test_recursive.py
│   ├── Exercise_4
│   │   ├── gcd
│   │   │   ├── Euclid_iterative.py
│   │   │   └── Euclid_recursive.py
│   │   └── gcd_Tests
│   │       ├── test_Euclid_iterative.py
│   │       └── test_Euclid_recursive.py
│   ├── Exercise_5
│   │   ├── group_by_extension.py
│   │   └── group_by_tests
│   │       └── test_group_by_extension.py
│   └── Lab1 PyTest.pdf
├── LAB2
│   ├── build
│   │   └── MyTest
│   │       ├── base_library.zip
│   │       ├── localpycs
│   │       │   └── struct.pyc
│   │       ├── MyTest
│   │       ├── MyTest.spec
│   │       ├── PYZ-00.toc
│   │       └── xref-MyTest.html
│   ├── console
│   │   ├── my_test.exe
│   │   ├── MyTest.py
│   │   └── test_MyTest.py
│   ├── dist
│   │   └── MyTest
│   │       ├── _internal
│   │       │   ├── base_library.zip
│   │       │   ├── libatk-1.0.so.0
│   │       │   ├── libatk-bridge-2.0.so.0
│   │       │   ├── libatspi.so.0
│   │       │   ├── libblkid.so.1
│   │       │   ├── libbrotlicommon.so.1
│   │       │   ├── libbrotlidec.so.1
│   │       │   ├── libbsd.so.0
│   │       │   ├── libbz2.so.1.0
│   │       │   ├── libcairo-gobject.so.2
│   │       │   ├── libcairo.so.2
│   │       │   ├── libcap.so.2
│   │       │   ├── libcom_err.so.2
│   │       │   ├── libcrypto.so.3
│   │       │   ├── libdatrie.so.1
│   │       │   ├── libdbus-1.so.3
│   │       │   ├── libdouble-conversion.so.3
│   │       │   ├── lib-dynload
│   │       │   │   ├── _bz2.cpython-310-x86_64-linux-gnu.so
│   │       │   │   ├── _codecs_cn.cpython-310-x86_64-linux-gnu.so
│   │       │   │   ├── _codecs_hk.cpython-310-x86_64-linux-gnu.so
│   │       │   │   ├── _codecs_iso2022.cpython-310-x86_64-linux-gnu.so
│   │       │   │   ├── _codecs_jp.cpython-310-x86_64-linux-gnu.so
│   │       │   │   ├── _codecs_kr.cpython-310-x86_64-linux-gnu.so
│   │       │   │   ├── _codecs_tw.cpython-310-x86_64-linux-gnu.so
│   │       │   │   ├── _contextvars.cpython-310-x86_64-linux-gnu.so
│   │       │   │   ├── _decimal.cpython-310-x86_64-linux-gnu.so
│   │       │   │   ├── _hashlib.cpython-310-x86_64-linux-gnu.so
│   │       │   │   ├── _lzma.cpython-310-x86_64-linux-gnu.so
│   │       │   │   ├── _multibytecodec.cpython-310-x86_64-linux-gnu.so
│   │       │   │   ├── _opcode.cpython-310-x86_64-linux-gnu.so
│   │       │   │   └── resource.cpython-310-x86_64-linux-gnu.so
│   │       │   ├── libepoxy.so.0
│   │       │   ├── libevdev.so.2
│   │       │   ├── libexpat.so.1
│   │       │   ├── libffi.so.8
│   │       │   ├── libfontconfig.so.1
│   │       │   ├── libfreetype.so.6
│   │       │   ├── libfribidi.so.0
│   │       │   ├── libgcc_s.so.1
│   │       │   ├── libgcrypt.so.20
│   │       │   ├── libgdk-3.so.0
│   │       │   ├── libgdk_pixbuf-2.0.so.0
│   │       │   ├── libgio-2.0.so.0
│   │       │   ├── libglib-2.0.so.0
│   │       │   ├── libgmodule-2.0.so.0
│   │       │   ├── libgobject-2.0.so.0
│   │       │   ├── libgpg-error.so.0
│   │       │   ├── libgraphite2.so.3
│   │       │   ├── libgssapi_krb5.so.2
│   │       │   ├── libgthread-2.0.so.0
│   │       │   ├── libgtk-3.so.0
│   │       │   ├── libgudev-1.0.so.0
│   │       │   ├── libharfbuzz.so.0
│   │       │   ├── libicudata.so.56 -> PyQt5/Qt5/lib/libicudata.so.56
│   │       │   ├── libicudata.so.70
│   │       │   ├── libicui18n.so.56 -> PyQt5/Qt5/lib/libicui18n.so.56
│   │       │   ├── libicui18n.so.70
│   │       │   ├── libicuuc.so.56 -> PyQt5/Qt5/lib/libicuuc.so.56
│   │       │   ├── libicuuc.so.70
│   │       │   ├── libinput.so.10
│   │       │   ├── libjpeg.so.8
│   │       │   ├── libk5crypto.so.3
│   │       │   ├── libkeyutils.so.1
│   │       │   ├── libkrb5.so.3
│   │       │   ├── libkrb5support.so.0
│   │       │   ├── liblz4.so.1
│   │       │   ├── liblzma.so.5
│   │       │   ├── libmd4c.so.0
│   │       │   ├── libmd.so.0
│   │       │   ├── libmount.so.1
│   │       │   ├── libmpdec.so.3
│   │       │   ├── libmtdev.so.1
│   │       │   ├── libpango-1.0.so.0
│   │       │   ├── libpangocairo-1.0.so.0
│   │       │   ├── libpangoft2-1.0.so.0
│   │       │   ├── libpcre2-16.so.0
│   │       │   ├── libpcre2-8.so.0
│   │       │   ├── libpcre.so.3
│   │       │   ├── libpixman-1.so.0
│   │       │   ├── libpng16.so.16
│   │       │   ├── libpython3.10.so.1.0
│   │       │   ├── libQt5Core.so.5 -> PyQt5/Qt5/lib/libQt5Core.so.5
│   │       │   ├── libQt5DBus.so.5 -> PyQt5/Qt5/lib/libQt5DBus.so.5
│   │       │   ├── libQt5EglFSDeviceIntegration.so.5
│   │       │   ├── libQt5EglFsKmsSupport.so.5
│   │       │   ├── libQt5Gui.so.5 -> PyQt5/Qt5/lib/libQt5Gui.so.5
│   │       │   ├── libQt5Network.so.5 -> PyQt5/Qt5/lib/libQt5Network.so.5
│   │       │   ├── libQt5QmlModels.so.5 -> PyQt5/Qt5/lib/libQt5QmlModels.so.5
│   │       │   ├── libQt5Qml.so.5 -> PyQt5/Qt5/lib/libQt5Qml.so.5
│   │       │   ├── libQt5Quick.so.5 -> PyQt5/Qt5/lib/libQt5Quick.so.5
│   │       │   ├── libQt5Svg.so.5 -> PyQt5/Qt5/lib/libQt5Svg.so.5
│   │       │   ├── libQt5WaylandClient.so.5 -> PyQt5/Qt5/lib/libQt5WaylandClient.so.5
│   │       │   ├── libQt5WebSockets.so.5 -> PyQt5/Qt5/lib/libQt5WebSockets.so.5
│   │       │   ├── libQt5Widgets.so.5 -> PyQt5/Qt5/lib/libQt5Widgets.so.5
│   │       │   ├── libQt5XcbQpa.so.5 -> PyQt5/Qt5/lib/libQt5XcbQpa.so.5
│   │       │   ├── libselinux.so.1
│   │       │   ├── libstdc++.so.6
│   │       │   ├── libsystemd.so.0
│   │       │   ├── libthai.so.0
│   │       │   ├── libudev.so.1
│   │       │   ├── libuuid.so.1
│   │       │   ├── libwacom.so.9
│   │       │   ├── libwayland-client.so.0
│   │       │   ├── libwayland-cursor.so.0
│   │       │   ├── libwayland-egl.so.1
│   │       │   ├── libX11.so.6
│   │       │   ├── libX11-xcb.so.1
│   │       │   ├── libXau.so.6
│   │       │   ├── libxcb-glx.so.0
│   │       │   ├── libxcb-icccm.so.4
│   │       │   ├── libxcb-image.so.0
│   │       │   ├── libxcb-keysyms.so.1
│   │       │   ├── libxcb-randr.so.0
│   │       │   ├── libxcb-render.so.0
│   │       │   ├── libxcb-render-util.so.0
│   │       │   ├── libxcb-shape.so.0
│   │       │   ├── libxcb-shm.so.0
│   │       │   ├── libxcb-sync.so.1
│   │       │   ├── libxcb-util.so.1
│   │       │   ├── libxcb-xfixes.so.0
│   │       │   ├── libxcb-xinerama.so.0
│   │       │   ├── libxcb-xkb.so.1
│   │       │   ├── libXcomposite.so.1
│   │       │   ├── libXcursor.so.1
│   │       │   ├── libXdamage.so.1
│   │       │   ├── libXdmcp.so.6
│   │       │   ├── libXext.so.6
│   │       │   ├── libXfixes.so.3
│   │       │   ├── libXinerama.so.1
│   │       │   ├── libXi.so.6
│   │       │   ├── libxkbcommon.so.0
│   │       │   ├── libxkbcommon-x11.so.0
│   │       │   ├── libXrandr.so.2
│   │       │   ├── libXrender.so.1
│   │       │   ├── libz.so.1
│   │       │   ├── libzstd.so.1
│   │       │   └── PyQt5
│   │       │       ├── Qt5
│   │       │       │   ├── lib
│   │       │       │   │   ├── libicudata.so.56
│   │       │       │   │   ├── libicui18n.so.56
│   │       │       │   │   ├── libicuuc.so.56
│   │       │       │   │   ├── libQt5Core.so.5
│   │       │       │   │   ├── libQt5DBus.so.5
│   │       │       │   │   ├── libQt5Gui.so.5
│   │       │       │   │   ├── libQt5Network.so.5
│   │       │       │   │   ├── libQt5QmlModels.so.5
│   │       │       │   │   ├── libQt5Qml.so.5
│   │       │       │   │   ├── libQt5Quick.so.5
│   │       │       │   │   ├── libQt5Svg.so.5
│   │       │       │   │   ├── libQt5WaylandClient.so.5
│   │       │       │   │   ├── libQt5WebSockets.so.5
│   │       │       │   │   ├── libQt5Widgets.so.5
│   │       │       │   │   └── libQt5XcbQpa.so.5
│   │       │       │   ├── plugins
│   │       │       │   │   ├── egldeviceintegrations
│   │       │       │   │   │   ├── libqeglfs-emu-integration.so
│   │       │       │   │   │   ├── libqeglfs-kms-egldevice-integration.so
│   │       │       │   │   │   └── libqeglfs-x11-integration.so
│   │       │       │   │   ├── generic
│   │       │       │   │   │   ├── libqevdevkeyboardplugin.so
│   │       │       │   │   │   ├── libqevdevmouseplugin.so
│   │       │       │   │   │   ├── libqevdevtabletplugin.so
│   │       │       │   │   │   ├── libqevdevtouchplugin.so
│   │       │       │   │   │   └── libqtuiotouchplugin.so
│   │       │       │   │   ├── iconengines
│   │       │       │   │   │   └── libqsvgicon.so
│   │       │       │   │   ├── imageformats
│   │       │       │   │   │   ├── libqgif.so
│   │       │       │   │   │   ├── libqicns.so
│   │       │       │   │   │   ├── libqico.so
│   │       │       │   │   │   ├── libqjpeg.so
│   │       │       │   │   │   ├── libqsvg.so
│   │       │       │   │   │   ├── libqtga.so
│   │       │       │   │   │   ├── libqtiff.so
│   │       │       │   │   │   ├── libqwbmp.so
│   │       │       │   │   │   └── libqwebp.so
│   │       │       │   │   ├── platforminputcontexts
│   │       │       │   │   │   ├── libcomposeplatforminputcontextplugin.so
│   │       │       │   │   │   └── libibusplatforminputcontextplugin.so
│   │       │       │   │   ├── platforms
│   │       │       │   │   │   ├── libqeglfs.so
│   │       │       │   │   │   ├── libqlinuxfb.so
│   │       │       │   │   │   ├── libqminimalegl.so
│   │       │       │   │   │   ├── libqminimal.so
│   │       │       │   │   │   ├── libqoffscreen.so
│   │       │       │   │   │   ├── libqvnc.so
│   │       │       │   │   │   ├── libqwayland-egl.so
│   │       │       │   │   │   ├── libqwayland-generic.so
│   │       │       │   │   │   ├── libqwayland-xcomposite-egl.so
│   │       │       │   │   │   ├── libqwayland-xcomposite-glx.so
│   │       │       │   │   │   ├── libqwebgl.so
│   │       │       │   │   │   └── libqxcb.so
│   │       │       │   │   ├── platformthemes
│   │       │       │   │   │   ├── libqgtk3.so
│   │       │       │   │   │   └── libqxdgdesktopportal.so
│   │       │       │   │   ├── wayland-decoration-client
│   │       │       │   │   │   └── libbradient.so
│   │       │       │   │   ├── wayland-graphics-integration-client
│   │       │       │   │   │   ├── libdmabuf-server.so
│   │       │       │   │   │   ├── libdrm-egl-server.so
│   │       │       │   │   │   ├── libqt-plugin-wayland-egl.so
│   │       │       │   │   │   ├── libshm-emulation-server.so
│   │       │       │   │   │   ├── libvulkan-server.so
│   │       │       │   │   │   ├── libxcomposite-egl.so
│   │       │       │   │   │   └── libxcomposite-glx.so
│   │       │       │   │   ├── wayland-shell-integration
│   │       │       │   │   │   ├── libfullscreen-shell-v1.so
│   │       │       │   │   │   ├── libivi-shell.so
│   │       │       │   │   │   ├── libwl-shell.so
│   │       │       │   │   │   ├── libxdg-shell.so
│   │       │       │   │   │   ├── libxdg-shell-v5.so
│   │       │       │   │   │   └── libxdg-shell-v6.so
│   │       │       │   │   └── xcbglintegrations
│   │       │       │   │       ├── libqxcb-egl-integration.so
│   │       │       │   │       └── libqxcb-glx-integration.so
│   │       │       │   └── translations
│   │       │       │       ├── qt_ar.qm
│   │       │       │       ├── qtbase_ar.qm
│   │       │       │       ├── qtbase_bg.qm
│   │       │       │       ├── qtbase_ca.qm
│   │       │       │       ├── qtbase_cs.qm
│   │       │       │       ├── qtbase_da.qm
│   │       │       │       ├── qtbase_de.qm
│   │       │       │       ├── qtbase_en.qm
│   │       │       │       ├── qtbase_es.qm
│   │       │       │       ├── qtbase_fi.qm
│   │       │       │       ├── qtbase_fr.qm
│   │       │       │       ├── qtbase_gd.qm
│   │       │       │       ├── qtbase_he.qm
│   │       │       │       ├── qtbase_hu.qm
│   │       │       │       ├── qtbase_it.qm
│   │       │       │       ├── qtbase_ja.qm
│   │       │       │       ├── qtbase_ko.qm
│   │       │       │       ├── qtbase_lv.qm
│   │       │       │       ├── qtbase_pl.qm
│   │       │       │       ├── qtbase_ru.qm
│   │       │       │       ├── qtbase_sk.qm
│   │       │       │       ├── qtbase_tr.qm
│   │       │       │       ├── qtbase_uk.qm
│   │       │       │       ├── qtbase_zh_TW.qm
│   │       │       │       ├── qt_bg.qm
│   │       │       │       ├── qt_ca.qm
│   │       │       │       ├── qt_cs.qm
│   │       │       │       ├── qt_da.qm
│   │       │       │       ├── qt_de.qm
│   │       │       │       ├── qt_en.qm
│   │       │       │       ├── qt_es.qm
│   │       │       │       ├── qt_fa.qm
│   │       │       │       ├── qt_fi.qm
│   │       │       │       ├── qt_fr.qm
│   │       │       │       ├── qt_gd.qm
│   │       │       │       ├── qt_gl.qm
│   │       │       │       ├── qt_help_ar.qm
│   │       │       │       ├── qt_help_bg.qm
│   │       │       │       ├── qt_help_ca.qm
│   │       │       │       ├── qt_help_cs.qm
│   │       │       │       ├── qt_help_da.qm
│   │       │       │       ├── qt_help_de.qm
│   │       │       │       ├── qt_help_en.qm
│   │       │       │       ├── qt_help_es.qm
│   │       │       │       ├── qt_help_fr.qm
│   │       │       │       ├── qt_help_gl.qm
│   │       │       │       ├── qt_help_hu.qm
│   │       │       │       ├── qt_help_it.qm
│   │       │       │       ├── qt_help_ja.qm
│   │       │       │       ├── qt_help_ko.qm
│   │       │       │       ├── qt_help_pl.qm
│   │       │       │       ├── qt_help_ru.qm
│   │       │       │       ├── qt_help_sk.qm
│   │       │       │       ├── qt_help_sl.qm
│   │       │       │       ├── qt_help_tr.qm
│   │       │       │       ├── qt_help_uk.qm
│   │       │       │       ├── qt_help_zh_CN.qm
│   │       │       │       ├── qt_help_zh_TW.qm
│   │       │       │       ├── qt_he.qm
│   │       │       │       ├── qt_hu.qm
│   │       │       │       ├── qt_it.qm
│   │       │       │       ├── qt_ja.qm
│   │       │       │       ├── qt_ko.qm
│   │       │       │       ├── qt_lt.qm
│   │       │       │       ├── qt_lv.qm
│   │       │       │       ├── qt_pl.qm
│   │       │       │       ├── qt_pt.qm
│   │       │       │       ├── qt_ru.qm
│   │       │       │       ├── qt_sk.qm
│   │       │       │       ├── qt_sl.qm
│   │       │       │       ├── qt_sv.qm
│   │       │       │       ├── qt_tr.qm
│   │       │       │       ├── qt_uk.qm
│   │       │       │       ├── qt_zh_CN.qm
│   │       │       │       └── qt_zh_TW.qm
│   │       │       ├── QtCore.abi3.so
│   │       │       ├── QtGui.abi3.so
│   │       │       ├── QtWidgets.abi3.so
│   │       │       └── sip.cpython-310-x86_64-linux-gnu.so
│   │       └── MyTest
│   ├── Dokumentacja Testów Jednostkowych i Manualnych dla MyTest.pdf
│   ├── ext4
│   │   ├── build
│   │   │   └── MyTest
│   │   │       └── base_library.zip
│   │   ├── installer.py
│   │   ├── MyTest.py
│   │   ├── MyTest.spec
│   │   └── MyTest_test.py
│   ├── MyTest.spec
│   └── Windows_without_console
│       └── my_test.exe
├── README.md
├── Testes_in_Cmake_beta
│   ├── CMakeLists.txt
│   └── tests.cpp
└── Testy_Maciej_43125.pdf

```

