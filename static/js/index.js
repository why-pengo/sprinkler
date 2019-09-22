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
            console.log(`running returned: ${data}`);
            set_to_running(data)
        }, dataType: "json"});
    }, 30000);
});

function set_to_running(zone) {
    if (zone !== '0') {
        console.log(`set zone ${zone} to running.`);
        $(":checkbox[value=" + zone + "]").prop("checked","true");
    }
}