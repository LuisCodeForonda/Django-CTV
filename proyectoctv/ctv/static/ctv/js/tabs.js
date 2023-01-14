/*

const tabs = document.querySelectorAll("#tab");
const contents = document.querySelectorAll("#tab-content");

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
});*/