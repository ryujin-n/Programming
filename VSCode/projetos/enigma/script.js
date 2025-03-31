const characterName = document.getElementById("characterName");
const dialogueText = document.getElementById("dialogueText");
const dialogueBox = document.getElementById("dialogueBox");
const nextButton = document.getElementById("nextButton");
const startButton = document.getElementById("startButton");
const finishButton = document.getElementById("finishButton");
const tarot = document.getElementById("tarot");
const fundo = document.getElementById("fundod");
var backgroundAudio = document.getElementById("background-audio");
var stage = "";
const slide = document.querySelector('.slide');
const cards = document.querySelectorAll("#card, #card2, #card3");
const card1 = document.getElementById("card"); 
const card2 = document.getElementById("card2");
const card3 = document.getElementById("card3");
const cardss = document.querySelectorAll('.flip-card');
const video = document.getElementById("video")
const nome = document.getElementById("nome")
const send = document.getElementById("send")
let nomeT = ""
var resp = window.matchMedia("(max-height: 900px)")

video.pause();

cardss.forEach(card => {
    card.addEventListener('click', function() {
        const cardInner = card.querySelector('.flip-card-inner');
        cardInner.classList.add('rotated');
    });
});

slide.classList.add('slide');

var typeSound = new Howl({
  src: ['src/oracle.wav'], 
  volume: 0.4, 
});

backgroundAudio.volume = 0.1;


const introd = [
  { name: "???", text: "Olá...viajante" },
  { name: "???", text: "Vejo uma alma curiosa...mas sem nome..." },
  { name: "???", text: "Aqueles que me encontram...me chamam de Oráculo"},
  { name: "Oráculo", text: "Qual o seu nome?"},
]

const dialogues = [
  { name: "Oráculo", text: ""},
  { name: "Oráculo", text: "Muitas eras vieram e se foram, mas eu permaneço... fadado a guiar viajantes... como você...ao futuro deles." },
  { name: "Oráculo", text: "Há segredos que os olhos não podem ver… Mas os mais atentos sempre encontram um caminho." },
  { name: "Oráculo", text: "Esses segredos... eu não poderei te guiar até suas respostas..." },
  { name: "Oráculo", text: "Terá de descobrir por conta própria... mas há algo que eu possa fazer por você" },
  { name: "Oráculo", text: "Poderei ler seu futuro..." },
  { name: "Oráculo", text: "Vamos começar...?" },
];

const dialogues2 = [
  { name: "Oráculo", text: "Aqui, diante de você, estão três cartas viradas, seus significados ocultos, aguardando o momento certo para serem revelados." },
  { name: "Oráculo", text: "Vire a primeira carta." },
];

const dialogues3 = [
  { name: "Oráculo", text: "A Torre..." },
  { name: "Oráculo", text: "Uma imagem de caos, destruição e revelações súbitas." },
  { name: "Oráculo", text: "Esta carta fala sobre rupturas, sobre a queda de estruturas que já não servem mais ao propósito do seu ser." },
  { name: "Oráculo", text: "Algo foi quebrado, algo que parecia sólido e seguro." },
  { name: "Oráculo", text: "Pode ser uma verdade que precisa ser enfrentada, ou uma grande transformação que não pode mais ser evitada." },
  { name: "Oráculo", text: "O que será que a Torre trouxe para você, querido viajante? O que está prestes a cair?" },
  { name: "Oráculo", text: "Agora, vire a segunda carta." },
];

const dialogues4 = [
  { name: "Oráculo", text: "O Julgamento... " },
  { name: "Oráculo", text: "O som de um trompete ressoa, chamando para a reflexão e para o renascimento." },
  { name: "Oráculo", text: "Este é o momento de um novo começo, mas também de julgamento sobre os caminhos tomados até agora." },
  { name: "Oráculo", text: "O passado clama por resolução...e a alma busca evolução. " },
  { name: "Oráculo", text: "O que você fará com essa segunda chance que está diante de você?" },
  { name: "Oráculo", text: "Agora, a última carta. Vire-a com cuidado." },
];
const dialogues5 = [
  { name: "Oráculo", text: "A Lua..." },
  { name: "Oráculo", text: "o véu que esconde o desconhecido. Este é o caminho dos mistérios, onde cada passo é envolto em sombras." },
  { name: "Oráculo", text: "Esta carta fala dos enganos que nos cercam, da confusão que pode ofuscar nossa visão. " },
  { name: "Oráculo", text: "A Lua também traz uma advertência: nem tudo o que reluz é ouro" },
  { name: "Oráculo", text: "O caminho à frente pode ser sinuoso e nebuloso, mas é preciso confiar na intuição, deixar-se guiar pela luz suave que vem de dentro." },
  { name: "Oráculo", text: "O que a Lua esconde para você?"},
  { name: "Oráculo", text: "Ou melhor..."},
  { name: "Oráculo", text: "Do que ela te protege?"},
];
const sry = [
  { name: "???", text: "O que...?" },
  { name: "???", text: "..." },
  { name: "Nyra", text: "Desculpar...?" },
  { name: "Nyra", text: "Eu tentei, pai... " },
  { name: "Nyra", text: "Tentei encontrar uma razão para perdoar você. Para acreditar que, de alguma forma, o que fez tinha um propósito. " },
  { name: "Nyra", text: "Mas toda vez que fecho os olhos, tudo o que vejo são cinzas..." },
  { name: "Nyra", text: "Cinzas da nossa casa, da nossa família… do que um dia fomos..." },
  { name: "Nyra", text: "Você jurou nos proteger." },
  { name: "Nyra", text: "Mas no fim, foi você quem nos destruiu." },
  { name: "Nyra", text: "Não foram os inimigos, não foi a guerra… foi você." },
  { name: "Nyra", text: "Suas escolhas, sua sede de algo maior do que nós." },
  { name: "Nyra", text: "Você nos sacrificou por um ideal que nem sei se era real." },
  { name: "Nyra", text: "Então não, eu não posso te perdoar." },
  { name: "Nyra", text: "Porque perdão não apaga o vazio que você deixou..." },
];

