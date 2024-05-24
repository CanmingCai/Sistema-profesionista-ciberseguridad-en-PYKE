# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'bc_notany.krb'):
           [1701027050.6139784, 'bc_notany_bc.py'],
         ('', '', 'family.kfb'):
           [1701027050.6169722, 'family.fbc'],
         ('', '', 'fc_notany.krb'):
           [1701027050.6259756, 'fc_notany_fc.py'],
        },
        compiler_version)

