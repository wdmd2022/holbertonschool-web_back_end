// module file with summation of money using calculateNumber

const Utils = require('./utils');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
    const cash = Utils.calculateNumber('SUM', totalAmount, totalShipping);
    console.log(`The total is: ${cash}`);
    return cash;
}

module.exports = sendPaymentRequestToApi;
