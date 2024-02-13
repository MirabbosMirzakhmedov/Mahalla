// JavaScript
document.addEventListener("DOMContentLoaded", function() {
    var alert = document.getElementById('myAlert');
    var closeButton = document.getElementById('closeButton');

    // Close the alert by pressing the button
    closeButton.addEventListener('click', function() {
        alert.style.display = 'none';
    });

    // Set a timer to close the alert automatically after 5 seconds (5000 milliseconds)
    var autoCloseTimer = setTimeout(function() {
        alert.style.display = 'none';
    }, 5000);
});