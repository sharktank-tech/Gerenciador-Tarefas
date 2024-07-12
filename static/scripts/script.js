$(document).ready(function() {
    // Função para abrir o popup ao clicar no botão de enviar email
    $("#btn-email").click(function() {
        $("#email-popup").fadeIn();
    });

    // Função para fechar o popup ao clicar no botão de fechar
    $("#close-email-popup").click(function() {
        $("#email-popup").fadeOut();
    });
});