$(document).ready(function(){
    console.log(`id = ${id}`);
    console.log(`dow = ${dow}`);
    console.log(`start = ${start}`);
    console.log(`end = ${end}`);
    console.log(`active = ${active}`);
    console.log(`run_once = ${run_once}`);
    console.log(`zone = ${zone}`);

    $('#id_dow').val(dow);
    $('#id_start').val(start);
    $('#id_end').val(end);
    $('#id_zone').val(zone);
    if (active === 'True') {
        $('#id_active').prop('checked', true);
    }
    if (run_once === 'True') {
        $('#id_run_once').prop('checked', true);
    }
});