var typingSpeed = 40; // 
let currentDialogueIndex = 0;
let currentDialogues = introd;
let interromperDialogo = false;


function moveDialogueBox() {
    dialogueBox.style.transition = "transform 1s ease"; 
    if (resp.matches) {
      dialogueBox.style.bottom = "25.2rem"; 
      dialogueBox.style.transform = "translateY(23.5rem)"; 
      dialogueBox.style.zIndex = "1";
    }
    else{
      dialogueBox.style.transform = "translateY(23.5rem)"; 
      dialogueBox.style.zIndex = "1";
    }
  }
function resetDialogueBox() {
    dialogueBox.style.transition = "transform 1s ease"; 
    dialogueBox.style.bottom = ""; 
    dialogueBox.style.transform = "translateY(0rem)"; 
    dialogueBox.style.zIndex = "1";
  }

function hideCards() {
  card1.classList.add("hide");
  card2.classList.add("hide");
  card3.classList.add("hide");

  setTimeout(() => {
      document.getElementById("card").style.display = "none";
      document.getElementById("card2").style.display = "none";
      document.getElementById("card3").style.display = "none";
  }, 1000); 
}

  function playDialogue() {

    if (interromperDialogo){
      backgroundAudio.pause()
      return
    }

    backgroundAudio.play()
    dialogueBox.style.display = "block";
    startButton.style.display = "none";  
    typeDialogue();
  }
  
function cartas(dialogo) {

  if (dialogo === "Vire a primeira carta.") {
    console.log("01010011 01000001 01000011 01010010 01001001 01000110 01001001 01000011 01001001 01001111 ");
    card1.style.pointerEvents = "auto";
  }
  if (dialogo === "Agora, vire a segunda carta.") {
    console.log("01010010 01000101 01001110 01010101 01001110 01000011 01001001 01000001 ")
    card2.style.pointerEvents = "auto";
  }
  if (dialogo === "Agora, a última carta. Vire-a com cuidado.") {
    console.log("01010011 01001111 01000110 01010010 01001001 01001101 01000101 01001110 01010100 01001111 ")
    card3.style.pointerEvents = "auto";
  }
  if (dialogo === "O caminho à frente pode ser sinuoso e nebuloso, mas é preciso confiar na intuição, deixar-se guiar pela luz suave que vem de dentro.") {
    console.log("00101101 00101110 00101110 00100000 00101101 00101110 00101110 00101101 00100000 00101101 00101101 00101110 00100000 00101110 00101110 00101101 00100000 00101110 00101110 00101110 00101110 00100000 00101101 00101110 00101110 00101110 ")
    hideCards();
    resetDialogueBox();
  }
  if (dialogo === "Ou melhor...") {
    typingSpeed = 200;
    dialogueBox.style.transition = "max-width 1s ease"; 
    dialogueBox.style.maxWidth = "340px";
    backgroundAudio.pause(); 
  }
  if (dialogo === "Do que ela te protege?") {
    dialogueBox.style.display = "none";
    video.style.display = "block";
    fundo.src=""
    video.play();
  }
  if (dialogo === "O que...?" ) {
    typingSpeed = 200; 
    backgroundAudio.pause(); 
  }
  if (dialogo === "..." ) {
    typingSpeed = 40; 
  }
  if (dialogo === "Desculpar...?" ) {
    backgroundAudio.src="src/audio2.mp3"
    backgroundAudio.load();  
    backgroundAudio.play(); 
  }

  if (dialogo === "Qual o seu nome?") {
    dialogueBox.style.transition = "transform 1s ease"; 
    dialogueBox.style.transform = "translateY(-3rem)";
    nome.style.display = "block";
    send.style.display = "block";

    send.onclick = function () {
        let nomeD = nome.value.trim();
        if (nomeD === "") return;
        else if (nomeD.toUpperCase().trim() === "AUDREY") {

      }
        else if (nomeD.toUpperCase().trim() === "ENFORCADO" || nomeD.toUpperCase().trim() === "O ENFORCADO" || nomeD.toUpperCase().trim() === "HANGED MAN"|| nomeD.toUpperCase().trim() === "HANGEDMAN"|| nomeD.toUpperCase().trim() === "OENFORCADO") {
          interromperDialogo = true
          dialogueBox.style.display="none"
          nome.style.display="none"
          send.style.display="none"
          fundo.style.display = "none"

          let video = document.createElement("video");
          video.src = "src/fim.mp4"; 
          video.autoplay = true;
          video.loop = false;
          video.controls = false;
          video.style.position = "fixed";
          video.style.width = "100vw";
          video.style.height = "100vh";
      
          document.body.appendChild(video);

          video.addEventListener('ended', function() {
            video.style.display = "none";
          });
      }
      if (nomeD.toUpperCase().trim() === "MALDI") {

        dialogueBox.style.transition = "max-width 1s ease"; 
        dialogueBox.style.maxWidth = "600px";
        characterName.style.fontFamily = "Bachroque, sans-serif"
        dialogueText.style.fontFamily = " Flink, sans-serif"
        nome.style.display = "none";
        send.style.display = "none";
        dialogueBox.style.transform = "translateY(0rem)";
    
        if (typeSound) {
            typeSound.stop();  
            typeSound.unload(); 
        }
    
        typeSound = new Howl({
            src: ['src/oracle2.mp3'],
            volume: 0.4,
        });
    
        currentDialogues = sry;
        currentDialogueIndex = 0;
        playDialogue();

    }
    else{
      nomeT = nomeD.charAt(0).toUpperCase() + nomeD.slice(1).toLowerCase();

      dialogues[0].text = "Um prazer te conhecer..." + nomeT + ".";

      hideform();

      currentDialogues = dialogues;
      currentDialogueIndex = 0;

      dialogueBox.style.transform = "translateY(0rem)";
      playDialogue();
    }
    };
    return; 
  }
}

