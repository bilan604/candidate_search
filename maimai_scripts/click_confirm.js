function main() {
    let divs = document.getElementsByClassName("mui-btn mui-btn-primary mui-btn-middle");
    for (const div of divs) {
		console.log("|",div.innerHTML,"|");
        if (div.innerHTML == "确 定") {
            div.click();
            return;
        }
    }
}

main();