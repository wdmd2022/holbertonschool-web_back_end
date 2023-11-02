// async tests using done

const expect = require('chai').expect;
const getPaymentTokenFromAPI = require('./6-payment_token.js');

describe('getPaymentTokenFromAPI', function() {
    it('should return a resolved promise with good news when success is true', function(done) {
        getPaymentTokenFromAPI(true)
            .then(response => {
                expect(response).to.eql({ data: 'Successful response from the API' });
                done();
            })
            .catch(err => {
                done(err);
            });
    });
});
