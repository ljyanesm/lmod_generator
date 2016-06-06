import sys
import os
version_number = ""
keywords = ""
description = ""
print 'whatis("Version: ' + version_number + '")'
print 'whatis("Keywords: '+ keywords + '")'
print 'whatis("Description: ' + description + '")'

dirname = '.'

for path,dirs,files in os.walk(dirname):
    for d in dirs:
        if "lib" in d:
            print 'prepend_path("LD_LIBRARY_PATH", "' + os.path.join(os.path.abspath(path), d) + '")'
            print 'prepend_path("LIBRARY_PATH", "' + os.path.join(os.path.abspath(path), d) + '")'
            if os.path.exists(os.path.join(path,d,"pkgconfig")):
                print 'prepend_path("PKG_CONFIG_PATH"' + os.path.join(os.path.abspath(path), d, "pkgconfig") + '")'
        if "bin" in d:
            print 'prepend_path("PATH", "' + os.path.join(os.path.abspath(path), d) + '")'
        if "man" in d:
            print 'prepend_path("MANPATH", "' + os.path.join(os.path.abspath(path), d) + '")'
        if "share" in d:
            if os.path.exists(os.path.join(path, d, "man")):
                print 'prepend_path("MANPATH", "' + os.path.join(os.path.abspath(path), d, "man") + '")'
        if "include" in d:
            print 'prepend_path("CPATH", "' + os.path.join(os.path.abspath(path), d) + '")'
            print 'prepend_path("CPLUS_INCLUDE_PATH", "' + os.path.join(os.path.abspath(path), d) + '")'
