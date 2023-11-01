// a neat module with a cool function that returns a cooler calculation


function calculateNumber(type, a, b) {
    const roundA = Math.round(a);
    const roundB = Math.round(b);

    switch (type) {
        case 'SUM':
            const roundlySummed = roundA + roundB;
            return roundlySummed;
        case 'SUBTRACT':
            const roundlySubtracted = roundA - roundB;
            return roundlySubtracted;
        case 'DIVIDE':
            if (roundB === 0) {
                return 'Error';
            }
            const roundlyDivided = roundA / roundB;
            return roundlyDivided;
    }
}


module.exports = calculateNumber;
