let userLists = JSON.parse(document.getElementById('shopLists').textContent);
let userLists_names = []
for (i in userLists) {
    userLists_names.push(userLists[i]['name'])
}

const elementNameOfCurrentList = document.getElementById("list-name");
let nameOfCurrentList = elementNameOfCurrentList.textContent

elementNameOfCurrentList.addEventListener("input", (e) => {
    editedNOCL = elementNameOfCurrentList.textContent
    if (userLists_names.includes(editedNOCL) && !(editedNOCL === nameOfCurrentList)) {
            elementNameOfCurrentList.style.color = "Red";
    }
    else {
        elementNameOfCurrentList.style.color = "Black";
    }
    
})

elementNameOfCurrentList.addEventListener("focusout", (e) => {
    editedNOCL = elementNameOfCurrentList.textContent
    if (userLists_names.includes(editedNOCL) && !(editedNOCL === nameOfCurrentList)) {
        console.log("Impossible to change list name : Already used.")
        elementNameOfCurrentList.textContent = nameOfCurrentList;
        elementNameOfCurrentList.style.color = "Black";
    }

    else {
        const myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");
        myHeaders.append("X-CSRFToken", getCookie('csrftoken'));

        const response = fetch("changeshoppinglistname/", {
            method: "POST",
            body: JSON.stringify({ name: editedNOCL}),
            headers: myHeaders,
        });
        nameOfCurrentList = editedNOCL
    }

})




const clickables = document.querySelectorAll(".clicker");

clickables.forEach(
    function (c) {
        c.addEventListener("click", function (e) {
            promise = fetch("", {
                method: 'POST',
                body: JSON.stringify({
                    clicked_id: c.id
                }),
                headers: {
                    "X-CSRFToken": getCookie('csrftoken'),
                }
                
            })
            promise.then((value) => {
                clickedElement = document.getElementById(value.headers.get("clicked_id"));
                
            })
        })
    }
)

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}