// it's good to chai to test things, like this better calculateNumber


const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', function() {
    describe('SUM', function() {
        it('should sum correctly mixed rounding pairs', function() {
            expect(calculateNumber('SUM', 2.2, 7.8)).to.equal(10);
        });
        it('should sum correctly whole numbers', function() {
            expect(calculateNumber('SUM', 3, 7)).to.equal(10);
        });
    });
    describe('SUBTRACT', function() {
        it('should return rounded negative numbers', function() {
            expect(calculateNumber('SUBTRACT', 2.2, 7.8)).to.equal(-6);
        });
        it('should return non-rounding-needed negative numbers', function() {
            expect(calculateNumber('SUBTRACT', 2, 8)).to.equal(-6);
        });
        it('should return rounded positive numbers', function() {
            expect(calculateNumber('SUBTRACT', 7.8, 2.2)).to.equal(6);
        });
        it('should return non-rounding-needed positive numbers', function() {
            expect(calculateNumber('SUBTRACT', 8, 2)).to.equal(6);
        });
    });
    describe('DIVIDE', function() {
        it('should correctly divide positive numbers after rounding', function() {
            expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
        });
        it('should return a whole number result where appropriate after division', function() {
            expect(calculateNumber('DIVIDE', 3.6, 1.8)).to.equal(2);
        });
        it('should return Error when division by zero after rounding', function() {
            expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
        });
        it('should return Error when division by zero without rounding', function() {
            expect(calculateNumber('DIVIDE', 4, 0)).to.equal('Error');
        });
    });
});
