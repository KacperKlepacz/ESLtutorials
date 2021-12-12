from myhdl import block, delay, always, now

@block
def HelloWorld():

    @always(delay(30))
    def say_hello():
        print("%s Hello ESL!" % now())

    return say_hello


inst = HelloWorld()
inst.run_sim(120)