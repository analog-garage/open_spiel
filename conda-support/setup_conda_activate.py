"""
Installs scripts in conda environment's etc/conda directory
to add to PYTHONPATHS
"""

import os
import sys

def main():
    if os.path.basename(sys.prefix) != 'openspiel-dev':
        raise AssertionError('Not run from openspiel-dev conda environment')

    this_dir = os.path.abspath(os.path.dirname(__file__))
    source_dir = os.path.dirname(this_dir)
    build_dir = os.path.join(source_dir, 'build_python_3', 'python')

    etc_conda_dir = os.path.join(sys.prefix, 'etc', 'conda')
    activate_dir = os.path.join(etc_conda_dir, 'activate.d')
    activate_script = os.path.join(activate_dir, 'openspiel_activate.sh')
    deactivate_dir = os.path.join(etc_conda_dir, 'deactivate.d')
    deactivate_script = os.path.join(deactivate_dir, 'openspiel_deactivate.sh')

    if not os.path.exists(activate_dir):
        os.makedirs(activate_dir)
    if not os.path.exists(deactivate_dir):
        os.makedirs(deactivate_dir)

    with open(activate_script, 'w') as f:
        f.write("""
#!/bin/sh
export NOOPENSPIEL_PYTHONPATH=$PYTHONPATH
export PYTHONPATH=$PYTHONPATH:%s:%s
""" % (build_dir, source_dir))

    with open(deactivate_script, 'w') as f:
        f.write("""
#!/bin/sh
export PYTHONPATH=$NOOPENSPIEL_PYTHONPATH
""")

if __name__ == '__main__':
    main()
