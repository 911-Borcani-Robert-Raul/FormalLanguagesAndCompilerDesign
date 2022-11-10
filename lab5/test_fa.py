from fa import FiniteAutomaton

fa = FiniteAutomaton.init_from_file('FA.in')

print(fa.check_word('CCAB'))
print(fa.check_word('ACCB'))
