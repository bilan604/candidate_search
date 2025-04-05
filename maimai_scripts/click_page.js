

function main(num) {
    let pages = document.getElementsByClassName("pagesItem___3rw03");
    for (const page of pages) {
        if (page.innerHTML == num) {
            page.click();
            return true;
        }
    }
    return false;
}

return main(arguments[0]);

