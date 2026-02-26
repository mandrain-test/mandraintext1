const { exec } = require("child_process");

function autoPush() {
  exec("git add .", (err, stdout, stderr) => {
    if (err) {
      console.error("Git add error:", err);
      return;
    }

    exec('git commit -m "auto update"', (err, stdout, stderr) => {
      if (err) {
        console.log("Nothing to commit or commit error");
      }

      exec("git push origin main", (err, stdout, stderr) => {
        if (err) {
          console.error("Push error:", err);
          return;
        }

        console.log("✅ Successfully pushed to GitHub");
      });
    });
  });
}

autoPush();