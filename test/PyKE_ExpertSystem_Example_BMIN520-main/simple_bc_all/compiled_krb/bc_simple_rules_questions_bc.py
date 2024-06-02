# bc_simple_rules_questions_bc.py

from __future__ import with_statement
import itertools
from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def no_rain(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_raining', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.no_rain: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_raincoat(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_raining', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_bring_raincoat: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_windy', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.what_to_bring_raincoat: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_umbrella(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_raining', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_bring_umbrella: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_windy', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.what_to_bring_umbrella: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_marshmellos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'any_disasters', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_bring_marshmellos: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_kite(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'any_disasters', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_bring_kite: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,3):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_tissues(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'any_disasters', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_bring_tissues: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (4,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cyber_threat_report(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'cyber_threat', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.cyber_threat_report: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1, 2, 3, 4):
              mark3 = context.mark(True)
              if rule.pattern(1).match_data(context, context,
                      context.lookup_data('ans')):
                context.end_save_all_undo()
                rule.rule_base.num_bc_rule_successes += 1
                yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark3)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def reporting_person(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'report_to', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.reporting_person: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                    context.lookup_data('ans')):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_threat(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'has_phishing_email', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.no_threat: got unexpected plan from when clause 1"
            with engine.prove('questions', 'has_malware', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.no_threat: got unexpected plan from when clause 2"
                with engine.prove('questions', 'has_ransomware', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.no_threat: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def handle_phishing(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'has_phishing_email', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.handle_phishing: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def handle_malware(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'has_malware', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.handle_malware: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_system_slow', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.handle_malware: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def handle_ransomware(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'has_ransomware', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.handle_ransomware: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def handle_gusano(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_system_slow', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.handle_gusano: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def handle_s1_caso1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'seccion1_p1', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.handle_s1_caso1: got unexpected plan from when clause 1"
            with engine.prove('questions', 'seccion1_p2', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.handle_s1_caso1: got unexpected plan from when clause 2"
                with engine.prove('questions', 'seccion1_p3', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.handle_s1_caso1: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'seccion1_p4', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules_questions.handle_s1_caso1: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def handle_s1_caso2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'seccion1_p1', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.handle_s1_caso2: got unexpected plan from when clause 1"
            with engine.prove('questions', 'seccion1_p2', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.handle_s1_caso2: got unexpected plan from when clause 2"
                with engine.prove('questions', 'seccion1_p3', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.handle_s1_caso2: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'seccion1_p4', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules_questions.handle_s1_caso2: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def handle_s1_caso3(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'seccion1_p1', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.handle_s1_caso3: got unexpected plan from when clause 1"
            with engine.prove('questions', 'seccion1_p2', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.handle_s1_caso3: got unexpected plan from when clause 2"
                with engine.prove('questions', 'seccion1_p3', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.handle_s1_caso3: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'seccion1_p4', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules_questions.handle_s1_caso3: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def handle_s1_caso4(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'seccion1_p1', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.handle_s1_caso4: got unexpected plan from when clause 1"
            with engine.prove('questions', 'seccion1_p2', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.handle_s1_caso4: got unexpected plan from when clause 2"
                with engine.prove('questions', 'seccion1_p3', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.handle_s1_caso4: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'seccion1_p4', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules_questions.handle_s1_caso4: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def handle_s1_caso5(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'seccion1_p1', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.handle_s1_caso5: got unexpected plan from when clause 1"
            with engine.prove('questions', 'seccion1_p2', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.handle_s1_caso5: got unexpected plan from when clause 2"
                with engine.prove('questions', 'seccion1_p3', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.handle_s1_caso5: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'seccion1_p4', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules_questions.handle_s1_caso5: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def handle_s1_caso6(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'seccion1_p1', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.handle_s1_caso6: got unexpected plan from when clause 1"
            with engine.prove('questions', 'seccion1_p2', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.handle_s1_caso6: got unexpected plan from when clause 2"
                with engine.prove('questions', 'seccion1_p3', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.handle_s1_caso6: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'seccion1_p4', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules_questions.handle_s1_caso6: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def handle_s1_caso7(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'seccion1_p1', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.handle_s1_caso7: got unexpected plan from when clause 1"
            with engine.prove('questions', 'seccion1_p2', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.handle_s1_caso7: got unexpected plan from when clause 2"
                with engine.prove('questions', 'seccion1_p3', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.handle_s1_caso7: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'seccion1_p4', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules_questions.handle_s1_caso7: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def handle_s1_caso8(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'seccion1_p1', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.handle_s1_caso8: got unexpected plan from when clause 1"
            with engine.prove('questions', 'seccion1_p2', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.handle_s1_caso8: got unexpected plan from when clause 2"
                with engine.prove('questions', 'seccion1_p3', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.handle_s1_caso8: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'seccion1_p4', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules_questions.handle_s1_caso8: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def handle_s1_caso9(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'seccion1_p1', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.handle_s1_caso9: got unexpected plan from when clause 1"
            with engine.prove('questions', 'seccion1_p2', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.handle_s1_caso9: got unexpected plan from when clause 2"
                with engine.prove('questions', 'seccion1_p3', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.handle_s1_caso9: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'seccion1_p4', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules_questions.handle_s1_caso9: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def handle_s1_caso10(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'seccion1_p1', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.handle_s1_caso10: got unexpected plan from when clause 1"
            with engine.prove('questions', 'seccion1_p2', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.handle_s1_caso10: got unexpected plan from when clause 2"
                with engine.prove('questions', 'seccion1_p3', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.handle_s1_caso10: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'seccion1_p4', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules_questions.handle_s1_caso10: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def handle_s1_caso11(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'seccion1_p1', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.handle_s1_caso11: got unexpected plan from when clause 1"
            with engine.prove('questions', 'seccion1_p2', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.handle_s1_caso11: got unexpected plan from when clause 2"
                with engine.prove('questions', 'seccion1_p3', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.handle_s1_caso11: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'seccion1_p4', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules_questions.handle_s1_caso11: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def handle_s1_caso12(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'seccion1_p1', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.handle_s1_caso12: got unexpected plan from when clause 1"
            with engine.prove('questions', 'seccion1_p2', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.handle_s1_caso12: got unexpected plan from when clause 2"
                with engine.prove('questions', 'seccion1_p3', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.handle_s1_caso12: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'seccion1_p4', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules_questions.handle_s1_caso12: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_simple_rules_questions')
  
  bc_rule.bc_rule('no_rain', This_rule_base, 'what_to_bring',
                  no_rain, None,
                  (pattern.pattern_literal('no_rain_gear'),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_bring_raincoat', This_rule_base, 'what_to_bring',
                  what_to_bring_raincoat, None,
                  (pattern.pattern_literal('raincoat'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_bring_umbrella', This_rule_base, 'what_to_bring',
                  what_to_bring_umbrella, None,
                  (pattern.pattern_literal('umbrella'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_bring_marshmellos', This_rule_base, 'what_to_bring',
                  what_to_bring_marshmellos, None,
                  (pattern.pattern_literal('marshmellos'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_to_bring_kite', This_rule_base, 'what_to_bring',
                  what_to_bring_kite, None,
                  (pattern.pattern_literal('kite'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_to_bring_tissues', This_rule_base, 'what_to_bring',
                  what_to_bring_tissues, None,
                  (pattern.pattern_literal('tissues'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('cyber_threat_report', This_rule_base, 'cyber_threat_result',
                  cyber_threat_report, None,
                  (contexts.variable('result'),),
                  (),
                  (contexts.variable('ans'),
                   contexts.variable('result'),))
  
  bc_rule.bc_rule('reporting_person', This_rule_base, 'report_to_person',
                  reporting_person, None,
                  (contexts.variable('people'),),
                  (),
                  (contexts.variable('ans'),
                   contexts.variable('people'),))
  
  bc_rule.bc_rule('no_threat', This_rule_base, 'what_to_do',
                  no_threat, None,
                  (pattern.pattern_literal('no_amenazas'),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('handle_phishing', This_rule_base, 'what_to_do',
                  handle_phishing, None,
                  (pattern.pattern_literal('reportar_phishing'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('handle_malware', This_rule_base, 'what_to_do',
                  handle_malware, None,
                  (pattern.pattern_literal('correr_antivirus'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('handle_ransomware', This_rule_base, 'what_to_do',
                  handle_ransomware, None,
                  (pattern.pattern_literal('respaldo'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('handle_gusano', This_rule_base, 'what_to_do',
                  handle_gusano, None,
                  (pattern.pattern_literal('preguntar_leyva'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('handle_s1_caso1', This_rule_base, 'seccion1',
                  handle_s1_caso1, None,
                  (pattern.pattern_literal('caso1'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('handle_s1_caso2', This_rule_base, 'seccion1',
                  handle_s1_caso2, None,
                  (pattern.pattern_literal('caso2'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('handle_s1_caso3', This_rule_base, 'seccion1',
                  handle_s1_caso3, None,
                  (pattern.pattern_literal('caso3'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('handle_s1_caso4', This_rule_base, 'seccion1',
                  handle_s1_caso4, None,
                  (pattern.pattern_literal('caso4'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('handle_s1_caso5', This_rule_base, 'seccion1',
                  handle_s1_caso5, None,
                  (pattern.pattern_literal('caso2'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('handle_s1_caso6', This_rule_base, 'seccion1',
                  handle_s1_caso6, None,
                  (pattern.pattern_literal('caso6'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('handle_s1_caso7', This_rule_base, 'seccion1',
                  handle_s1_caso7, None,
                  (pattern.pattern_literal('caso4'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('handle_s1_caso8', This_rule_base, 'seccion1',
                  handle_s1_caso8, None,
                  (pattern.pattern_literal('caso8'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('handle_s1_caso9', This_rule_base, 'seccion1',
                  handle_s1_caso9, None,
                  (pattern.pattern_literal('caso4'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('handle_s1_caso10', This_rule_base, 'seccion1',
                  handle_s1_caso10, None,
                  (pattern.pattern_literal('caso8'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('handle_s1_caso11', This_rule_base, 'seccion1',
                  handle_s1_caso11, None,
                  (pattern.pattern_literal('caso2'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('handle_s1_caso12', This_rule_base, 'seccion1',
                  handle_s1_caso12, None,
                  (pattern.pattern_literal('caso3'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))


Krb_filename = '..\\bc_simple_rules_questions.krb'
Krb_lineno_map = (
    ((16, 20), (4, 4)),
    ((22, 27), (6, 6)),
    ((40, 44), (9, 9)),
    ((46, 51), (11, 11)),
    ((52, 57), (12, 12)),
    ((70, 74), (15, 15)),
    ((76, 81), (17, 17)),
    ((82, 87), (18, 18)),
    ((100, 104), (21, 21)),
    ((106, 111), (23, 23)),
    ((112, 112), (24, 24)),
    ((125, 129), (27, 27)),
    ((131, 136), (29, 29)),
    ((137, 137), (30, 30)),
    ((150, 154), (33, 33)),
    ((156, 161), (35, 35)),
    ((162, 162), (36, 36)),
    ((175, 179), (41, 41)),
    ((181, 186), (43, 43)),
    ((187, 187), (44, 44)),
    ((190, 190), (45, 45)),
    ((206, 210), (48, 48)),
    ((212, 217), (50, 50)),
    ((220, 220), (51, 51)),
    ((236, 240), (55, 55)),
    ((242, 247), (57, 57)),
    ((248, 253), (58, 58)),
    ((254, 259), (59, 59)),
    ((272, 276), (62, 62)),
    ((278, 283), (64, 64)),
    ((296, 300), (67, 67)),
    ((302, 307), (69, 69)),
    ((308, 313), (70, 70)),
    ((326, 330), (73, 73)),
    ((332, 337), (75, 75)),
    ((350, 354), (78, 78)),
    ((356, 361), (80, 80)),
    ((374, 378), (86, 86)),
    ((380, 385), (88, 88)),
    ((386, 391), (89, 89)),
    ((392, 397), (90, 90)),
    ((398, 403), (91, 91)),
    ((416, 420), (94, 94)),
    ((422, 427), (96, 96)),
    ((428, 433), (97, 97)),
    ((434, 439), (98, 98)),
    ((440, 445), (99, 99)),
    ((458, 462), (102, 102)),
    ((464, 469), (104, 104)),
    ((470, 475), (105, 105)),
    ((476, 481), (106, 106)),
    ((482, 487), (107, 107)),
    ((500, 504), (110, 110)),
    ((506, 511), (112, 112)),
    ((512, 517), (113, 113)),
    ((518, 523), (114, 114)),
    ((524, 529), (115, 115)),
    ((542, 546), (118, 118)),
    ((548, 553), (120, 120)),
    ((554, 559), (121, 121)),
    ((560, 565), (122, 122)),
    ((566, 571), (123, 123)),
    ((584, 588), (126, 126)),
    ((590, 595), (128, 128)),
    ((596, 601), (129, 129)),
    ((602, 607), (130, 130)),
    ((608, 613), (131, 131)),
    ((626, 630), (134, 134)),
    ((632, 637), (136, 136)),
    ((638, 643), (137, 137)),
    ((644, 649), (138, 138)),
    ((650, 655), (139, 139)),
    ((668, 672), (142, 142)),
    ((674, 679), (144, 144)),
    ((680, 685), (145, 145)),
    ((686, 691), (146, 146)),
    ((692, 697), (147, 147)),
    ((710, 714), (150, 150)),
    ((716, 721), (152, 152)),
    ((722, 727), (153, 153)),
    ((728, 733), (154, 154)),
    ((734, 739), (155, 155)),
    ((752, 756), (158, 158)),
    ((758, 763), (160, 160)),
    ((764, 769), (161, 161)),
    ((770, 775), (162, 162)),
    ((776, 781), (163, 163)),
    ((794, 798), (166, 166)),
    ((800, 805), (168, 168)),
    ((806, 811), (169, 169)),
    ((812, 817), (170, 170)),
    ((818, 823), (171, 171)),
    ((836, 840), (174, 174)),
    ((842, 847), (176, 176)),
    ((848, 853), (177, 177)),
    ((854, 859), (178, 178)),
    ((860, 865), (179, 179)),
)
