let currentDate = new Date();
currentDate.setTime(currentDate.getTime() + (1 * 60 * 60 * 1000));
let expirationDate = currentDate.toUTCString();
document.cookie = "connected=true; expires=" + expirationDate + "; path=/";

window.location.href = '/'