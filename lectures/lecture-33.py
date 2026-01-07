# Python list comprehension

#cleaned [
#   Data transformation
#   For loop
#   Data filtering
#]

domains = ['www.google.com',
           'openai.com',
           'localhost',
           'WWW.DATAWITHBARAA.COM']

cleaned = [
   domain.lower().replace("www.", "")
   for domain in domains
   if "." in domain 
]

print(cleaned)
