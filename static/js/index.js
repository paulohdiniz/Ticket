///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function atualizarConteudoDaDiv() {
    var divConteudo2 = document.getElementById("conteudohora");
    var agora = new Date();
    var hora = agora.getHours().toString().padStart(2, '0');
    var minuto = agora.getMinutes().toString().padStart(2, '0');
    var seg = agora.getSeconds().toString().padStart(2, '0');
    var horaMinuto = hora + ":" + minuto + ":" + seg;
    divConteudo2.textContent = horaMinuto.toLocaleString();

    var divConteudo = document.getElementById("conteudodata");
    var dia = agora.getDate().toString().padStart(2, '0');
    var mes = (agora.getMonth() + 1).toString().padStart(2, '0'); // Note que o mês começa em 0 (janeiro) e termina em 11 (dezembro)
    var ano = agora.getFullYear();
    var dataFormatada = dia + "/" + mes + "/" + ano;
    divConteudo.textContent = dataFormatada.toLocaleString();
}
atualizarConteudoDaDiv();
setInterval(atualizarConteudoDaDiv, 1000); // 1segundo

function toggleAba(abaId) {
    var conteudo = document.getElementById(abaId);
    if (conteudo.style.display === "none" || conteudo.style.display === "") conteudo.style.display = "block";
    else  conteudo.style.display = "none";
} 
function toggleAbao(abaId) {
    var conteudo = document.getElementById(abaId);
    if (conteudo.style.display === "block" || conteudo.style.display === "") conteudo.style.display = "none";
    else  conteudo.style.display = "block";
} 

function openmodal1(){
    modal1.classList.remove("hidden");
    overlay.classList.remove("hidden");
    document.getElementById('menus').style.display = "none";
}

var temp4 = 1;
function closemodal1() {
    modal1.classList.add("hidden");
    overlay.classList.add("hidden");
    mensagem.classList.add("hidden");
    temp4 = 1;
}

function openmodalagendamento(index){
    modalagendamento.classList.remove("hidden");
    overlay.classList.remove("hidden");
    document.getElementById('menus').style.display = "none";
}

var temp40 = 1;
function closemodalagendamento(index) {
    modalagendamento.classList.add("hidden");
    overlay.classList.add("hidden");
    temp40 = 1;
}
