window.onkeydown = function(e) {
    return !(e.keyCode == 32);
};

/*
  Handles a click on the down button to slide down the playlist.
*/
document.getElementsByClassName('down-header')[0].addEventListener('click', function(){
  var list = document.getElementById('list');

  list.style.height = ( parseInt( document.getElementById('flat-black-player-container').offsetHeight ) - 135 ) + 'px';

  document.getElementById('list-screen').classList.remove('slide-out-top');
  document.getElementById('list-screen').classList.add('slide-in-top');
  document.getElementById('list-screen').style.display = "block";
});

/*
  Handles a click on the up arrow to hide the list screen.
*/
document.getElementsByClassName('hide-playlist')[0].addEventListener('click', function(){
  document.getElementById('list-screen').classList.remove('slide-in-top');
  document.getElementById('list-screen').classList.add('slide-out-top');
  document.getElementById('list-screen').style.display = "none";
});

/*
  Handles a click on the song played progress bar.
*/
document.getElementById('song-played-progress').addEventListener('click', function( e ){
  var offset = this.getBoundingClientRect();
  var x = e.pageX - offset.left;

  Amplitude.setSongPlayedPercentage( ( parseFloat( x ) / parseFloat( this.offsetWidth) ) * 100 );
});

// document.querySelector('img[data-amplitude-song-info="cover_art_url"]').style.height = document.querySelector('img[data-amplitude-song-info="cover_art_url"]').offsetWidth + 'px';

$("#generate-playlist").click(function(event){
  var day = '' + $('input[name="day"]').val();
  // "http://localhost:8000/ten-lists/api/v1.0/mp3s?&day=1&format=json";
  var tenListsAPI = tenlists_base_url + "?&day=" + day + "&format=json";
  $.getJSON(tenListsAPI, function(data){
      generated_songs = data.mp3s;
      // console.log(generated_songs);

      $.each(generated_songs, function(index, value) {
        // $.each(this, function(name, value) {
        //   console.log(`${index + 1} ${name} = ${value}`);
        // });
        // console.log(`<p>index ${index} is ${value.name}</p>`);
        var playlist_entry = `<div class="song amplitude-song-container amplitude-play-pause" data-amplitude-song-index="${index}"> <span class="song-number-now-playing"> <span class="number">${index + 1}</span> <img class="now-playing" src="static/img/now-playing.svg"/> </span> <div class="song-meta-container"> <span class="song-name" data-amplitude-song-info="name" data-amplitude-song-index="${index}"></span> <span class="song-artist-album"><span data-amplitude-song-info="artist" data-amplitude-song-index="${index}"></span> - <span data-amplitude-song-info="album" data-amplitude-song-index="${index}"></span></span> </div> <span class="song-duration"> ${value.duration} <span> </div>`;
        $( "#list" ).append( playlist_entry );
      });

      Amplitude.init({
        "bindings": {
          37: 'prev',
          39: 'next',
          32: 'play_pause'
        },
        "songs": generated_songs
      });
  });

  $('#flat-black-player-container').show();
  $('.day-chooser').remove();
  $( "#starting-point" ).show();
});
