// Slider for Q20.
if (document.getElementById("questnum").value == 20) {
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
};

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
// Back button.


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

function changeColour(painSliderValue) {
  if (painSliderValue == 0) {
    $('#human-body').maphilight({fillColor: '00ff00'});
  };
  if (painSliderValue == 1) {
    $('#human-body').maphilight({fillColor: '33ff00'});
  };
  if (painSliderValue == 2) {
    $('#human-body').maphilight({fillColor: '66ff00'});
  };
  if (painSliderValue == 3) {
    $('#human-body').maphilight({fillColor: '99ff00'});
  };
  if (painSliderValue == 4) {
    $('#human-body').maphilight({fillColor: 'ccff00'});
  };
  if (painSliderValue == 5) {
    $('#human-body').maphilight({fillColor: 'ffff00'});
  };
  if (painSliderValue == 6) {
    $('#human-body').maphilight({fillColor: 'ffcc00'});
  };
  if (painSliderValue == 7) {
    $('#human-body').maphilight({fillColor: 'ff9900'});
  };
  if (painSliderValue == 8) {
    $('#human-body').maphilight({fillColor: 'ff6600'});
  };
  if (painSliderValue == 9) {
    $('#human-body').maphilight({fillColor: 'ff3300'});
  };
  if (painSliderValue == 10) {
    $('#human-body').maphilight({fillColor: 'ff0000'});
  };

  // Initialise the pain level with an empty string.
  var painLevel = '';

  // Set pain level depending on pain slider value.
  if (painSliderValue >= 0 && painSliderValue <= 4) {
    painLevel = ' NO PAIN';
  };
  if (painSliderValue >= 5 && painSliderValue <= 9) {
    painLevel = ' MODERATE PAIN';
  };
  if (painSliderValue == 10) {
    painLevel = ' UNBEARABLE PAIN';
  };

  // The current value will be the selected body part.
  var currentValue = $('#selected-body-part').val();

  // Remove any uppercase letter(s) from `currentValue`.
  // This is to make sure the pain level does not duplicate.
  currentValue = currentValue.replace(/[^a-z-]+/g, '');
  // Append the pain level to `selected-body-part`.
  $('#selected-body-part').val(currentValue + painLevel);
};

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
    $(this).data('maphilight', hData).trigger('alwaysOn.maphilight');
  });
});

function displayPart(id) {
  // Set the value of the input `selected-body-part` to the selected body part.
  $('#selected-body-part').val(id + ' NO PAIN');
};

