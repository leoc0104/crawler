document.getElementById('show-entity-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const entityId = document.getElementById('show-id').value;
    const response = await fetch(`http://localhost:5000/entities/${entityId}`, {
        method: 'GET',
    });

    const data = await response.json();
    const entitiesList = document.getElementById('show-entity-list');

    entitiesList.innerHTML = '<ul>' + `
        <li>
            <strong>${data.text}</strong> <br>
            Rótulo: ${data.label} <br>
        </li>` + '</ul>';
});

document.getElementById('list-entities').addEventListener('click', async () => {
    const response = await fetch('http://localhost:5000/entities');
    const data = await response.json();
    const entityList = document.getElementById('entity-list');

    entityList.innerHTML = '<ul>' + data.map(entity => `
        <li>
            <strong>${entity.text}</strong> <br>
            Rótulo: ${entity.label} <br><br>
        </li>`).join('') + '</ul>';
});

document.getElementById('add-entity-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const text = document.getElementById('text').value;
    const label = document.getElementById('label').value;

    const response = await fetch('http://localhost:5000/entities', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, label })
    });

    const data = await response.json();
    alert(data.message);
});

document.getElementById('update-entity-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const entityId = document.getElementById('update-id').value;
    const text = document.getElementById('new-text').value;
    const label = document.getElementById('new-label').value;

    const response = await fetch(`http://localhost:5000/entities/${entityId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, label })
    });

    const data = await response.json();
    alert(data.message);
});

document.getElementById('delete-entity-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const entityId = document.getElementById('delete-id').value;

    const response = await fetch(`http://localhost:5000/entities/${entityId}`, {
        method: 'DELETE',
    });

    const data = await response.json();
    alert(data.message);
});
