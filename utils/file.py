def content_of(filepath) -> str:
	with open(filepath) as f: 
		return f.read()