# driver.py

from __future__ import with_statement
import sys
from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)

def fc_test():
    engine.reset()
    try:
        engine.activate('fc_forall')
    except:
        krb_traceback.print_exc()
        sys.exit(1)

def bc_test():
    engine.reset()
    try:
        engine.activate('bc_forall')
        with engine.prove_goal('bc_forall.no_step_siblings($child)') as gen:
            for vars, plan in gen:
                print(vars['child'])
    except:
        krb_traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    #fc_test()
    bc_test()

