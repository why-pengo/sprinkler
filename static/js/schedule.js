function ready() {
    console.log(`id = ${id}`);
    console.log(`dow = ${dow}`);
    console.log(`start = ${start}`);
    console.log(`end = ${end}`);
    console.log(`active = ${active}`);
    console.log(`run_once = ${run_once}`);
    console.log(`zone = ${zone}`);

    document.getElementById("id_dow").value = dow;
    document.getElementById("id_start").value = start;
    document.getElementById("id_end").value = end;
    document.getElementById("id_zone").value = zone;
    if (active === 'True') {
        document.getElementById("id_active").checked = true;
    }
    if (run_once === 'True') {
        document.getElementById("id_run_once").checked = true;
    }
}
