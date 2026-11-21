
// 1. Récupérer l'heure actuelle
const heuree = new Date().getHours();

// 2. Définir les questions par plage horaire
const questions = {
  matin: [
    "Que faisons-nous ce matin ?",
    "Une idée pour aujourd'hui ?",
    "Par quoi commence-t-on ce matin ?",
    "Quel est le programme ?",
    "Qu'avons-nous de prévu aujourd'hui ?"
  ],

  apresMidi: [
    "Que faisons-nous cet après-midi ?",
    "Que pourrions-nous faire ?",
    "Un nouveau projet en tête ?",
    "On s'occupe de quoi aujourd'hui ?"
  ],

  soir: [
    "De quoi avez-vous envie ce soir ?",
    "Une journée bien remplie ?",
    "Prêt à vous détendre un peu ?",
    "Comment puis-je vous aider ce soir ?",
    "On se pose un peu ?",
    "Quel est le programme pour ce soir ?"
  ],

  nuit: [
    "Encore debout ?",
    "Une idée derrière la tête ?",
    "Par quoi souhaitez-vous commencer ?",
    "Je vous écoute.",
    "Inspiré ?",
    "Que puis-je faire pour vous ?",
    "La nuit porte conseil, paraît-il..."
  ]
};

// 3. Sélectionner la plage horaire
let listeQuestions = [];

if (heuree >= 5 && heuree < 12) {
  listeQuestions = questions.matin;
} else if (heuree >= 12 && heuree < 18) {
  listeQuestions = questions.apresMidi;
} else if (heuree >= 18 && heuree < 22) {
  listeQuestions = questions.soir;
} else {
  listeQuestions = questions.nuit;
}

// 4. Choisir une question aléatoire
const index = Math.floor(Math.random() * listeQuestions.length);
const daytask = listeQuestions[index];

// 5. Afficher le message
document.getElementById("question").textContent = daytask;
