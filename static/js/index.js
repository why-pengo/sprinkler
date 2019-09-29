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
                        let msg = `zoneOff = ${result.zoneOff}, timestamp = ${result.timestamp}\n`;
                        let selector = $(`#zone${zone}`);
                        selector.text(msg);
                        $("#debug").append(msg);
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
                        let msg = `zoneOn = ${result.zoneOn}, timestamp = ${result.timestamp}\n`;
                        let selector = $(`#zone${zone}`);
                        selector.text(msg);
                        selector = $("#debug");
                        selector.append(msg);
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

function set_schedules(schedules) {
    console.log(`Array.isArray(schedules) = ${Array.isArray(schedules)}`);
    if (Array.isArray(schedules)) {
        for (zone of schedules) {
            for (item in zone) {
                console.log(`zone[${item}] = ${zone[item]}`);
            }
        }
    }
}
