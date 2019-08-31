# Installation using conda

This is an alternate build/install method for Mac OSX using conda. 

*This has only been tested on Mac OSX 10.14.5 (Mojave) with Xcode 10.1*

## Summary

1. Install conda. If you do not already have anaconda installed, we recommend 
   the minimal Miniconda distribution.

2. Install Xcode either from AppStore or from developer.apple.com.

3.  Run `./conda-install.sh` once to install system packages and download some
    dependencies. (*This is just the submodule section of `install.sh`)

4. Create your conda environment:

   ```bash
   $ conda env create -f conda-support/openspiel-dev.yaml
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
    (openspiel-dev) $ ./open_spiel/scripts/build_and_run_tests.sh
    ```

7.  Configure conda environment to automatically set PYTHONPATH

    ```bash
    (openspiel-dev) $ python conda-support/setup_conda_activate.py
    (openspiel-dev) $ conda deactivate
    $ conda activate openspiel-dev
    (openspiel-dev) $ python -c 'import pyspiel'
    ```

8. Optional extra test

   ```bash
   (openspiel-dev) $ pytest --pyargs open_spiel.python.tests
   ```

## Building conda package

You can build a conda package named `open_spiel` using the supplied recipe:

```bash
$ cd conda-support
$ conda build recipe
```

Note that because open_spiel has no version, a version is hard-coded in the recipe.

If you have made local modifications (e.g. added games), you should probably rename
the package in the recipe to avoid confusion.

