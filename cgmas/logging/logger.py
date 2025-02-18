from logging import Logger


class cgmasLogger(Logger):
	def __init__(self, name):
		super().__init__(name)
		self.name = name
