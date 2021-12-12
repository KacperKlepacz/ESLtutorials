from myhdl import block, delay, always, now, Signal


@block
def HelloWorld(clk, to="ESL"):

    @always(clk.posedge)
    def say_hello():
        print("%s Hello %s!" % (now(), to))

    return say_hello
