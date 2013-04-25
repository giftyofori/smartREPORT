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
   setTimeout(function (){if (xhr.readyState===4) {pbardone();}},3000);
   document.getElementById("sarts-btn").innerHTML="";
   console.log(xhr.readyState);
}

//function to activate progressbar
function pbar() {
    var bar = document.getElementById("progress-info-sarts");
    bar.style.visibility ="visible";
    bar.style.backgroundColor="#d6e9f8;";
    var p = document.createElement("p");
    p.setAttribute('class','progressbar');
    p.setAttribute('id','progressbar');
    p.style.fontSize ="11px";
    p.innerText = "Sending All Reports"
    bar.appendChild(p);
    
    
}

function pbardone() {
    p = document.getElementById("progressbar");
    p.innerText = "All Reports Has Been Sent";
    document.r
    
}
