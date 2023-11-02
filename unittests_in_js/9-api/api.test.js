// testing our integration, oh yeah!
const request = require('request');
const expect = require('chai').expect;

describe('Cart page', function() {
    it('should return 200 and correct message for numeric id', function(done) {
        request.get('http://localhost:7865/cart/12', function(error, response, body) {
            expect(response.statusCode).to.equal(200);
            expect(body).to.equal('Payment methods for cart 12');
            done();
        });
    });

    it('should return 404 for non-numeric id', function(done) {
        request.get('http://localhost:7865/cart/hello', function(error, response, body) {
            expect(response.statusCode).to.equal(404);
            done();
        });
    });

});

describe('test suite for index page', function() {
    it('should return 200 when everything is all good', function(done) {
        request.get('http://localhost:7865', function(error, response, body) {
            expect(response.statusCode).to.equal(200);
            done();
        });
    });

    it('should welcome us warmly', function(done) {
        request.get('http://localhost:7865', function(error, response, body) {
            expect(body).to.equal('Welcome to the payment system');
            done();
        });
    });
});
