async function fetchPlayers() {
    const response = await fetch('/');
    const html = await response.text();
    document.getElementById('playerList').innerHTML = html;
}

async function addPlayer() {
    const name = document.getElementById('playerName').value;
    const role = document.getElementById('playerRole').value;
    const res = await fetch('/add_player', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({name, role})
    });
    const players = await res.json();
    renderPlayers(players);
}

async function adjustPoints(name, delta) {
    const res = await fetch('/adjust_points', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({name, delta})
    });
    const players = await res.json();
    renderPlayers(players);
}

function renderPlayers(players) {
    const list = document.getElementById('playerList');
    list.innerHTML = '';
    players.forEach(player => {
        const li = document.createElement('li');
        li.textContent = `${player.name} (${player.role}) - ${player.points}`;
        li.style.color = player.role.toLowerCase() === "ground" ? "green" : "brown";

        const plus = document.createElement('button');
        plus.textContent = "+";
        plus.onclick = () => adjustPoints(player.name, 1);

        const minus = document.createElement('button');
        minus.textContent = "-";
        minus.onclick = () => adjustPoints(player.name, -1);

        li.appendChild(plus);
        li.appendChild(minus);
        list.appendChild(li);
    });
}

window.onload = () => fetchPlayers();
