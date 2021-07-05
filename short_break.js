window.onload = function() {
  let seconds = 60;
  let minutes = 5;

  setInterval(function() {
    document.querySelector('.minute').innerText = minutes;
    document.querySelector('.second').innerText = seconds;

    seconds -= 1;
    if (seconds == 00) {
      minutes -= 1;
      seconds = 60;
      if (minutes == 0) {
        document.querySelector('.countdown').innerHTML = 'EXPIRED!';
      }
    }
  }, 1000); 
};
