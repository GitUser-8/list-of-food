const clickables = document.querySelectorAll(".clicker");



clickables.forEach(
    function (c) {
        c.addEventListener("click", function (e) {
            tr_response = fetch("", {
                method: 'POST',
                body: JSON.stringify({
                    id: 142
                }),
                headers: {
                    "X-CSRFToken": getCookie('csrftoken'),
                }
                
            })
            var_try = tr_response
            document.getElementById("test").innerHTML = var_try
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