Electrum-ARG - Lightweight Argentum client
==========================================

::

  Licence: MIT Licence
  Original Author: Thomas Voegtlin
  Port Maintainer: Protonn
  Language: Python
  Homepage: https://www.github.com/argentumproject/electrum-arg
  





Getting started
===============

Electrum is a pure python application. However, if you want to use the
Qt interface, then you need to install the Qt dependencies::

    sudo apt-get install python-qt4

If you downloaded the official package (tar.gz), then you can run
Electrum from its root directory, without installing it on your
system; all the python dependencies are included in the 'packages'
directory. To run Electrum from its root directory, just do::

    ./electrum-arg

You can also install Electrum on your system, by running this command::

    python setup.py install

This will download and install the Python dependencies used by
Electrum, instead of using the 'packages' directory.

If you cloned the git repository, then you need to compile extra files
before you can run Electrum. Read the next section, "Development
Version".



Development version
===================

Check out the code from Github::

    git clone git://github.com/argentumproject/electrum-arg.git
    cd electrum-arg

Run install (this should install dependencies)::

    sudo python setup.py install

Compile the icons file for Qt::

    sudo apt-get install pyqt4-dev-tools
    sudo pyrcc4 icons.qrc -o gui/qt/icons_rc.py

Compile the protobuf description file::

    sudo apt-get install protobuf-compiler
    sudo protoc --proto_path=lib/ --python_out=lib/ lib/paymentrequest.proto

Create translations (optional)::

    sudo apt-get install python-pycurl gettext
    sudo ./contrib/make_locale

Creating Binaries
=================


In order to create binaries, you must create the 'packages' directory::

    pip install ecdsa
    pip install pbkdf2
    pip install qrcode
    pip install dnspython
    pip install jsonrpclib
    sudo ./contrib/make_packages

This directory contains the python dependencies used by Electrum.

Mac OS X
--------

::

    # On MacPorts installs: 
    sudo python setup-release.py py2app
    
    # On Homebrew installs: 
    ARCHFLAGS="-arch i386 -arch x86_64" sudo python setup-release.py py2app --includes sip
    
    sudo hdiutil create -fs HFS+ -volname "Electrum-ARG" -srcfolder dist/Electrum-ARG.app dist/electrum-arg-VERSION-macosx.dmg

Windows
-------

See `contrib/build-wine/README` file.


Android
-------

See `gui/kivy/Readme.txt` file.
