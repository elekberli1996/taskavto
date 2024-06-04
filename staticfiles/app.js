element=document.getElementById("message");
console.log(element)

if (element !== null){
    
    setTimeout(() => {
        element.style.display="none";
        console.log(element)
        
    }, 3000);

}