
import os
import site
import shutil

def main():
    package_root = site.getsitepackages()[0]

    shutil.copyfile('pyspiel.so', os.path.join(package_root, 'pyspiel.so'))
    shutil.copytree('open_spiel', os.path.join(package_root, 'open_spiel'))

if __name__ == '__main__':
    main()
