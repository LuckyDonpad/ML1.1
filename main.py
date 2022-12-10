from core.expression import Expression
from core.interface.input import input_expression
from core.interface.output import output_table
from core.utils.utils import proof_general_validity, show_all_false

expression = Expression(input_expression())
table = expression.evaluate_table()
output_table(table, expression.variables_dict)
proof_general_validity(table)
show_all_false(table)
