function print_sqaure_pattern(){
    let n = prompt("Enter a positive number to print pattern:");
    if (n<=0){
        console.log("enter a positive number")
    }
    for(let i=0; i<n; i++){
        row=''
        for(let j=0; j<n; j++){
            row += '* ' //adding star with a space in row
        }
        console.log(row);
    }
}

print_sqaure_pattern();


//while writing this code i made a mistake that i defined row variable above i-for loop by which previous row element is also added and printed in next row , the pattern was printing like below. 
// * * * 
// * * * * * * 
// * * * * * * * * * 