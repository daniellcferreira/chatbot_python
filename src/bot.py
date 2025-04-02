from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
import torch

class BlenderBot:
  
  def __init__(self, model_name='facebook/blenderbot-400M-distill'):
    """
    Inicializa o chatbot BlenderBot.
    - Carrega o tokenizer e o modelo pré-treinado.
    - Define o dispositivo (GPU se disponível, senão CPU).
    """
    self.tokenizer = BlenderbotTokenizer.from_pretrained(model_name)  # Carrega o tokenizer
    self.model = BlenderbotForConditionalGeneration.from_pretrained(model_name)  # Carrega o modelo
    self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')  # Define o dispositivo
    self.model.to(self.device)  # Move o modelo para o dispositivo adequado
    print(f"Modelo carregado no dispositivo: {self.device}")

  def get_response(self, user_input):
    """
    Gera uma resposta com base na entrada do usuário.
    - Tokeniza a entrada e a move para o dispositivo correto.
    - Gera a resposta usando o modelo.
    - Decodifica e retorna a resposta.
    """
    try:
      input_ids = self.tokenizer([user_input], return_tensors='pt', truncation=True, max_length=512).input_ids.to(self.device)  # Tokeniza e move para o dispositivo
      
      with torch.no_grad():  # Desativa o cálculo do gradiente para economizar memória
        response_ids = self.model.generate(input_ids, max_new_tokens=100, num_return_sequences=1)  # Gera resposta
      
      response = self.tokenizer.decode(response_ids[0], skip_special_tokens=True)  # Decodifica a resposta gerada
      return response  # Retorna a resposta final
    except Exception as e:
      return f"Erro ao gerar resposta: {str(e)}"  # Retorna erro caso ocorra algum problema
