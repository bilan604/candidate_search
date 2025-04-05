function main() {
    let projects = document.getElementsByClassName("groupItem___15smE ");
    for (const project of projects) {
        if (project.innerHTML.includes(name) ) {
            project.click();
            return true;
        }
    }
    return false;
}

return main(arguments[0]);

