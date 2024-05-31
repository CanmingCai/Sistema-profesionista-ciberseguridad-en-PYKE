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
         ('', '', 'bc_forall.krb'):
           [1716848737.464609, 'bc_forall_bc.py'],
         ('', '', 'family.kfb'):
           [1716848737.4726098, 'family.fbc'],
         ('', '', 'fc_forall.krb'):
           [1716848737.54987, 'fc_forall_fc.py'],
        },
        compiler_version)

