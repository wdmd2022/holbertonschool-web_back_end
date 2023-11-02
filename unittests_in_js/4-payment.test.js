const sinon = require('sinon');
const expect = require('chai').expect;
const Utils = require('./utils.js');
const sendPaymentRequestToApi = require('./4-payment.js');


describe('sendPaymentRequestToApi using a stub', function() {
    it('should use calculateNumber correctly from Utils using a stub', function() {
        const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
        const spy = sinon.spy(console, 'log');
        sendPaymentRequestToApi(100, 20);
        expect(stub.calledWith('SUM', 100, 20)).to.be.true;
        expect(spy.calledWith('The total is: 10')).to.be.true;
        stub.restore();
        spy.restore();
    });
});
