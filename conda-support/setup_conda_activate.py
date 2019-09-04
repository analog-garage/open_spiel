"""
Installs scripts in conda environment's etc/conda directory
to add to PYTHONPATHS
"""

import os
import sys

def main():
    conda_env = os.getenv('CONDA_DEFAULT_ENV')
    if conda_env is None:
        raise AssertionError('Not run from a conda environment')

    if conda_env == 'base':
        raise AssertionError('Cannot be run in base conda environment')

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
export PYTHONPATH_SANS_OPENSPIEL=$PYTHONPATH
export PYTHONPATH=$PYTHONPATH:%s:%s
export OPENSPIEL_CONDA_ENV=%s
""" % (build_dir, source_dir, conda_env))

    with open(deactivate_script, 'w') as f:
        f.write("""
#!/bin/sh
export PYTHONPATH=$PYTHONPATH_SANS_OPENSPIEL
unset PYTHONPATH_SANS_OPENSPIEL
unset OPENSPIEL_CONDA_ENV
""")

if __name__ == '__main__':
    main()