function hideform() {
  nome.classList.add("hide");
  send.classList.add("hide");

  setTimeout(() => {
      nome.style.display = "none";
      send.style.display = "none";
  }, 1000); 
}

function typeDialogue() {
  if (currentDialogueIndex >= currentDialogues.length) {
    if (currentDialogues === dialogues) {
      nextButton.style.display = "block";  
    } else {
      nextButton.style.display = "none"; 
    }
    return;
  }
      
  const { name, text } = currentDialogues[currentDialogueIndex];
  characterName.textContent = name;
  dialogueText.textContent = "";

  let index = 0;
  let speed = typingSpeed; 

  function typeNextChar() {

      if (index < text.length) {
          dialogueText.textContent += text.charAt(index);

          if (!typeSound.playing()) {
              typeSound.play();
          }

          index++;
          setTimeout(typeNextChar, speed); 
      } else {
          typeSound.stop();
          cartas(text);

          currentDialogueIndex++;
          setTimeout(typeDialogue, 1000);  
      }
  }

  typeNextChar();
}

startButton.addEventListener("click",playDialogue);
  
function pointers() {
  card1.style.pointerEvents = "none";
  card2.style.pointerEvents = "none";
  card3.style.pointerEvents = "none";
}
  
function nextbto() {
  pointers();
  nextButton.style.display = "none"
  dialogueBox.style.display = "none"; 

  tarot.style.display = "flex";
  fundo.style.transition = "filter 1s ease";
  fundo.style.filter = "blur(0.3rem)";
  
  moveDialogueBox();
  
  currentDialogues = dialogues2;
  currentDialogueIndex = 0;
  playDialogue(); 
}

function tower() {
  if (card1.classList.contains("flip")) {
      card1.addEventListener(
          "transitionend",
          () => {
              setTimeout(() => { 
                  currentDialogues = dialogues3;
                  currentDialogueIndex = 0; 
                  playDialogue();
              }, 900); 
          },
          { once: true } 
      );
  }
}

function judge() {
  if (card2.classList.contains("flip")) {
      card2.addEventListener(
          "transitionend",
          () => {
              setTimeout(() => {
                  currentDialogues = dialogues4;
                  currentDialogueIndex = 0; 
                  playDialogue();
              }, 900);
          },
          { once: true } 
      );
  }
}

function moon() {
  if (card3.classList.contains("flip")) {
      card3.addEventListener(
          "transitionend",
          () => {
              setTimeout(() => {
                  currentDialogues = dialogues5;
                  currentDialogueIndex = 0; 
                  playDialogue();
              }, 900);
          },
          { once: true } 
      );
  }
}

card1.addEventListener("click", () => {
  card1.classList.add("flip");
  tower(); 
  card1.style.pointerEvents = "none"; 

});

card2.addEventListener("click", () => {
  card2.classList.add("flip");
  judge(); 
  card2.style.pointerEvents = "none"; 

});

card3.addEventListener("click", () => {
  card3.classList.add("flip");
  moon(); 
  card3.style.pointerEvents = "none"; 
});


  