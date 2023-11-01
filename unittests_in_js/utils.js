// module with calculateNumber function

const Utils = {
    calculateNumber: function(type, a, b) {
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
}

module.exports = Utils;
