import sys
from pyke import knowledge_engine
from pyke import krb_traceback, goal

# 创建知识引擎实例
engine = knowledge_engine.engine(__file__)
my_goal = goal.compile('diagnose_rules.plant_diagnosis($plant, $symptom)')

def diagnose_plant(plant, symptom):
    try:
        # 重置引擎
        engine.reset()

        # 激活规则
        print("Activating diagnose_rules")
        engine.activate('diagnose_rules')

        # 开始推理
        print(f"Diagnosing plant {plant} with symptom {symptom}")
        '''
        with engine.prove_goal(
               'bc_example.how_related($person1, $person2, $relationship)',
               person1=person1) \
          as gen:
            for vars, plan in gen:
                print("%s, %s are %s" % \
                        (person1, vars['person2'], vars['relationship']))
        '''
        print("Rules in the knowledge engine:")
        for rule in engine.get_kb('diagnose_rules').rules:
            print(rule)

        with my_goal.prove(engine, plant=plant, symptom=symptom) as gen:
            print("gen:", gen)
            for vars, plan in gen:
                print("%s may have %s" % (vars['plant'], vars['disease']))


    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    # 示例调用
    diagnose_plant("Tomato", "Spots_on_leaves")

