class TestClass:
    def test_one(self):
        """Documentation of test_one"""
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'bang_zoom')

    def test_three(self):
        x = 'shorty'
        assert x.find('longy') != -1
