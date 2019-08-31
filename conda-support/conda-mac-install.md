# Installation using conda

This is an alternate build/install method for Mac OSX using conda. 

## Summary

1. Install conda. If you do not already have anaconda installed, we recommend 
   the minimal Miniconda distribution.

2. Install Xcode either from AppStore or from developer.apple.com.

3.  Run `./conda-install.sh` once to install system packages and download some
    dependencies. (*This is just the submodule section of `install.sh`)

4. Create your conda environment:

   ```bash
   $ conda env create -f openspiel-dev.yaml
   ```

   This will create a conda environment named `openspiel-dev` that contains
   the necessary dependencies.

5. Activate the environment:

   ```bash
   $ conda activate openspiel-dev
   (openspiel-dev) $
   ```

   You can deactivate the environment using `conda deactivate`

6.  Build and run tests to check everything works:

    ```bash
    (openspeil-dev) $ ./open_spiel/scripts/build_and_run_tests.sh
    ```

7.  Configure PYTHONPATH

    ```bash
    # For the python modules in open_spiel.
    export PYTHONPATH=$PYTHONPATH:/<path_to_open_spiel>
    # For the Python bindings of Pyspiel
    export PYTHONPATH=$PYTHONPATH:/<path_to_open_spiel>/build_python_3/python
    ```

To make sure OpenSpiel works on the default configurations, we do use the
`python3` command and not `python` (which still defaults to Python 2 on modern
Linux versions).

## Detailed steps

### Installing system-wide dependencies

See `install.sh` for the required packages and cloned repositories.

### Installing Python dependencies

Using a `virtualenv` to install python dependencies is highly recommended. For
more information see:
[https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

Install dependencies (Python 3):

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Alternatively, although not recommended, you can install the Python dependencies
system-wide with:

```bash
pip3 install --upgrade -r requirements.txt
```

### Building and running tests

Make sure that the virtual environment is still activated.

Build and run tests (Python 3):

```bash
mkdir build
cd build
CXX=g++ cmake -DPython_TARGET_VERSION=3.6 -DCMAKE_CXX_COMPILER=${CXX} ../open_spiel
make -j$(nproc)
ctest -j$(nproc)
```

The CMake variable `Python_TARGET_VERSION` is used to specify a Python version.
Any Python library found with CMake modules FindPython2/FindPython3 that agrees
with the major version and is at least as high for minor version and patch
number is accepted. If the variable is not set, the FindPython module is used:
it builds for Python 3 if both Python 2 and Python 3 are available. In the two
examples above, CMake will search for Python 2 and accept any version >= 2.7 or
search for Python 3 and accept any version >= 3.6.

One can run an example of a game running (in the `build/` folder):

```bash
./examples/example --game=tic_tac_toe
```

### Setting Your PYTHONPATH environment variable

To be able to import the Python code (both the C++ binding `pyspiel` and the
rest) from any location, you will need to add to your PYTHONPATH the root
directory and the `open_spiel` directory.

When using a virtualenv, the following should be added to
`<virtualenv>/bin/activate`. For a system-wide install, ddd it in your `.bashrc`
or `.profile`.

```bash
# For the python modules in open_spiel.
export PYTHONPATH=$PYTHONPATH:/<path_to_open_spiel>
# For the Python bindings of Pyspiel
export PYTHONPATH=$PYTHONPATH:/<path_to_open_spiel>/build/python
```

# Running the first example

In the `build` directory, running `examples/example` will prints out a list of
registered games and the usage. Now, let’s play game of Tic-Tac-Toe with uniform
random players:

```bash
examples/example --game=tic_tac_toe
```
