class html:
    def __init__(self, tags=[]):
        self.tags = tags
    def __getattr__(self, tag):
        return html(self.tags + [tag])
    def __call__(self, *text):
        ret = ''.join(text)
        for tag in self.tags[::-1]:
            ret = f"<{tag}>{ret}</{tag}>"
        return ret


Format = html()
print(Format.div("Foo", "Bar"))



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