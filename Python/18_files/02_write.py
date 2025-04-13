# Write to a file called  Jogn  Doe.txt 
# It should contain data about John Doe

f = open("John Doe.txt", "w")

string = ''' 
John Doe is a nice guy. He lives in Nyc and he works with Python His favourite package is Pandas
'''

f.write(string)

f.close()