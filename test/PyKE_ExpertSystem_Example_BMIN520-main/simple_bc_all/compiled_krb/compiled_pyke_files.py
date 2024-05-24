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
         ('', '', 'bc_simple_rules.krb'):
           [1716508625.230572, 'bc_simple_rules_bc.py'],
         ('', '', 'bc_simple_rules_questions.krb'):
           [1716508625.2430665, 'bc_simple_rules_questions_bc.py'],
         ('', '', 'facts.kfb'):
           [1716508625.2520044, 'facts.fbc'],
         ('', '', 'questions.kqb'):
           [1716508625.2675328, 'questions.qbc'],
        },
        compiler_version)

