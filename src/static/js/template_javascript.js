// Função para rolar automaticamente o contêiner de chat para a última mensagem
function autoScrollChatContainer(){
  let chatContainer = $('#chat-container')[0];
  if (chatContainer) {
    $("#chat-container").animate({
      scrollTop: chatContainer.scrollHeight - chatContainer.clientHeight
    }, 1000);
  }
}

// Função para renderizar mensagens do chat na interface
function goRenderizeWidgetChatMessage(originUser, message) {
  let currentDate = new Date(); 
  let hours = currentDate.getHours();
  let minutes = currentDate.getMinutes().toString().padStart(2, '0');
  let time = `${hours}:${minutes}`;

  // Define o ícone e a cor com base no remetente da mensagem
  let icon = (originUser === 'bot') ? 'robot' : 'person-fill';
  let color = (originUser === 'bot') ? 'dark' : 'success';

  // Estrutura HTML da mensagem adicionada ao chat
  let messageWidget = `<div class="row">
                          <div class="col-1">
                              <i class="bi bi-${icon} fs-2 text-${color}"></i>
                          </div>
                          <div class="col-11 text-center">
                              <div class="badge bg-${color} bg-gradient text-wrap mt-3">
                                  ${message}
                              </div>
                              <p class="text-muted"><small>${time}</small></p>
                          </div>  
                      </div>`;

  // Adiciona a mensagem ao chat
  $('#chat-container').append(messageWidget);
  autoScrollChatContainer();
}

// Exibe um indicador de carregamento enquanto o bot está processando a resposta
function startLoading(){
  $("#input-question").val('Aguarde, o Dio Bot está respondendo...').prop('readonly', true);
  $("#btn-send-question").prop('disabled', true);
}

// Retorna o campo de entrada para o estado normal após a resposta do bot
function stopLoading(){
  $("#input-question").val('').prop('readonly', false);
  $("#btn-send-question").prop('disabled', false);
}

// Envia a pergunta do usuário para a API e exibe a resposta
function goSendQuestion(question){
  if(question){
      goRenderizeWidgetChatMessage('user', question); // Exibe a mensagem do usuário
      startLoading(); // Inicia o carregamento
      $.getJSON('/api', {
          user_input: question
      }, function(data) {
          goRenderizeWidgetChatMessage('bot', data); // Exibe a resposta do bot
          stopLoading(); // Finaliza o carregamento
      });
      return false;
  }
}

// Aguarda o carregamento da página e exibe a mensagem inicial do bot
$(document).ready(function() {
  setTimeout(goRenderizeWidgetChatMessage, 2000, 'bot', "Olá, sou o Dio Bot! Como posso ajudar?");
});
