// meu-script.js

// Configurar URLs como variáveis JavaScript
var testPageUrl = '/test';
var laterPageUrl = '/goodbye';

document.getElementById('test-here').addEventListener('click', function() {
  window.location.href = testPageUrl;
});

document.getElementById('later').addEventListener('click', function() {
  window.location.href = laterPageUrl;
});
