import contextlib
import sys

from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)


cyber_threat_mapping = {
    1: "Phishing",
    2: "Malware",
    3: "Ransomware",
    4: "Gusano",
    5: "Estas seguro"
}

report_to_mapping = {
    1: "Jazz",
    2: "Ricardo",
    3: "Caro",
    4: "Muy mal"
}

action_mapping = {
    "no_amenazas": "No tienes amenazas",
    "reportar_phishing": "Reportar phishing",
    "correr_antivirus": "Correr antivirus",
    "respaldo": "Hacer respaldo",
    "preguntar_leyva": "Hay que preguntar a Leyva"
}

def bc_test():

    engine.reset()      # Allows us to run tests multiple times.

    engine.activate('bc_simple_rules') #STUDENTS: you will need to edit the name of your rule file here

    print("doing proof")
    try:
        with engine.prove_goal('bc_simple_rules.what_to_bring($bring)') as gen: #STUDENTS: you will need to edit this line
            for vars, plan in gen:
                print("You should bring: %s" % (vars['bring'])) #STUDENTS: you will need to edit this line
    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("done")
    #engine.print_stats()

    
def bc_test_questions():

    engine.reset()      # Allows us to run tests multiple times.

    engine.activate('bc_simple_rules_questions') #STUDENTS: you will need to edit the name of your rule file here

    print("doing proof")
    
    try:
        # with engine.prove_goal('bc_simple_rules_questions.what_to_bring($bring)') as gen: #STUDENTS: you will need to edit this line
        #     for vars, plan in gen:
        #         print("You should bring: %s" % (vars['bring']))

        # ==============primer prueba================
        # with engine.prove_goal('bc_simple_rules_questions.cyber_threat_result($result)') as gen:  # Second section
        #     for vars, plan in gen:
        #         result_text = cyber_threat_mapping[vars['result']]
        #         print("Tienes amenazas de : %s" % result_text)
        
        # with engine.prove_goal('bc_simple_rules_questions.report_to_person($people)') as gen:  # Second section
        #     for vars, plan in gen:
        #         result_text = report_to_mapping[vars['people']]
        #         print("Tienes que reportar: %s" % result_text)

        # ==============segunda prueba================
        result_gen = []
        with engine.prove_goal('bc_simple_rules_questions.what_to_do($action)') as gen:
            for vars, plan in gen:
                result_gen.append(vars)
                action_text = action_mapping[vars['action']]
                print("Recommended action: %s" % action_text)

        print("===result_gen====: ", result_gen)        

    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("done")

if __name__ == "__main__":
    #bc_test()
    bc_test_questions()


