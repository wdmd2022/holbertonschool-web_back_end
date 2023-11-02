// tests for 8-job file

const expect = require('chai').expect;
const kue = require('kue');
const queue = kue.createQueue();
const createPushNotificationsJobs = require('./8-job');

describe('createPushNotificationsJobs test suite', () => {
    before(() => queue.testMode.enter());
    afterEach(() => queue.testMode.clear());
    after(() => queue.testMode.exit());

    it('display a error message if jobs is not an array', () => {
        expect(() => createPushNotificationsJobs('whatever', queue).to.throw('Jobs is not an array'));
    });

    });
