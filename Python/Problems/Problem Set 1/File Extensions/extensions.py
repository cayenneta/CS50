def main():
	chosen_file = input("What file do you want to know about? ")
	chosen_file = chosen_file.lower()
	chosen_file_sanitized = chosen_file[chosen_file.rfind('.') + 1:].replace(' ','')
	extension_dict = {
	"jpg" : "image/jpeg",
	"gif" : "image/gif",
	"jpeg" : "image/jpeg",
	"png" : "image/png",
	"pdf" : "application/pdf",
	"txt" : "text/plain",
	"zip" : "application/zip",
	}
	if chosen_file_sanitized in extension_dict:
		print(extension_dict[chosen_file_sanitized])
	else:
		print("application/octet-stream")
if __name__ == '__main__':
	main()
