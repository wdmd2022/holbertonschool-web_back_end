// module file with summation of money using calculateNumber

const Utils = require('./utils.js');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
    const cash = Utils.calculateNumber('SUM', totalAmount, totalShipping);
    console.log(`The total is: ${sum}`);
}

module.exports = sendPaymentRequestToApi;
