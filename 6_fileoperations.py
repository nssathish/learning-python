import os

def copyFilesFrom(sourcePath, targetPath):
	directories = [directory for directory in os.listdir(sourcePath) if directory != ".DS_Store"]
	totalNumberOfFiles = 0
	for directory in directories:
		numberOfFiles = 0
		#print()

		for fileName in os.listdir(os.path.join(sourcePath, directory)):
			'''
			sourceFile = os.path.join(sourcePath, directory, fileName)
			with open(sourceFile, "rb") as sf:
				sourceFileBytes = sf.read()

				targetFile = os.path.join(targetPath, fileName)
				with open(targetFile, "w+b") as tf:
					tf.write(sourceFileBytes)
			print(f"completed writing source file: {sourceFile} as {targetFile}")
			'''
			numberOfFiles += 1
		totalNumberOfFiles += numberOfFiles
		print(f"Directory: {directory} and it's Number of Files copied: {numberOfFiles}")
	print(f"Total files copied: {totalNumberOfFiles}")



if __name__ == "__main__":
	targetpath = sourcepath = ""
	copyFilesFrom(sourcepath, targetpath)
