function fillFilmList() {
    fetch ('/lab7/rest-api/films/')
    .then (function (data) {
        return data.json();
    })
    .then (function (films) {
        let tbody = document.getElementById('film-list');
        tbody.innerHTML = '';
        for (let i=0; i < films.length; i++) {
            let tr = document.createElement('tr');

            let tdTitle = document.createElement('td');
            let tdTitleRus = document.createElement('td');
            let tdYear = document.createElement('td');
            let tdActions = document.createElement('td');

            tdTitle.innerHTML = films[i].title == films[i].title_ru ? '': `<i>(${films[i].title})</i>`;
            tdTitleRus.innerText = films[i].title_ru;
            tdYear.innerText = films[i].year;

            let editButton = document.createElement('button');
            editButton.innerText = 'Редактировать';
            editButton.onclick = function() {
                editFilm(films[i].id);
            };

            let delButton = document.createElement('button');
            delButton.innerText = 'Удалить';
            delButton.onclick = function() {
                deleteFilm(films[i].id, films[i].title_ru);
            };

            tdActions.appendChild(editButton);
            tdActions.appendChild(delButton);

            tr.append(tdTitle);
            tr.append(tdTitleRus);
            tr.append(tdYear);
            tr.append(tdActions);   

            tbody.append(tr);
        }
    })
}

function deleteFilm(id, title) {
    if (! confirm (`Вы точно хотите удалить фильм "${title}"?`))
        return;

    fetch(`/lab7/rest-api/films/${id}`, {method: 'DELETE'})
        .then(function () {
            fillFilmList();
        });
}

function showModal() {
    document.querySelector('div.modal').style.display = 'block';
    document.getElementById('description-error').innerText = '';
    document.getElementById('title-error').innerText = '';
    document.getElementById('title_ru-error').innerText = '';
    document.getElementById('year-error').innerText = '';
}

function hideModal() {
    document.querySelector('div.modal').style.display = 'none'
}

function cancel() {
    hideModal();
}

function addFilm() {
    document.getElementById('id').value = ''; 
    document.getElementById('title').value = '';
    document.getElementById('title_ru').value = '';
    document.getElementById('year').value = '';
    document.getElementById('description').value = '';
    showModal();
}

function sendFilm() {
    const id = document.getElementById('id').value;
    const film = {
        title: document.getElementById('title').value,
        title_ru: document.getElementById('title_ru').value,
        year: document.getElementById('year').value,
        description: document.getElementById('description').value,
    }

    const url = `/lab7/rest-api/films/${id}`;
    const method = id === '' ? 'POST' : 'PUT';    

    fetch(url, {
        method: method,
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(film)
    })

    .then (function(resp){
        if (resp.ok) {
            fillFilmList();
            hideModal();
            return {};
        }
        return resp.json();
    })

    .then (function(errors) {
        if (errors.description)
            document.getElementById('description-error').innerText = errors.description;
        if (errors.title)
            document.getElementById('title-error').innerText = errors.title;

        if (errors.title_ru)
            document.getElementById('title_ru-error').innerText = errors.title_ru;

        if (errors.year)
            document.getElementById('year-error').innerText = errors.year;

    });
}

function editFilm(id) {
    fetch (`/lab7/rest-api/films/${id}`)
    .then (function(data){
        return data.json();
    })

    .then (function (film){
        document.getElementById('id').value = id;
        document.getElementById('title').value = film.title || '';
        document.getElementById('title_ru').value = film.title_ru || '';
        document.getElementById('year').value = film.year || '';
        document.getElementById('description').value = film.description || '';

        showModal();
    })
}