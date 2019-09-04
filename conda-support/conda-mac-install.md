# Installation using conda

This is an alternate build/install method for Mac OSX using conda. 

*This has only been tested on Mac OSX 10.14.5 (Mojave) with Xcode 10.1*

## Summary

1. Install conda 4.7.11 or later. If you do not already have anaconda installed, we recommend 
   the minimal Miniconda distribution. If you already have conda, you can update it using `conda -n base update conda`.

2. Install Xcode either from AppStore or from developer.apple.com.

3.  Run `./install-submodules.sh` once to install system packages and download some
    dependencies. (*This is just the submodule section of `install.sh`)

4. Create your conda environment:

   ```bash
   $ conda env create -f conda-support/openspiel-dev.yaml
   ```

   This will create a conda environment named `openspiel-dev` that contains
   the necessary dependencies.

   If you want to give the environment a different name such as `osdev`, add
   the `-n` argument:

   ```bash
   $ conda env create -n osdev -f conda-support/openspiel-dev.yaml
   ```

5. Activate the environment:

   ```bash
   $ conda activate openspiel-dev
   (openspiel-dev) $
   ```

   You can deactivate the environment using `conda deactivate`

7.  Configure conda environment to automatically modify `PYTHONPATH` when activated and deactivated:

    ```bash
    (openspiel-dev) $ python conda-support/setup_conda_activate.py
    (openspiel-dev) $ conda deactivate
    $ conda activate openspiel-dev
    ```

6.  Build and run tests to check everything works:

    ```bash
    (openspiel-dev) $ ./open_spiel/scripts/build_and_run_tests.sh
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

