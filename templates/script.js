// script.js
document.addEventListener("DOMContentLoaded", function () {
    fetch("/templates/courses.html")
        .then(response => response.text())
        .then(data => {
            document.getElementById("course-placeholder").innerHTML = data;
        })
        .catch(error => {
            console.error("Error loading course content:", error);
        });
});
