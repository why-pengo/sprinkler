function ready() {
    // for edits, may not do edits.
    // console.log(`id = ${id}`);
    // console.log(`dow = ${dow}`);
    // console.log(`start = ${start}`);
    // console.log(`end = ${end}`);
    // console.log(`active = ${active}`);
    // console.log(`run_once = ${run_once}`);
    // console.log(`zone = ${zone}`);
    // console.log(`crontab = ${crontab}`);
    // console.log(`cron_key = ${cron_key}`);
    //
    // document.getElementById("id_dow").value = dow;
    // document.getElementById("id_start").value = start;
    // document.getElementById("id_end").value = end;
    // document.getElementById("id_zone").value = zone;
    // if (active === "True") {
    //     document.getElementById("id_active").checked = true;
    // } else {
    //     document.getElementById("id_active").checked = false;
    // }
    // if (run_once === "True") {
    //     document.getElementById("id_run_once").checked = true;
    // } else {
    //     document.getElementById("id_run_once").checked = false;
    // }
}

function updateDow(el) {
    const dowInput = document.getElementById("dow");
    let dowAry = [];
    if (dowInput.value.length !== 0) {
        dowAry = dowInput.value.split(",");
    }
    // if class "active" is found check if we need to add, el.checked is undefined.
    if (el.className.search("active") > 1) {
        if (!dowAry.includes(el.value)) {
            dowAry.push(el.value);
        }
    } else {  // check if we need to remove
        if (dowAry.includes(el.value)) {
            const index = dowAry.indexOf(el.value);
            dowAry.splice(index, 1);
        }
    }
    dowAry.sort();
    console.log(`dowAry = ${dowAry}`);
    dowInput.value = dowAry.toString();
    console.log(`dowInput.value = ${dowInput.value}`);
}

function updateStart() {
    const startInput = document.getElementById("start");
    const startHour = document.getElementById("start_hour");
    const startMinute = document.getElementById("start_minute");
    const startAmPm = document.getElementById("start_ampm");
    let hour = 0;
    let minute = 0;
    let ampm = "AM";
    hour = startHour.value;
    minute = startMinute.value;
    ampm = startAmPm.value;
    startInput.value = `${hour}:${minute} ${ampm}`;
    console.log(`start = ${startInput.value}`);
}

function updateEnd() {
    const endInput = document.getElementById("end");
    const endHour = document.getElementById("end_hour");
    const endMinute = document.getElementById("end_minute");
    const endAmPm = document.getElementById("end_ampm");
    let hour = 0;
    let minute = 0;
    let ampm = "AM";
    hour = endHour.value;
    minute = endMinute.value;
    ampm = endAmPm.value;
    endInput.value = `${hour}:${minute} ${ampm}`;
    console.log(`end = ${endInput.value}`);
}

function updateZone(el) {
    const zoneInput = document.getElementById("zone");
    zoneInput.value = el.value;
}

function validate() {
    // dow
    const dowInput = document.getElementById("dow");
    if (dowInput.value.length < 1) {
        const dowErrDiv = document.getElementById("dow_err");
        dowErrDiv.classList.remove("d-none");
        dowErrDiv.innerText = "You have to select at least one day of week.";
        return false;
    }

    // start
    const startInput = document.getElementById("start");
    if (startInput.value.length < 1) {
        const startErrDiv = document.getElementById("start_err");
        startErrDiv.classList.remove("d-none");
        startErrDiv.innerText = "You have to select a start time.";
        return false;
    }

    // end
    const endInput = document.getElementById("end");
    if (endInput.value.length < 1) {
        const endErrDiv = document.getElementById("end_err");
        endErrDiv.classList.remove("d-none");
        endErrDiv.innerText = "You have to select an end time.";
        return false;
    }
    // TODO: end time must follow start time.

    // zone
    const zoneInput = document.getElementById("zone");
    if (zoneInput.value.length < 1) {
        const zoneErrDiv = document.getElementById("zone_err");
        zoneErrDiv.classList.remove("d-none");
        zoneErrDiv.innerText = "You have to select a zone.";
        return false;
    }

    console.log("form validation good.");
}