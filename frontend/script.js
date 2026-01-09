function loginVoice() {
  fetch("http://127.0.0.1:5000/login/voice", { method: "POST" })
    .then(res => res.json())
    .then(data => {
      alert(data.success ? "✅ Login Success" : "❌ Login Failed");
    })
    .catch(err => {
      alert("❌ Error connecting to server");
      console.error(err);
    });
}