// Send the patient ID to the local storage.
function sendUser() {
  patient_id = document.getElementById("PatientID").innerHTML;
  // Check browser support
  if (typeof(Storage) !== "undefined") {
    // Store
    localStorage.setItem("PatientID", patient_id);
    // Retrieve
    console.log(localStorage.getItem("PatientID"));
  } else {
    document.getElementById("result").innerHTML = "Sorry, your browser does not support web storage.";
  };
};
