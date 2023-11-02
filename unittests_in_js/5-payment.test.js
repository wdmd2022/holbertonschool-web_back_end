const sinon = require('sinon');
const expect = require('chai').expect;
const Utils = require('./utils.js');
const sendPaymentRequestToApi = require('./5-payment.js');


describe('sendPaymentRequestToApi with hooks', function() {
    let spy;

    beforeEach(() => {
        // Spy on console.log before each test
        spy = sinon.spy(console, 'log');
    });

    afterEach(() => {
        // Restore the original console.log after each test
        spy.restore();
    });

    it('should log the string correctly when inputs are 100 and 20 and call console once', function() {
        sendPaymentRequestToApi(100, 20);
        expect(spy.calledWith('The total is: 120')).to.be.true;
        expect(spy.calledOnce).to.be.true;
    });

    it('should log the string correctly when inputs are 10 and 10 and call console once', function() {
        sendPaymentRequestToApi(10, 10);
        expect(spy.calledWith('The total is: 20')).to.be.true;
        expect(spy.calledOnce).to.be.true;
    });
});
