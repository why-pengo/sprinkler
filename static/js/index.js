function ready() {
    getRunning();
    setInterval(getRunning, 30000);
    getSchedules();
}

function getRunning() {
    const csrftoken = getCookie('csrftoken');
    fetch("/running", {headers: {'X-CSRFToken': csrftoken}, })
        .then(data => data.json())
        .then(rv => setToRunning(rv))
        .catch(err => console.log(err))
}

function switchClicked(el) {
    let checked = el.checked;
    const zone = el.value;
    const csrftoken = getCookie('csrftoken');
    console.log(`zone = ${zone}, checked = ${checked}`);
    if (checked === false) {
        const url = `/zone_off/${zone}`;
        fetch(url, { headers: {'X-CSRFToken': csrftoken}, })
            .then(rv => `zoneOff ${rv.timestamp}`)
            .then(msg => updateZoneText(zone, msg))
            .catch(err => console.log(err))
    } else {
        const url = `/zone_on/${zone}`;
        fetch(url, { headers: {'X-CSRFToken': csrftoken}, })
            .then(rv => `zoneOn ${rv.timestamp}`)
            .then(msg => updateZoneText(zone, msg))
            .catch(err => console.log(err))
    }
}

function updateZoneText(zone, msg) {
    document.getElementById(`zone${zone}`).append(`${msg}<br />`);
}

function setToRunning(zone) {
    console.log(`called  with ${zone}.`);
    if (zone !== 0) {
        console.log(`set zone ${zone} to running.`);
        document.getElementById(`zone${ zone }`).checked = true;
    }
}

function getSchedules() {
    const csrftoken = getCookie('csrftoken');
    fetch("/list_jobs", {headers: {'X-CSRFToken': csrftoken}, })
        .then(data => data.json())
        .then(json => setSchedules(json))
        .catch(err => console.log(err)
    )
}

function setSchedules(data) {
    for (let zones of data) {
        for (let item in zones) {
            console.log(`Array.isArray(zones[${item}]) = ${Array.isArray(zones[item])}`);
            console.log(`zones[${item}] = ${zones[item]}`);
            for (let schedule of zones[item]) {
                console.log(`item[schedule] = ${item[schedule]}`);
                let msg = '';
                for (let [k, v] of Object.entries(schedule)) {
                    console.log(`k, v = ${k}, ${v}`);
                    // msg = msg.concat(`${k}=${v} `)
                    msg = msg.concat(`${v} `)
                }
                updateZoneText(item, msg);
            }
        }
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
