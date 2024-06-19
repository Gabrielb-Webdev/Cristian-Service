<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Recibir datos del formulario
    $name = $_POST['name'];
    $email = $_POST['email'];
    $subject = $_POST['subject'];
    $message = $_POST['message'];
    
    // Configurar destinatario
    $to = 'info@digitalservice.com.ar';
    
    // Construir mensaje de correo
    $body = "Nombre: $name\n";
    $body .= "Correo: $email\n";
    $body .= "Asunto: $subject\n";
    $body .= "Mensaje:\n$message";
    
    // Configurar cabeceras
    $headers = "From: $email\r\n";
    $headers .= "Reply-To: $email\r\n";
    
    // Enviar correo
    if (mail($to, $subject, $body, $headers)) {
        // Redirigir al index.php
        header("Location: https://digitalservice.com.ar");
        exit();
    } else {
        echo '<p class="error-message">Hubo un problema al enviar el mensaje.</p>';
    }
}
?>
