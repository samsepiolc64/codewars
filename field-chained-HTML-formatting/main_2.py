
class Format:
    tags = frozenset(("div", "h1", "p", "span"))
    def __init__(self):
        pass

    class p:
        def __init__ (self, x):
            print('%s%s%s' % ('<p>',x,'</p>'))

    class div(p):
        #def __init__ (self, x):
        #    print('%s%s%s' % ('<div>',x,'</div>'))
        def __getattr__(self, x):
            print(x)
            if x == 0:
                Format.p.__init__(self, x)


format = Format()
format.div('foo')



"""

@test.describe("Sample tests")
def test_samples():
    @test.it("should wrap input in the correct element")
    def correct_element():
        test.assert_equals(format.div("Foo"), "<div>Foo</div>")

    @test.it("should chain call together")
    def chaining():
        test.assert_equals(format.div.h1("Foo"), "<div><h1>Foo</h1></div>")

    @test.it("should allow multiple arguments")
    def multiple_args():
        test.assert_equals(format.div("Foo", "Bar"), "<div>FooBar</div>")

    @test.it("should allow you to store and reuse methods")
    def store_and_reuse():
        wrap_in_div = format.div
        test.assert_equals(wrap_in_div("Foo"), "<div>Foo</div>")


"""