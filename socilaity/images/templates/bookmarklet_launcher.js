(function(){
    if (!window.sociality) {
        socilaity_js = document.body.appendChild(document.createElement("script"))
        sociality_js.src = "127.0.0.1:8000/static/js/sociality.js?r=" + Math.floor(Math.random() * 999999999999999999)
        window.sociality = true
    } else {
        socialityLaunch()
    }
})()
