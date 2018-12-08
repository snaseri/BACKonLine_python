// Slider for Q20.
// Load values from input HTML and convert to object.
var sliderJSON = $("#range-slider-input").attr("values"),
    sliderObject = JSON.parse(sliderJSON);

// Cycle through object and create ticks.
for (var propt in sliderObject) {
  $("#ticklist").append("<div class='range-slider-ticks-dots'><span class='range-slider-ticks-label' slider-value='" + propt + "'>" + propt + "</span></div>");
};

// Get the initial value of the slider and mark the tick label as bold.
$("span[slider-value='" + $("#range-slider-input").val() + "']").addClass("is-selected");

// Detect any change of the slider and bold the relevant tick label.
$("#range-slider-input").change(function() {
  $("span.range-slider-ticks-label").removeClass("is-selected");
  $("span[slider-value='" + $(this).val() + "']").addClass("is-selected");
});

// Add click event to labels and apply the `is-selected` styling.
$(".range-slider-ticks-label").click(function() {
  $("span.range-slider-ticks-label").removeClass("is-selected");
  $(this).addClass("is-selected");
  $("#range-slider-input").val(parseInt($(this).attr("slider-value")));
});

// Green text for 'tick all' type questions.
$('h1').each(function() {
  var ques = $(this).text();
  if (ques.indexOf('Please tick all options that apply') >= 0) {
    ques = ques.replace("Please tick all options that apply","<span style='color: #00b050;'>Please tick <strong>all</strong> options that apply</span>");
    $(this).html(ques);
  } else if (ques.indexOf('Please tick all body areas that apply') >= 0) {
    ques = ques.replace("Please tick all body areas that apply","<span style='color: #00b050;'>Please tick <strong>all</strong> body areas that apply</span>");
    $(this).html(ques);
  };
});

// For skipping questions if certain questions are answered.


// Code for back and next button.
// function back() {
//   console.log("Back button");
//   var direction = document.getElementById("direction").value;
//   document.getElementById("direction").value = "back"
//   var calculation = document.getElementById("questnum").value;
//   var counter = document.getElementById("counter").innerHTML;
//   console.log(direction);
//   if (counter == calculation && counter != 1 ) {
//     document.getElementById("questnum").value -= 1
//   }
//   if (calculation-counter == 1) {
//     document.getElementById("questnum").value = calculation - 2;
//   }
// };
//
// function forward() {
//   console.log("Next button");
//   var direction = document.getElementById("direction").value;
//   document.getElementById("direction").value = "forward";
//   var calculation = parseInt(document.getElementById("questnum").value);
//   var counter = document.getElementById("counter").innerHTML;
//   console.log("Next button");
//   var direction = document.getElementById("direction").value;
//   document.getElementById("direction").value = "forward";
//   var calculation = parseInt(document.getElementById("questnum").value);
//   var counter = document.getElementById("counter").innerHTML;
//   if (counter == calculation) {
//     document.getElementById("questnum").value = calculation + 1;
//   };
//   if (counter-calculation == 1) {
//     document.getElementById("questnum").value = calculation + 2;
//   };
//   console.log(direction);
// };

// Make sure user has selected at least one option.
function validate() {
  var valid = document.getElementsByName("option-text[]");
  var hasChecked = false;
  for (var i = 0; i < valid.length; i++) {
    if (valid[i].checked) {
      hasChecked = true;
      break;
    };
  };
  if (hasChecked == false) {
    alert("Please select at least one option");
    return false;
  };
  return true;
};

// Disable other checkboxes if certain option is selected.
// Array of hard coded values.
disableOptions = ["I don't take any medication for my back pain", "I am unable to ease my back pain", "Any activity that I do for a long period of time increases my back pain", "Everything I do causes me pain", "Nothing I do stops my pain", "Nothing helped"];
// Add click event to each option.
$(".options").click(function() {
  // Store option text.
  option = $(this).find("label").text();
  // Create boolean.
  found = false;
  // Cycle through the array.
  disableOptions.forEach(function(value, index) {
    // Check if chosen option equals current element in array.
    if (option == value) {
      // Mark the found boolean as true.
      found = true;
    };
  });
  // Check if entry matched a value in the array.
  if (found == true) {
    // Check if the box has been checked.
    if ($(this).find("input").prop("checked") == true) {
      // Disable the options for this question and uncheck.
      $(this).parent().find(".options input").prop({'disabled': true, 'checked': false});
      // Re-enable the checkbox and mark it checked.
      $(this).find("input").prop({'disabled': false, 'checked': true});
    } else {
      // Re-enable all checkboxes.
      $(this).parent().find(".options input").prop('disabled', false);
    };
  };
});

