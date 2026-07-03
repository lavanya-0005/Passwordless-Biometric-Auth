async function loadDashboard() {

    const response = await fetch(
        "http://127.0.0.1:5000/dashboard"
    );

    const data = await response.json();

    // Dashboard Cards
    document.getElementById("users").innerText =
        data.total_users;

    document.getElementById("voice").innerText =
        data.voice_logins;

    document.getElementById("face").innerText =
        data.face_logins;

    document.getElementById("total").innerText =
        data.total_logins;

    // Login History Table
    let rows = "";

    data.history.forEach(item => {

        rows += `
        <tr>
            <td>${item[0]}</td>
            <td>${item[1]}</td>
            <td>${item[2]}</td>
            <td>${item[3]}</td>
        </tr>
        `;

    });

    document.getElementById("history").innerHTML = rows;

}

loadDashboard();