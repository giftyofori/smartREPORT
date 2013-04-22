function nextlink(){
    return document.getElementById('nextlink').innerHTML='<input type="submit" value="next" class="arwnext" />'//'<a href="/report/arw/stage2/">next</a>';
    //return alert("it works");
}

function percent(){
    return alert("cooliiiiiiiiiiii");
    //document.getElementById('percent').style.background="rgba(0,0,0,0)";    

}

function start_sarts(url) {
   var  xhr =  new XMLHttpRequest;
   xhr.open("GET",url,false);
   pbar();
   xhr.send();
   setTimeout(function (){if (xhr.readyState===4) {pbardone();}},1000);
   console.log(xhr.readyState);
}

//function to activate progressbar
function pbar() {
    bar = document.getElementById("progress-info-sarts");
    bar.innerHTML ="";
    bar.style.backgroundColor="inherit";
    bar.style.backgroundColor = "rgba(0,0,0,0.2)"
    //bar.style.border = "1px solid red";
    p = document.createElement("p");
    p.setAttribute('class','progressbar');
    p.setAttribute('id','progressbar');
    p.innerText = "Sending .............."
    bar.appendChild(p);
    console.log(bar);
    
    
}

function pbardone() {
    p = document.getElementById("progressbar");
    p.innerText = "Done"
    
}
