    $(".rounded-corners").corner();
    $(".rounded-top").corner("top");
    $(".rounded-bottom").corner("bottom");

    $("#set-focus").focus();
    $("#logo").hover(function() {
        $(this).attr('src', "{{ MEDIA_URL }}/images/tratten-logo-hover.png");
      }, function() {
        $(this).attr('src', "{{ MEDIA_URL }}/images/tratten-logo.png");
    });
    $("#small-logo").hover(function() {
        $(this).attr('src', "{{ MEDIA_URL }}/images/tratten-logo-small-hover.png");
      }, function() {
        $(this).attr('src', "{{ MEDIA_URL }}/images/tratten-logo-small.png");
    });
