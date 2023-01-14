//variables del menu
const boton = document.querySelector('#btn-menu');
const menu = document.querySelector('#menu');
const menuitems = document.querySelectorAll("#menu-item");

//variables del slide
const slideprev = document.querySelector('#prev');
const slidenext = document.querySelector('#next');

//variables del los tabs
const tabs = document.querySelectorAll("#tab");
const contents = document.querySelectorAll("#tab-content");


//codigo del menu
boton.addEventListener('click', () => {
    menu.classList.toggle("hidden");
    boton.classList.toggle("bg-gray-300");
    boton.classList.toggle("text-gray-900");
});

//codigo de las opciones del menu
menuitems.forEach((menuitem, index) =>{
    menuitem.addEventListener("click", () =>{
        console.log("esta aqui")
       // menuitems.forEach((menuitem) => menuitem.classList.remove("border-b-2"));
        //menuitem.classList.add("border-b-2");
        console.log(index);
        menuitems[index].classList.add("boder-b-2");
    });
});

//codigo del slide
if (!(slideprev === null)) {
    
    console.log("esta el slide aqui");
    let slideIndex = 1;
    let contadorSlide = 0;

    showSlides(slideIndex);

    slideprev.addEventListener('click', () => {
        showSlides(slideIndex -= 1);
    });

    slidenext.addEventListener('click', () => {
        showSlides(slideIndex += 1);
    });


    function showSlides(n) {
        let i;
        let slides = [...document.querySelectorAll("#mySlides")];
        let dots = document.querySelectorAll("#dot");
        if (n > slides.length) { slideIndex = 1 }
        if (n < 1) { slideIndex = slides.length }
        for (i = 0; i < slides.length; i++) {
            slides[i].classList.add('hidden');
        }
        for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" bg-gray-800", "");
        }
        slides[slideIndex - 1].classList.remove("hidden");
        dots[slideIndex - 1].className += " bg-gray-800";
        contadorSlide = 0;
    }

    function currentSlide(n) {
        showSlides(slideIndex = n);
    }

    function autoSlide() {
        const actual = Number(document.querySelector('.bg-gray-800').dataset.id);
        n = actual + 1;
        currentSlide(n);
    }

    setInterval(contAutoSlide, 1000);

    function contAutoSlide() {
        if (contadorSlide == 4) {
            contadorSlide = 0;
            autoSlide();
        }
        contadorSlide += 1;
    }
}

//codigo de los tabs (pestañas)
if(!(tabs === null)){
    tabs.forEach((tab, index) =>{
        tab.addEventListener("click", () =>{
            //remover las clases activas
             
            tabs.forEach((tab) => tab.classList.remove("text-gray-200"));
            tabs.forEach((tab) => tab.classList.remove("bg-red-700"));
            
            tab.classList.add("text-gray-200");
            tab.classList.add("bg-red-700");
    
            //mostrar los contenedores
            contents.forEach((content) => content.classList.add("hidden"))
            contents[index].classList.remove("hidden");
            console.log(index);
        });
    });
}

/*
3 adaptadores display port a hdmi hembra
3 adaptadores vga hembra a hdmi macho*/