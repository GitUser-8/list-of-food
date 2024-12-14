const clickables = document.querySelectorAll(".clicker");

clickables.forEach(
    function (c) {
    c.addEventListener("click", function (e) {
        response = fetch("", {
            method: "POST",
        }
        )
        document.getElementById("item").innerHTML = response
    }) 
    }
)