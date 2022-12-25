from core.expression import Expression
from core.interface.input import input_messages_consequence
from core.utils.utils import get_theorem, get_disjuncts, resolution_method, get_disjunct_from_keys


condition = input_messages_consequence()
theorem = Expression(get_theorem(condition))
disjuncts = get_disjuncts(theorem.evaluate_table(), theorem.variables_dict)
resolution_method(disjuncts)
