function createScript() {
  var script = ScriptApp.createScript();
  script.setTitle("YouTube Text Corrector");
  script.setDescription("Corrects Japanese text from YouTube captions");
}

function createTrigger() {
  var script = ScriptApp.getScriptById("SCRIPT_ID");
  ScriptApp.newTrigger("main")
    .timeBased()
    .everyHours(1) // Run every hour
    .create();
}