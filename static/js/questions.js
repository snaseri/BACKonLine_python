// Slider for Q20
var rangeSlider = function() {
  var slider = $('.range-slider');
  var range = $('.range-slider-range');
  var value = $('.range-slider-value');
    
  slider.each(function() {
    value.each(function() {
      var value = $(this).prev().attr('value');
      $(this).html(value);
    });

    range.on('input', function() {
      $(this).next(value).html(this.value);
    });
  });
};

rangeSlider();
