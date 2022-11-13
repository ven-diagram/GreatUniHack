var w = 400,
h = 400,
p = 7,
q = 7;
count=1;
var img, cv, ctx;

function myFunction() {
    var x = document.getElementById("myText").value;
    document.getElementById("demo").innerHTML = x;
    if (x=="kitten"){
        text1="You got it in ";
        text2= count;
        text3= " guesses!";
        let result = text1.concat(text2).concat(text3);
        window.alert(result);
        leaderboard();

    }
    else{
        if (p >= 200) {
            return;
        }


        p=p * 1.1**p;
        q = q * 1.1**q;
        count++;

        if (p > 200) {
            p = 200;
            q = 200;
            let string1="You ran out of guesses it's a kitten";
            window.alert(string1);
            leaderboard();


        }
        drawImage();

    }
}

function init() {
    img = new Image();
    img.onload = drawImage;
    img.src = "kitten.png"
}
function drawImage() {

    cv =  document.getElementById('cv');
    ctx = cv.getContext("2d");

    cv.width = p;  // set canvas resolution
    cv.height = q;

    ctx.drawImage(img, 0, 0, p, q); // draw image with given resolution

    cv.style.width = w + "px";  // enlarge canvas by stretching
    cv.style.height = h + "px";



}

function leaderboard(){
    window.location.href="leaderboard.html";




}

init();


