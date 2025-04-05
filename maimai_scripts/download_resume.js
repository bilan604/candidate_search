
function main() {
    let divs = document.getElementsByClassName("resumeAction___2H0Jt");
    for (const div of divs) {
        if (div.innerHTML.includes("下载")) {
            div.click();
            return true;
        }
    }
    return false;
}

return main();

