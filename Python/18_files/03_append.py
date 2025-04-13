# Write to a file called  Jogn  Doe.txt 
# It should contain data about John Doe's Hometown

f = open("John Doe.txt", "a")

string = ''' 
John Doe initially lived in Pheonix, Arizona. He is a very nice guy.
'''

f.write(string)

f.close()