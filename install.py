#!/usr/bin/env python

from distutils.spawn import find_executable
import os

if __name__ == '__main__':
    work_root = os.path.join(os.path.dirname(os.path.abspath(__file__)))

    ve = find_executable('virtualenv')
    if not ve:
        raise 'No virtualenv found'

    ve_dir = "%(work_root)s/.virtualenv" %  locals()

    os.system("mkdir -p %(ve_dir)s" % locals())
    os.system("virtualenv %(ve_dir)s" % locals())
    os.system("%(ve_dir)s/bin/pip install -r %(work_root)s/requirements.txt" % locals())

    script_filename = '%(work_root)s/bin/epgen' % locals()
    with open(script_filename, 'w') as f:
        os.chmod(script_filename, 0755)
        f.write("#!/bin/bash\n\n")
        f.write("%(ve_dir)s/bin/python %(work_root)s/epgen/epgen.py $*\n" % locals())

    with open('%s/.bashrc' % os.environ['HOME'], 'a') as f:
        f.write("export PATH=%(work_root)s/bin:$PATH\n" % locals())

