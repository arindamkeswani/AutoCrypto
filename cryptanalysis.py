from flask import Flask, render_template, request, jsonify
import textblob, hashlib,time
from textblob import TextBlob
import pandas as pd
app = Flask(__name__)


def md(pw, counter=1):   #MD5
	# print("Implementing MD5 dictionary attack")
	start= time.time()
	for password in f:
		hash_obj = hashlib.md5(str(password).strip().encode('utf-8')).hexdigest()
		
		# print(f"Trying password {counter} ---> {password}")
		counter+=1

		if hash_obj == pw:
			end= time.time()
			# print(f"Password found: {password}")
			t=end-start
			# print(f"Running time: {t}")
			return f"{password}",f"\nTime taken: {round(t,4)} seconds"
			time.sleep(10)
			break
	end=time.time()
	t=end-start
	return " Not found",f"\nTime taken: {round(t,4)} seconds"
	# else:
	# 	print("Password not found")
	# return "Hello"

def ha1(pw, counter=1):  #SHA1
	# print("Implementing SHA1 dictionary attack")
	start= time.time()
	for password in f:
		
		hash_obj = hashlib.sha1(str(password).strip().encode('utf-8')).hexdigest()
		
		# print(f"Trying password {counter} ---> {password}")
		# counter+=1

		if hash_obj == pw:
			end= time.time()
			t=end-start
			return f"{password}",f"\nTime taken: {round(t,4)} seconds"
			# print(f"Password found: {password}")
			# print(f"Running time: {t}")
			time.sleep(10)
			break
	
	end=time.time()
	t=end-start
	return " Not found",f"\nTime taken: {round(t,4)} seconds"


def ha256(pw, counter=1):  #SHA1
	# print("Implementing SHA1 dictionary attack")
	start= time.time()
	for password in f:
		
		hash_obj = hashlib.sha256(str(password).strip().encode('utf-8')).hexdigest()
		
		# print(f"Trying password {counter} ---> {password}")
		# counter+=1

		if hash_obj == pw:
			end= time.time()
			t=end-start
			return f"{password}",f"\nTime taken: {round(t,4)} seconds"
			# print(f"Password found: {password}")
			# print(f"Running time: {t}")
			time.sleep(10)
			break
	
	end=time.time()
	t=end-start
	return " Not found",f"\nTime taken: {round(t,4)} seconds"


def ha512(pw, counter=1):  #SHA1
	# print("Implementing SHA1 dictionary attack")
	start= time.time()
	for password in f:
		
		hash_obj = hashlib.sha512(str(password).strip().encode('utf-8')).hexdigest()
		
		# print(f"Trying password {counter} ---> {password}")
		# counter+=1

		if hash_obj == pw:
			end= time.time()
			t=end-start
			return f"{password}",f"\nTime taken: {round(t,4)} seconds"
			# print(f"Password found: {password}")
			# print(f"Running time: {t}")
			time.sleep(10)
			break
	
	end=time.time()
	t=end-start
	return " Not found",f"\nTime taken: {round(t,4)} seconds"


def ke256(pw, counter=1):  #SHA1
	# print("Implementing SHA1 dictionary attack")
	start= time.time()
	for password in f:
		
		hash_obj = hashlib.shake_256(str(password).strip().encode('utf-8')).hexdigest(100)
		
		# print(f"Trying password {counter} ---> {password}")
		# counter+=1

		if hash_obj == pw:
			end= time.time()
			t=end-start
			return f"{password}",f"\nTime taken: {round(t,4)} seconds"
			# print(f"Password found: {password}")
			# print(f"Running time: {t}")
			time.sleep(10)
			break
	
	end=time.time()
	t=end-start
	return " Not found",f"\nTime taken: {round(t,4)} seconds"



def caeser(text):
	cipher = text.lower()
	ans=[]

	for k in range(1,26):
		decry=""
		for i in cipher:
			if i==' ':
				decry+=" "
			elif 48<=ord(i)<=57:
				decry+=i
			elif (ord(i)-k) >= 97:
				decry+= chr(ord(i)-k)
			elif (ord(i)-k) < 97:
				decry+= chr(ord(i)+26-k)
		# print(k,":",detect_langs(decry))
		# print(decry)
		lang = TextBlob(decry)  
		#print(lang.detect_language()) 

		if lang.detect_language()=='en':

			ans.append(f"<br/>{k} :{decry}")
			# print()
	return ans

def caeseres(text):
	cipher = text.lower()
	ans=[]

	for k in range(1,26):
		decry=""
		for i in cipher:
			if i==' ':
				decry+=" "
			elif 48<=ord(i)<=57:
				decry+=i
			elif (ord(i)-k) >= 97:
				decry+= chr(ord(i)-k)
			elif (ord(i)-k) < 97:
				decry+= chr(ord(i)+26-k)
		# print(k,":",detect_langs(decry))
		# print(decry)
		lang = TextBlob(decry)  
		#print(lang.detect_language()) 

		if lang.detect_language()=='es':

			ans.append(f"<br/>{k} :{decry}")
			# print()
	return ans

def caeserde(text):
	cipher = text.lower()
	ans=[]

	for k in range(1,26):
		decry=""
		for i in cipher:
			if i==' ':
				decry+=" "
			elif 48<=ord(i)<=57:
				decry+=i
			elif (ord(i)-k) >= 97:
				decry+= chr(ord(i)-k)
			elif (ord(i)-k) < 97:
				decry+= chr(ord(i)+26-k)
		# print(k,":",detect_langs(decry))
		# print(decry)
		lang = TextBlob(decry)  
		#print(lang.detect_language()) 

		if lang.detect_language()=='de':

			ans.append(f"<br/>{k} :{decry}")
			# print()
	return ans

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html', title='About the project')

@app.route('/join', methods=['GET','POST'])
def my_form_post():
	cho = request.form['text1']
	# cho = request.args.get('text1')

	# text2 = request.form['text2']
	# key = request.args.get('text2')

	pw = request.form['text3']
	# pw = request.args.get('text3')
	# ans=[text1,text2,text3]
	if cho=='1':
		ans,tim= md(pw)
	elif cho=='2':
		ans,tim= ha1(pw)
	elif cho=='3':
		ans,tim= ha256(pw)
	elif cho=='4':
		ans,tim= ha512(pw)
	elif cho=='5':
		ans,tim= ke256(pw)
	elif cho=='6':
		ans= caeser(pw)
	elif cho=='7':
		ans= caeseres(pw)
	elif cho=='8':
		ans= caeserde(pw)

	# ans= md(pw)

	if cho=='6' or cho=='7' or cho=='8':
		result = {"Possible plaintexts":ans}
	else:
		result = {"Password":ans,"Time taken":tim }


	# result = {str(key): value for key, value in result.items()}
	return jsonify(result=result)


counter=1 #to count number of tries
t=0 #calculate time
df=pd.read_csv('D:\Arindam\Projects\cryptanalysis\wordlist.csv')

# pw= input("Enter hashed password:")

# print("For MD5, enter 1")
# print("For SHA1, enter 2")
# print("For SHA256, enter 3")
# print("For SHA512, enter 4")
# print("For SHAKE256 , enter 5")

# cho=int(input("Enter your choice: "))

f= df['List']

# if cho==1:
#   md(pw)
# elif cho==2:
#   ha1(pw)
# elif cho==3:
#   ha256(pw)
# elif cho==4:
#   ha512(pw)
# elif cho==5:
#   ke256(pw)


if __name__ == '__main__':
    # app.run(debug=True, port=80, host='0.0.0.0')
    app.run(debug=True)


