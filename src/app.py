from flask import Flask, render_template, request, jsonify
from bot import BlenderBot

app = Flask(__name__, template_folder='templates')  # Especifica a pasta de templates

chat_bot = BlenderBot()  # Inicializa o bot

# Rota para o cliente web
@app.route('/')
def web_client():
  return render_template('web_client.html')  # Renderiza o template HTML do cliente web

# Rota para a API do chatbot
@app.route('/api', methods=['POST'])
def api():
  try:
    data = request.json  # Obtém o corpo da requisição
    user_input = data.get('user_input', '')  # Obtém a entrada do usuário
    response = chat_bot.get_response(user_input)  # Obtém a resposta do bot
    return jsonify({"response": response})
  except Exception as e:
    return jsonify({"error": str(e)}), 400  # Retorna erro com status 400

if __name__ == '__main__':
  app.run(debug=True)  # Inicia o servidor Flask
