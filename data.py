from tempfile import NamedTemporaryFile

tempfile = NamedTemporaryFile(mode="w", delete=False)

print(tempfile)