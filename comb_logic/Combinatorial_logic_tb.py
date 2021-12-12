import random
from myhdl import block, instance, Signal, intbv, delay
from Combinatorial_logic import mux

random.seed(10)
randrange = random.randrange


@block
def test_mux():

    z, a, b, c, sel = [Signal(intbv(0)) for i in range(5)]

    mux_1 = mux(z, a, b, c, sel)

    @instance
    def stimulus():
        print(
            """
              sel
               |  
            a | \\
            b |  | z
            c | /
            """
        )
        print("z a b c sel")
        for i in range(12):
            a.next, b.next, c.next, sel.next = randrange(8), randrange(8), randrange(8), randrange(3)
            yield delay(10)
            print("%s %s %s %s %s" % (z, a, b, c, sel))

    return mux_1, stimulus


tb = test_mux()
tb.run_sim()
