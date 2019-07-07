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
});
