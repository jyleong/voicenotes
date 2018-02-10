
function toggleThinking(){
  $('#heart').css('animation', 'rippleYellow 0.7s linear infinite');
  $('#heart').css('background-color', 'yellow');
}
function toggleListening(){
  $('#heart').css('animation', 'rippleGreen 0.7s linear infinite');
  $('#heart').css('background-color', 'rgba(101, 255, 120, 0.8)');
}
function toggleSpeaking(){
  $('#heart').css('animation', 'rippleRed 0.7s linear infinite');
  $('#heart').css('background-color', 'red');
}
function toggleStandby(){
  $('#heart').css('animation', 'None');
  $('#heart').css('background-color', 'rgba(128,128,128,1)');
}
