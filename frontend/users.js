let allUsers = [];

async function loadUsers() {

    const response = await fetch(
        "http://127.0.0.1:5000/users"
    );

    allUsers = await response.json();

    displayUsers(allUsers);

}

function displayUsers(users){

    let rows="";

    users.forEach(user=>{

        rows+=`

        <tr>

            <td>${user[0]}</td>

            <td>${user[1]}</td>

            <td>${user[2]}</td>

            <td>

                <button onclick="deleteUser(${user[0]})">

                    Delete

                </button>

            </td>

        </tr>

        `;

    });

    document.getElementById("usersTable").innerHTML=rows;

}

function searchUser(){

    const value=document
    .getElementById("search")
    .value
    .toLowerCase();

    const filtered=allUsers.filter(user=>

        user[1].toLowerCase().includes(value)

    );

    displayUsers(filtered);

}

async function deleteUser(id){

    if(!confirm("Delete this user?"))
        return;

    await fetch(

        "http://127.0.0.1:5000/delete-user/"+id,

        {

            method:"DELETE"

        }

    );

    loadUsers();

}

loadUsers();