// Get the patient ID from local storage.
function onLoad() {
  patient_id = localStorage.getItem("PatientID");
  document.getElementById("patient_id").value = patient_id;
};

function sendRadio(value) {
  option = value.innerHTML.split('<')[0];
  document.getElementById("radio").value = option;
};

function sendCheckbox(value) {
  if (value.checked == true) {
    if ((document.getElementById("counter").innerHTML == 5 && value.id.substring(12) == 16 ) || (document.getElementById("counter").innerHTML == 12 && value.id.substring(12) == 11 ) || (document.getElementById("counter").innerHTML == 14 && (value.id.substring(12) == 7 || value.id.substring(12) == 8) ) || (document.getElementById("counter").innerHTML == 15 && value.id.substring(12) == 8 ) || (document.getElementById("counter").innerHTML == 17 && value.id.substring(12) == 5 )) {
      document.getElementById("checkbox").value = "[]"
      document.getElementById("checkbox").value = document.getElementById("checkbox").value.substring(0, document.getElementById("checkbox").value.length-1) + value.id.substring(12) + "," + document.getElementById("checkbox").value[document.getElementById("checkbox").value.length - 1];
    } else {
      document.getElementById("checkbox").value = document.getElementById("checkbox").value.substring(0, document.getElementById("checkbox").value.length-1) + value.id.substring(12) + "," + document.getElementById("checkbox").value[document.getElementById("checkbox").value.length - 1];
    };
  } else {
      console.log("unchecked");
      console.log(value.id.substring(12));
      document.getElementById("checkbox").value = document.getElementById("checkbox").value.replace(value.id.substring(12) + ",", "");
    };
};

function sendTextArea(value) {
  document.getElementById("textarea").value = value.value;
};

// Make body map responsive.
$('#body-map').imageMapResize();

// Display body map.
$('#human-body').maphilight();

var currentColor = 'green';
// Object with colour swatches.
var fills = {
  green: {fillColor: '00ff00', strokeColor:'000000'},
  amber: {fillColor: 'ffbf00', strokeColor:'000000'},
  red:   {fillColor: 'ff0000', strokeColor:'000000'}
};

$('map area').click(function(e) {
  // Use swatch object to higlight.
  $('#human-body').maphilight(fills[currentColor]);
  // Switch out the colours.
  if (currentColor == 'green') {
    currentColor = 'amber';
  } else if (currentColor == 'amber') {
    currentColor = 'red';
  } else {
    currentColor ='green';
  };
});

// Make the clicked area selected.
$('map area').click(function(e) {
  e.preventDefault();
  // Remember clicked area.
  var clickedArea = $(this);
  // For each area...
  $('map area').each(function() {
    // get
    hData = $(this).data('maphilight') || {};
    // modify
    hData.alwaysOn = $(this).is(clickedArea);
    // set
    $(this).data('maphilight', hData ).trigger('alwaysOn.maphilight');
  });
});

function displayPart(id) {
  // Convert the body part ID to sentence case.
  id = id.toLowerCase().replace(/(^|\s)[a-z]/g, function(id) {
    return id.toUpperCase();
  });
  // Replace the dashes with spaces.
  id = id.replace(/-/g, ' ');
  // Initialise pain level.
  var painLevel = ''
  // Set pain level depending on colour selected.
  if (currentColor == 'green') {
    painLevel = ' LOW PAIN';
  } else if (currentColor == 'amber') {
    painLevel = ' MEDIUM PAIN';
  } else {
    painLevel = ' HIGH PAIN';
  };
  // Set the value of the input `selected-body-part` to the body part and pain level.
  $('#selected-body-part').val(id + painLevel);
};

// References:
// https://stackoverflow.com/questions/53499666/change-styling-of-a-certain-part-in-h1-tag-when-in-jinja-template
// https://stackoverflow.com/questions/53622707/change-colour-of-map-area-on-click
