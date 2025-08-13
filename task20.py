class IntFormatter:
    def format(self, value):
        return f"{value:,}"
class FloatFormatter:
    def format(self, value):
        return f"{value:.2f}"
formatters = [IntFormatter(), FloatFormatter()]
for f in formatters:
    print(f.format(12345.678))