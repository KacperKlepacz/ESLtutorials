from myhdl import block, Signal

from clk_driver import ClkDriver
from Hello_world import HelloWorld


@block
def Greetings():

    clk1 = Signal(0)
    clk2 = Signal(0)

    clkdriver_1 = ClkDriver(clk1)  # positional and default association
    clkdriver_2 = ClkDriver(clk=clk2, period=10)  # named association
    hello_1 = HelloWorld(clk=clk1)  # named and default association
    hello_2 = HelloWorld(to="ESL_v2", clk=clk2)  # named association

    return clkdriver_1, clkdriver_2, hello_1, hello_2


inst = Greetings()
inst.run_sim(100)
