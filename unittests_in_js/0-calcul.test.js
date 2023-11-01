// it's good to test things, like calculateNumber


const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', function() {
    it('should round .4 down when there is just one down-rounding number', function() {
        assert.strictEqual(calculateNumber(1.4, 1.9), 3);
    });

    it('should round .4 down when both numbers are rounding down but they are quite large numbers all things considered so it does not matter that much', function() {
        assert.strictEqual(calculateNumber(99.4, 101.4), 200);
    });

    it('should round down .4 even when there are two small .4-numbers', function() {
        assert.strictEqual(calculateNumber(1.4, 3.4), 4);
    });

    it('should round up .9 when the other number rounds down', function() {
        assert.strictEqual(calculateNumber(1.9, 1.1), 3);
    });

    it('should round up .9 when the other number rounds up but just barely', function() {
        assert.strictEqual(calculateNumber(2.9, 3.6), 7);
    });

    it('should leave two numbers unrounded if possible', function() {
        assert.strictEqual(calculateNumber(100, 100), 200);
    });
})
