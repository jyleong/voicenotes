
function toggleThinking(){
  cleanHeartClasses();
  $('.heart').first().css('animation', 'rippleYellow 0.7s linear infinite');
  $("div.heart").first().addClass("heartThinking");
  //$('#heart').css('background-color', 'yellow');
}
function toggleListening(){
  cleanHeartClasses();
  $('.heart').first().css('animation', 'rippleGreen 0.7s linear infinite');
  $("div.heart").first().addClass("heartListening");
  //$('#heart').css('background-color', 'rgba(101, 255, 120, 0.8)');
}
function toggleSpeaking(){
  cleanHeartClasses();
  $('.heart').first().css('animation', 'rippleRed 0.7s linear infinite');

  $("div.heart").first().addClass("heartSpeaking");
  //$('#heart').css('background-color', 'red');
}
function toggleStandby(){
  cleanHeartClasses();
  $('.heart').first().css('animation', 'None');
  $("div.heart").first().addClass("heartStandby");
  //$('#heart').css('background-color', 'rgba(128,128,128,1)');
}
function cleanHeartClasses(){
  $("div.heart").first().removeClass("heartStandby");
  $("div.heart").first().removeClass("heartSpeaking");
  $("div.heart").first().removeClass("heartThinking");
  $("div.heart").first().removeClass("heartListening");
  $("div.heart").first().removeClass("animation");
}

toggleSpeaking();

//$("div.heart").css(background-color, "black");
