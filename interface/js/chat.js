const bouton = document.getElementById("envoyer");

bouton.addEventListener("click", async () => {

    // Pour le style :
    const chat_container = document.getElementById("chat-container");
    const response_container = document.getElementById("reponse");
    response_container.removeAttribute('class', 'responded');
    chat_container.setAttribute('class', 'sent');
    response_container.setAttribute('class', 'waiting');

    const texte = document.getElementById("message").value;

    const resultat = await fetch("/pal/chat", { //await = attendre réponse serveur
        method: "POST",
        headers: {
            "Content-Type": "text/plain" //format des données (Content-Type = header (entete) http qui indique le type de contenu envoyé)
        },
        body: texte
    });

    // -------------------------------------------------------------

    const donnees = await resultat.json(); //await = attendre réponse serveur ; resultat.json() = convertir la réponse en JSON

    // Pour le style (p2) :
    response_container.removeAttribute('class', 'waiting');
    response_container.setAttribute('class', 'responded');

    document.getElementById("reponse").textContent = donnees.message; //afficher la réponse du serveur (ligne message du json) dans l'élément HTML avec l'id "reponse"
});