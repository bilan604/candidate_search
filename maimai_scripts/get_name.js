function main(num) {
    let profiles = document.getElementsByClassName("mainContent___nwb6Q talent-common-card");
    let stack = [profiles[num]];
    let newStack = [];
    while (stack.length !== 0) {
        for (const si of stack) {
            if (!si.innerHTML.includes("<") && si.innerHTML.length > 1) {
                return si.innerHTML;
            }
        }

        newStack = [];
        for (let i=0; i<stack.length; i++) {
            //
            console.log(stack[i].children.length, "is null?");
            for (const child of stack[i].children) {
                newStack.push(child);
            }
            
        }

        stack = newStack;
    }
    return null;

}

return main(arguments[0]);