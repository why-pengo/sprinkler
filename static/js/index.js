function ready() {
    console.log(`running: ${running}`)
    set_to_running(running)

    setInterval(async function () {
        const csrftoken = getCookie('csrftoken');
        let data = await fetch("/running", {
            headers: {'X-CSRFToken': csrftoken},
        })
        let rv = await data.json();
        console.log(`running returned: ${rv}`);
        set_to_running(rv)
    }, 30000);

    get_schedules();
}

function switchClicked(el) {
    let checked = el.checked;
    const zone = el.value;
    console.log(`zone = ${zone}, checked = ${checked}`);
    // if (checked === false) {
    //     const url = `/zone_off/${zone}`;
    //     const csrftoken = getCookie('csrftoken');
    //     $.ajax(
    //         {
    //             url: url,
    //             headers: {'X-CSRFToken': csrftoken},
    //             success: function(result){
    //                 // let msg = `zoneOff = ${result.zoneOff}, timestamp = ${result.timestamp}\n`;
    //                 let msg = `zoneOff ${result.timestamp}`;
    //                 update_zone_text(zone, msg);
    //                 console.log(`call to ${url} result = ${result}`);
    //             }
    //         }
    //     );
    // } else {
    //     // el.prop('checked', false);
    //     const url = `/zone_on/${zone}`;
    //     const csrftoken = getCookie('csrftoken');
    //     $.ajax(
    //         {
    //             url: url,
    //             headers: {'X-CSRFToken': csrftoken},
    //             success: function(result){
    //                 // let msg = `zoneOn = ${result.zoneOn}, timestamp = ${result.timestamp}\n`;
    //                 let msg = `zoneOn ${result.timestamp}`;
    //                 update_zone_text(zone, msg);
    //                 console.log(`call to ${url} result = ${result}`);
    //             }
    //         }
    //     );
    // }
}

function update_zone_text(zone, msg) {
    let selector = document.getElementById(`zone${zone}`);
    selector.append(`${msg}<br />`);
    selector = document.getElementById("debug");
    selector.append(`${msg}<br />`);
}

function set_to_running(zone) {
    if (zone !== '0') {
        console.log(`set zone ${zone} to running.`);
        // $(":checkbox[value=" + zone + "]").prop("checked", "true");
        let cb = document.getElementById(`zone${ zone }`);
        cb.checked = true;
    }
}

async function get_schedules() {
    const csrftoken = getCookie('csrftoken');
    let data = await fetch("/list_jobs", {
        headers: {'X-CSRFToken': csrftoken},
    })
    let rv = await data.json();
    console.log(`list_jobs returned: ${rv}`);
    set_schedules(rv);
}

function set_schedules(data) {
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
                update_zone_text(item, msg);
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
