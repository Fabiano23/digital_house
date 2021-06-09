# Importa as libs necessárias
from flask import Flask, jsonify, request 

# instancia o objeto do Flask
app = Flask(__name__) #define app using Flask

# define dicionário que vai ser utilizado
dicCidades = [{'nome' : 'Sao Paulo'}, {'nome' : 'Rio de Janeiro'}, {'nome' : 'Belo Horizonte'}]

# serviço a ser executado na raiz do domínio '/'
@app.route('/', methods=['GET'])
def test():
	return jsonify({'mensagem' : 'Ola Mundo!'})

# GET -> retorna todas as cidades
@app.route('/APICidades', methods=['GET'])
def returnAll():
	return jsonify({'cidades' : dicCidades})

# GET -> retorna uma cidade específica, informada na rota
@app.route('/APICidades/<string:nome>', methods=['GET'])
def returnOne(nome):
	lstCidades = [cidade for cidade in dicCidades if cidade['nome'] == nome]
	return jsonify({'cidade' : lstCidades[0]})

# POST -> inclui uma nova cidade através da rota
@app.route('/APICidades', methods=['POST'])
def addOneRot():
	# captura cidade através do parâmetro
    cidade = {'nome' : request.json['nome']}
	# coloca nova cidade no final da lista
    dicCidades.append(cidade)
    return jsonify({'cidades' : dicCidades})

# PUT - Atualiza uma cidade através da rota
@app.route('/APICidades/<string:nome>', methods=['PUT'])
def editOne(nome):
	lstCidades = [cidade for cidade in dicCidades if cidade['nome'] == nome]
	lstCidades[0]['nome'] = request.json['nome']
	return jsonify({'cidade' : lstCidades[0]})

# DELETE -> apaga uma cidade através de parâmetro
@app.route('/APICidades', methods=['DELETE'])
def removeOne():
	parm  = request.args.get('parm', type = str)
	lstCidades = [cidade for cidade in dicCidades if cidade['nome'] == parm]
	dicCidades.remove(lstCidades[0])
	return jsonify({'cidades' : dicCidades})

# inicialização do serviço
if __name__ == '__main__':
	app.run(debug=True, port=5000, host="127.0.0.1") # roda app na porta 8080 em modo debug