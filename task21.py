class Guitar:
    def play(self):
        print("Playing guitar :guitar:")
class Piano:
    def play(self):
        print("Playing piano :musical_keyboard:")
for instrument in (Guitar(), Piano()):
    instrument.play()