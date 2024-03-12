class Polynomial:

    class TermNode:

        def __init__(self, coefficient, exponent, next = None):
            self.coefficient = coefficient
            self.exponent = exponent
            self.next = next

        def __eq__(self, other):
            if other is None:
                return False
            return self.coefficient == other.coefficient and self.exponent == other.exponent

        def __ne__(self, other):
            return not self == other

    def __init__(self, coefficient, exponent):
        self._first_node = self.TermNode(coefficient, exponent)

    def _add_single_term_node(self, term_node):
        if term_node.exponent > self._first_node.exponent:
            old_first = self._first_node
            self._first_node = self.TermNode(term_node.coefficient, term_node.exponent)
            self._first_node.next = old_first
        elif term_node.exponent == self._first_node.exponent:
            self._first_node.coefficient += term_node.coefficient
        else:
            current_term_node = self._first_node
            while current_term_node.next != None:
                if term_node.exponent > current_term_node.next.exponent:
                    old_next = current_term_node.next
                    current_term_node.next = self.TermNode(term_node.coefficient, term_node.exponent)
                    current_term_node.next.next = old_next
                    break
                elif term_node.exponent == current_term_node.next.exponent:
                    current_term_node.next.coefficient += term_node.coefficient
                    break
                else:
                    current_term_node = current_term_node.next
            else:
                current_term_node.next = self.TermNode(term_node.coefficient, term_node.exponent)

    def __add__(self, other):
        new_polynomial = Polynomial(self._first_node.coefficient, self._first_node.exponent)
        next_node_to_add = self._first_node.next
        while next_node_to_add is not None:
            new_polynomial._add_single_term_node(next_node_to_add)
            next_node_to_add = next_node_to_add.next
        next_node_to_add = other._first_node
        while next_node_to_add is not None:
            new_polynomial._add_single_term_node(next_node_to_add)
            next_node_to_add = next_node_to_add.next

        return new_polynomial

    def __mul__(self, other):
        result = None
        my_current_term = self._first_node
        while my_current_term is not None:
            other_current_term = other._first_node
            while other_current_term is not None:
                next_term = self.TermNode(my_current_term.coefficient * other_current_term.coefficient, my_current_term.exponent + other_current_term.exponent)
                if result is None:
                    result = Polynomial(next_term.coefficient, next_term.exponent)
                else:
                    result._add_single_term_node(next_term)
                other_current_term = other_current_term.next
            my_current_term = my_current_term.next
        return result

    def differentiate(self):
        result = Polynomial(self._first_node.coefficient*self._first_node.exponent, self._first_node.exponent-1)
        current_term = self._first_node.next
        while current_term is not None:
            result._add_single_term_node( self.TermNode(current_term.coefficient * current_term.exponent, current_term.exponent-1) )
            current_term = current_term.next

        return result

    def integrate(self):
        result = Polynomial(self._first_node.coefficient / (self._first_node.exponent + 1), self._first_node.exponent + 1)
        current_term = self._first_node.next
        while current_term is not None:
            result._add_single_term_node(
                self.TermNode(current_term.coefficient / (current_term.exponent+1), current_term.exponent + 1))
            current_term = current_term.next

        return result

    def __eq__(self, other):
        current_term = self._first_node
        other_current_term = other._first_node

        while current_term is not None and other_current_term is not None:
            if current_term.coefficient == other_current_term.coefficient and current_term.exponent == other_current_term.exponent:
                current_term = current_term.next
                other_current_term = other_current_term.next
            else:
                return False
        return current_term is None and other_current_term is None

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        result = ""
        current_node = self._first_node

        while current_node is not None:
            result += f'{current_node.coefficient: .2f}x^{current_node.exponent}'
            if current_node.next is not None:
                if current_node.next.coefficient > 0:
                    result += " + "
                elif current_node.next.coefficient < 0:
                    result += " - "

            current_node = current_node.next

        return result[:-2]


poly2 = Polynomial(2,3) # makes the polynomial 2.00x^3
poly3 = Polynomial(3,4) # makes the polynomial 3.00x^4
poly1 = poly2 + poly3; # makes poly1 = 3.00x^4 + 2.00x^3
print(poly1) # prints out 3.0x^4 + 2.00x^3
poly3 = poly2*poly1 # sets poly3 to 6.00x^7+4.00x^6
print(poly3)
poly4 = poly3.differentiate() # sets poly4 to 42.00x^6+24.00x^5
print(poly4)
poly5 = poly1.integrate() # sets poly5 to .60x^5+.50x^4
print(poly5)


