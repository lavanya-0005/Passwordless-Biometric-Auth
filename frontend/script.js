let stream = null;

async function startCamera() {

    const video = document.getElementById("video");

    stream = await navigator.mediaDevices.getUserMedia({
        video: true
    });

    video.srcObject = stream;
}
// =========================
// VOICE REGISTER
// =========================
async function registerUser() {

    const username = document.getElementById("username").value.trim();

    if (username === "") {
        alert("Enter Username");
        return;
    }

    document.getElementById("result").innerHTML =
        "🎤 Recording Voice... Please Speak";

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/register",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    username: username
                })
            }
        );

        const data = await response.json();

        document.getElementById("result").innerHTML =
            data.message;

        alert(data.message);

    } catch (error) {

        console.log(error);

        document.getElementById("result").innerHTML =
            "Voice Registration Failed";

        alert("Voice Registration Failed");
    }
}

// =========================
// VOICE LOGIN
// =========================
async function loginUser() {

    const username = document.getElementById("username").value.trim();

    if (username === "") {
        alert("Enter Username");
        return;
    }

    document.getElementById("result").innerHTML =
        "🎤 Verifying Voice...";

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/login/voice",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    username: username
                })
            }
        );

        const data = await response.json();

        document.getElementById("result").innerHTML =
            data.message;

        alert(data.message);

    } catch (error) {

        console.log(error);

        document.getElementById("result").innerHTML =
            "Voice Login Failed";

        alert("Voice Login Failed");
    }
}

// =========================
// FACE REGISTER
// =========================
async function registerFace() {

    const username = document.getElementById("username").value.trim();

    if (username === "") {
        alert("Enter Username");
        return;
    }

    const video = document.getElementById("video");
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");

    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    const image = canvas.toDataURL("image/jpeg");

    document.getElementById("result").innerHTML = "Registering Face...";

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/register/face",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    username: username,
                    image: image
                })
            }
        );

        const data = await response.json();

        document.getElementById("result").innerHTML = data.message;

        alert(data.message);

    } catch (error) {

        console.log(error);

        document.getElementById("result").innerHTML =
            "Face Registration Failed";

        alert("Face Registration Failed");
    }
}
// =========================
// FACE LOGIN
// =========================
async function loginFace() {

    const username = document.getElementById("username").value.trim();

    if (username === "") {
        alert("Enter Username");
        return;
    }

    const video = document.getElementById("video");
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");

    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    const image = canvas.toDataURL("image/jpeg");

    document.getElementById("result").innerHTML = "Verifying Face...";

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/login/face",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    username: username,
                    image: image
                })
            }
        );

        const data = await response.json();

        document.getElementById("result").innerHTML = data.message;

        alert(data.message);

    } catch (error) {

        console.log(error);

        document.getElementById("result").innerHTML =
            "Face Login Failed";

        alert("Face Login Failed");
    }
}