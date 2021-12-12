from myhdl import block, always_comb, Signal

@block
def mux(z, a, b, c, sel):

    """ Multiplexer.

    z -- mux output
    a, b, c -- data inputs
    sel -- control input: select a if sel == 0, b if sel == 1, otherwise c

    """

    @always_comb
    def comb():
        if sel == 0:
            z.next = a
        elif sel == 1:
            z.next = b
        else:
            z.next = c

    return comb
