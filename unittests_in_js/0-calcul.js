// a neat module with a cool function that returns a calculation


function calculateNumber(a, b) {
    let roundA = Math.round(a);
    let roundB = Math.round(b);
    let roundySum = roundA + roundB;
    return roundySum;
}


module.exports = calculateNumber;
