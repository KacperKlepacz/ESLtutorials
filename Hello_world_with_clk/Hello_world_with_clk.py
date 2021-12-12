from myhdl import block, delay, always, now, Signal

@block
def HelloWorld():

    clk = Signal(0)

    @always(delay(15))
    def drive_clk():
        clk.next = not clk

    @always(clk.posedge)
    def say_hello():
        print("%s Hello ESL!" % now())

    return drive_clk, say_hello


inst = HelloWorld()
inst.run_sim(120)