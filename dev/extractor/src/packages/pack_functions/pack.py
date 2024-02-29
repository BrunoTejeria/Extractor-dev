
class Console():
	def __init__(self):
		self.print = Console.Print.print
		self.input = Console.Input.input

	class Print():
		@staticmethod
		def print(*args, **kwargs):
			print(*args, **kwargs)

	class Input():
		@staticmethod
		def input(text):
			return input(text)