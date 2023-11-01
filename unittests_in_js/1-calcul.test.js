// it's good to test things, like this better calculateNumber


const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', function() {
    describe('SUM', function() {
        it('should sum correctly mixed rounding pairs', function() {
            assert.strictEqual(calculateNumber('SUM', 2.2, 7.8), 10);
        });
        it('should sum correctly whole numbers', function() {
            assert.strictEqual(calculateNumber('SUM', 3, 7), 10);
        });
    });
    describe('SUBTRACT', function() {
        it('should return rounded negative numbers', function() {
            assert.strictEqual(calculateNumber('SUBTRACT', 2.2, 7.8), -6);
        });
        it('should return non-rounding-needed negative numbers', function() {
            assert.strictEqual(calculateNumber('SUBTRACT', 2, 8), -6);
        });
        it('should return rounded positive numbers', function() {
            assert.strictEqual(calculateNumber('SUBTRACT', 7.8, 2.2), 6);
        });
        it('should return non-rounding-needed positive numbers', function() {
            assert.strictEqual(calculateNumber('SUBTRACT', 8, 2), 6);
        });
    });
    describe('DIVIDE', function() {
        it('should correctly divide positive numbers after rounding', function() {
            assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
        });
        it('should return a whole number result where appropriate after division', function() {
            assert.strictEqual(calculateNumber('DIVIDE', 3.6, 1.8), 2);
        });
        it('should return Error when division by zero after rounding', function() {
            assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
        });
        it('should return Error when division by zero without rounding', function() {
            assert.strictEqual(calculateNumber('DIVIDE', 4, 0), 'Error');
        });
    })


})