// GETTING ANSWERED QUESTIONS FROM THE html
function pageLoad() {
var answerid = document.getElementById("answerid").value;
answerid = answerid.replace(/[\[\]/(\)'/,]+/g, '');
if (document.getElementById("questnum").value == 3) {
  if (answerid == null || answerid == "") {answerid = "Type it here"}
  document.getElementById("question3-input").value = answerid
}
else {
  answerid = answerid.split(" ");
  leng = answerid.length;
  for (var step = 0; step < leng; step++) {
    console.log(step)
    document.getElementById("option-text-"+ answerid[step]).checked = true
}
}
};

function back() {
console.log("Back button");
var direction = document.getElementById("direction").value;
document.getElementById("direction").value = "back";
var calculation = document.getElementById("questnum").value;
var counter = document.getElementById("counter").innerHTML;
console.log(direction);
//  Normal back button function without any questions being skipped.
if (counter == calculation && counter != 1 ) {
  document.getElementById("questnum").value -= 1;
};
if (calculation-counter == 1) {
  document.getElementById("questnum").value = calculation - 2;
};
var allqhide = document.getElementById("qhide").value;
var qhide = allqhide.split(",");
// Question skipping.
if (counter == 3 && qhide[0] == "t") {
  document.getElementById("questnum").value = 1;
};
if (counter == 7 && qhide[1] == "t") {
  document.getElementById("questnum").value = 5;
};
if (counter == 13 && qhide[2] == "t") {
  document.getElementById("questnum").value = 11;
};
if (counter == 18 && qhide[3] == "t") {
  document.getElementById("questnum").value = 16;
};
if (counter == 20 && qhide[4] == "t") {
  document.getElementById("questnum").value = 18;
};
if (counter == 23 && qhide[5] == "t") {
  document.getElementById("questnum").value = 21;
};
if (counter == 29 && qhide[6] == "t") {
  document.getElementById("questnum").value = 26;
};
if (counter == 23 && qhide[7] == "t") {
  document.getElementById("questnum").value = 4;
};
if (counter == 29 && qhide[8] == "t") {
  document.getElementById("questnum").value = 23;
};

};

window.onload=pageLoad;

// Forward button.
function forward() {
var counter = document.getElementById("counter").innerHTML;
var allqhide = document.getElementById("qhide").value;
var qhide = allqhide.split(",");
// Question skipping.
if (counter == 1) {
  if (document.getElementById("option-text-2").checked == true) {
    qhide[0] = "t";
    document.getElementById("qhide").value = qhide;
  } else {
    qhide[0] = "f";
    document.getElementById("qhide").value = qhide;
  };
};
if (counter == 5) {
  if (document.getElementById("option-text-32").checked == true) {
    qhide[1] = "t";
    document.getElementById("qhide").value = qhide;
  } else {
    qhide[1] = "f";
    document.getElementById("qhide").value = qhide;
  };
};
if (counter == 11) {
  if (document.getElementById("option-text-70").checked == true) {
    qhide[2] = "t";
    document.getElementById("qhide").value = qhide;
  } else {
    qhide[2] = "f";
    document.getElementById("qhide").value = qhide;
  };
};
if (counter == 16) {
  if (document.getElementById("option-text-101").checked == true) {
    qhide[3] = "t";
    document.getElementById("qhide").value = qhide;
  } else {
    qhide[3] = "f";
    document.getElementById("qhide").value = qhide;
  };
};
if (counter == 18) {
  if (document.getElementById("option-text-110").checked == true) {
    qhide[4] = "t";
    document.getElementById("qhide").value = qhide;
  } else {
    qhide[4] = "f";
    document.getElementById("qhide").value = qhide;
  };
};
if (counter == 21) {
  if (document.getElementById("option-text-128").checked == true) {
    qhide[5] = "t";
    document.getElementById("qhide").value = qhide;
  } else {
    qhide[5] = "f";
    document.getElementById("qhide").value = qhide;
  };
};
if (counter == 26){
  if (document.getElementById("option-text-145").checked == true) {
    qhide[6] = "t";
    document.getElementById("qhide").value = qhide;
  } else {
    qhide[6] = "f";
    document.getElementById("qhide").value = qhide;
  };
};
// Section skipping.
if (counter == 4) {
  if (document.getElementById("option-text-16").checked == true) {
    qhide[7] = "t";
    document.getElementById("qhide").value = qhide}
  else {
    qhide[7] = "f";
    document.getElementById("qhide").value = qhide;
  }
};
// Section skipping.
if (counter == 23) {
  if (document.getElementById("option-text-135").checked == true) {
    qhide[8] = "t";
    document.getElementById("qhide").value = qhide;
  } else {
    qhide[8] = "f";
    document.getElementById("qhide").value = qhide;
  };
};

console.log("Next button");
var direction = document.getElementById("direction").value;
document.getElementById("direction").value = "forward";
var calculation = parseInt(document.getElementById("questnum").value);
console.log("Next button");
var direction = document.getElementById("direction").value;
document.getElementById("direction").value = "forward";
var calculation = parseInt(document.getElementById("questnum").value);
var counter = document.getElementById("counter").innerHTML;
if (counter == calculation) {
  document.getElementById("questnum").value = calculation + 1;
};
if (counter-calculation == 1) {
  document.getElementById("questnum").value = calculation + 2;
};
// Question skipping.
if (qhide[0] == "t" && counter == 1) {
  document.getElementById("skippedqs").value = 1;
  document.getElementById("questnum").value = 3;
};
if (qhide[1] == "t" && counter == 5) {
  document.getElementById("skippedqs").value = 1;
  document.getElementById("questnum").value = 7
};
if (qhide[2] == "t" && counter == 11) {
  document.getElementById("skippedqs").value = 1;
  document.getElementById("questnum").value = 13;
};
if (qhide[3] == "t" && counter == 16) {
  document.getElementById("skippedqs").value = 1;
  document.getElementById("questnum").value = 18;
};
if (qhide[4] == "t" && counter == 18) {
  document.getElementById("skippedqs").value = 1;
  document.getElementById("questnum").value = 20;
};
if (qhide[5] == "t" && counter == 21) {
  document.getElementById("skippedqs").value = 1;
  document.getElementById("questnum").value = 23;
};
if (qhide[6] == "t" && counter == 26) {
  document.getElementById("skippedqs").value = 2;
  document.getElementById("questnum").value = 29;
};
// Section skipping.
if (qhide[7] == "t" && counter == 4) {
  document.getElementById("skippedqs").value = 18;
  document.getElementById("questnum").value = 23;
};
if (qhide[8] == "t" && counter == 23) {
  document.getElementById("skippedqs").value = 5;
  document.getElementById("questnum").value = 29;
};
console.log(direction);
};


// References:
// https://stackoverflow.com/questions/53499666/change-styling-of-a-certain-part-in-h1-tag-when-in-jinja-template
// https://stackoverflow.com/questions/53622707/change-colour-of-map-area-on-click
