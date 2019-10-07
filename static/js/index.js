$(document).ready(function(){
    $('input:checkbox').click(function() {
        let checked = $(this).prop('checked');
        console.log(`zone = ${this.value}, checked = ${checked}`);
        if (checked === false) {
            const zone = this.value;
            const url = `/zone_off/${zone}`;
            $.ajax(
                {
                    url: url, success: function(result){
                        // let msg = `zoneOff = ${result.zoneOff}, timestamp = ${result.timestamp}\n`;
                        let msg = `zoneOff ${result.timestamp}`;
                        update_zone_text(zone, msg);
                        console.log(`call to ${url} result = ${result}`);
                    }
                }
            );
        } else {
            $('input:checkbox').not(this).prop('checked', false);
            const zone = this.value;
            const url = `/zone_on/${zone}`;
            $.ajax(
                {
                    url: url, success: function(result){
                        // let msg = `zoneOn = ${result.zoneOn}, timestamp = ${result.timestamp}\n`;
                        let msg = `zoneOn ${result.timestamp}`;
                        update_zone_text(zone, msg);
                        console.log(`call to ${url} result = ${result}`);
                    }
                }
            );
        }
    });

    console.log(`running: ${running}`)
    set_to_running(running)

    setInterval(function(){
        $.ajax({ url: "/running", success: function(data){
            // console.log(`running returned: ${data}`);
            set_to_running(data)
        }, dataType: "json"});
    }, 30000);

    get_schedules();
});

function update_zone_text(zone, msg) {
    let selector = $(`#zone${zone}`);
    selector.append(`${msg}<br />`);
    selector = $("#debug");
    selector.append(`${msg}<br />`);
}

function set_to_running(zone) {
    // console.log(`typeof(zone) = ${typeof(zone)}`);
    if (zone !== '0') {
        console.log(`set zone ${zone} to running.`);
        $(":checkbox[value=" + zone + "]").prop("checked","true");
    }
}

function get_schedules() {
    $.ajax({ url: "/list_jobs", success: function(data){
            // console.log(`list_jobs returned: ${data}`);
            set_schedules(data);
        }, dataType: "json"});
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
