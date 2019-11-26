from flask import Flask, request, jsonify

import os

app = Flask(__name__)


@app.route('/', methods = ['POST'])
def call():
	str1=" "
	currDir = os.path.dirname(__file__)
	MSG = str(request.json.get('MSG'))
	if MSG=="agitation":
		aaa = open((os.path.join(currDir,"agitation.txt")),'r')
		with aaa as txt :
			data = txt.readlines()
			for row in data:
				str1+=str(row)+" , " 
			msg = {"drugs" : str1}
			return jsonify(msg)
	elif MSG == 'allergies':
		aaa = open((os.path.join(currDir,"allergies.txt")),'r')
		with aaa as txt :
			data = txt.readlines()
			for row in data:
				str1+=str(row)+" , "
			msg = {"drugs" : str1}
			return jsonify(msg)
	elif MSG == 'anxiety':
		aaa = open((os.path.join(currDir,"anxiety.txt")),'r')
		with aaa as txt :
			data = txt.readlines()
			for row in data:
				str1+=str(row)+" , "
			msg = {"drugs" : str1}
			return jsonify(msg)
	elif MSG == 'asthma':
		aaa = open((os.path.join(currDir,"asthma.txt")),'r')
		with aaa as txt :
			data = txt.readlines()
			for row in data:
				str1+=str(row)+" , "
			msg = {"drugs" : str1}
			return jsonify(msg)
	elif MSG == 'cancer':
		aaa = open((os.path.join(currDir,"cancer.txt")),'r')
		with aaa as txt :
			data = txt.readlines()
			for row in data:
				str1+=str(row)+" , "
			msg = {"drugs" : str1}
			return jsonify(msg)
	elif MSG == 'cholestr1ol':
		aaa = open((os.path.join(currDir,"cholestr1ol.txt")),'r')
		with aaa as txt :
			data = txt.readlines()
			for row in data:
				str1+=str(row)+" , "
			msg = {"drugs" : str1}
			return jsonify(msg)
	elif MSG == 'depression':
		aaa = open((os.path.join(currDir,"depression.txt")),'r')
		with aaa as txt :
			data = txt.readlines()
			for row in data:
				str1+=str(row)+" , "
			msg = {"drugs" : str1}
			return jsonify(msg)
	elif MSG == 'diabT1':
		aaa = open((os.path.join(currDir,"diabT1.txt")),'r')
		with aaa as txt :
			data = txt.readlines()
			for row in data:
				str1+=str(row)+" , "
			msg = {"drugs" : str1}
			return jsonify(msg)
	elif MSG == 'hairloss':
		aaa = open((os.path.join(currDir,"hairloss.txt")),'r')
		with aaa as txt :
			data = txt.readlines()
			for row in data:
				str1+=str(row)+" , "
			msg = {"drugs" : str1}
			return jsonify(msg)
	elif MSG == 'herpes':
		aaa = open((os.path.join(currDir,"herpes.txt")),'r')
		with aaa as txt :
			data = txt.readlines()
			for row in data:
				str1+=str(row)+" , "
			msg = {"drugs" : str1}
			return jsonify(msg)
	elif MSG == 'Insomnia':
		aaa = open((os.path.join(currDir,"Insomnia.txt")),'r')
		with aaa as txt :
			data = txt.readlines()
			for row in data:
				str1+=str(row)+" , "
			msg = {"drugs" : str1}
			return jsonify(msg)
	elif MSG == 'migrane':
		aaa = open((os.path.join(currDir,"migrane.txt")),'r')
		with aaa as txt :
			data = txt.readlines()
			for row in data:
				str1+=str(row)+" , "
			msg = {"drugs" : str1}
			return jsonify(msg)
	elif MSG == 'obesity':
		aaa = open((os.path.join(currDir,"obesity.txt")),'r')
		with aaa as txt :
			data = txt.readlines()
			for row in data:
				str1+=str(row)+" , "
			msg = {"drugs" : str1}
			return jsonify(msg)
	else:
		msg = {"error" : "file not found"}
		return jsonify(msg)

if __name__ == '__main__': 
	app.run(debug = True)