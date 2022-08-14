function ready() {
    getRunning();
    setInterval(getRunning, 30000);
    getSchedules();
    getWeather();
}

function getRunning() {
    const csrftoken = getCookie("csrftoken");
    fetch("/running", {headers: {"X-CSRFToken": csrftoken}, })
        .then(data => data.json())
        .then(rv => setToRunning(rv))
        .catch(err => console.log(err));
}

function switchClicked(el) {
    let checked = el.checked;
    const zone = el.value;
    const csrftoken = getCookie("csrftoken");
    console.log(`zone = ${zone}, checked = ${checked}`);
    let msg;
    if (checked === false) {
        const url = `/zone_off/${zone}`;
        fetch(url, {method: "PUT", headers: {"X-CSRFToken": csrftoken},})
            .then(rv => rv.json())
            .then(data => updateZoneText(zone, `zoneOff ${data.timestamp}`))
            .catch(err => console.log(err));
    } else {
        const url = `/zone_on/${zone}`;
        fetch(url, {method: "PUT", headers: {"X-CSRFToken": csrftoken},})
            .then(rv => rv.json())
            .then(data => updateZoneText(zone, `zoneOn ${data.timestamp}`))
            .catch(err => console.log(err));
    }
}

function updateZoneText(zone, msg) {
    // console.log(`zone = ${zone}, msg = ${msg}`);
    let ul = document.getElementById(`zone_${zone}_ul`);
    let li = document.createElement("li");
    li.appendChild(document.createTextNode(msg));
    ul.appendChild(li);
}

function setToRunning(zone) {
    // console.log(`called  with ${zone}.`);
    if (zone !== 0) {
        console.log(`set zone ${zone} to running.`);
        document.getElementById(`zone${ zone }`).checked = true;
    }
}

function getSchedules() {
    const csrftoken = getCookie("csrftoken");
    fetch("/list_jobs", {headers: {"X-CSRFToken": csrftoken}, })
        .then(data => data.json())
        .then(json => setSchedules(json))
        .catch(err => console.log(err));
}

function setSchedules(data) {
    for (let zones of data) {
        for (let item in zones) {
            // console.log(`Array.isArray(zones[${item}]) = ${Array.isArray(zones[item])}`);
            // console.log(`zones[${item}] = ${zones[item]}`);
            for (let schedule of zones[item]) {
                // console.log(`item[schedule] = ${item[schedule]}`);
                let msg = "";
                for (let [k, v] of Object.entries(schedule)) {
                    // console.log(`k, v = ${k}, ${v}`);
                    msg = msg.concat(`${v} `);
                }
                updateZoneText(item, msg);
            }
        }
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function getWeather() {
    let url = "https://api.weather.gov/gridpoints/FFC/54,98/forecast/hourly";
    let userAgent = "(My sprinkler, morgan.jon@icloud.com)";
    fetch(url, {headers: {"User-Agent": userAgent}})
        .then(rv => rv.json())
        .then(data => addWeather(data));
}

function addWeather(data) {
    let periods = data["properties"]["periods"];
    let zone = 1;
    for (let period of periods.slice(0, 5)) {
        let el = document.getElementById(`zone_${zone}_weather`);
        let icon = period["icon"];
        let image = icon.replace("?size=small", "");
        let time = new Date(period["startTime"]);
        let today = `${time.getFullYear()}-${time.getMonth()}-${time.getDate()} ${time.getHours()}:00`;
        el.innerHTML = `<div class="div-container">
                          <p class="m-0 p-0">${today}</p>
                          <p class="m-0 p-0"><img src="${image}"/></p>
                          <p class="m-0 p-0">${period["temperature"]} ${period["temperatureUnit"]} ${period["shortForecast"]}</p>
                          <p class="m-0 p-0">${period["windSpeed"]} ${period["windDirection"]}</p>
                        </div>`;
        zone = zone + 1;
    }
}
