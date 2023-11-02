// creates a job processor with kue

const kue = require('kue');
const queue = kue.createQueue();
let blacklisted = ['4153518780', '4153518781']

function sendNotification(phoneNumber, message, job, done) {
    job.progress(0, 100);
    if (blacklisted.includes(phoneNumber)) {
        let noCanText = new Error(`Phone number ${phoneNumber} is blacklisted`);
        done(noCanText);
        return;
    }
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
  let { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
queue.on('failed', (job, err) => console.log(`Job ${job.id} failed with message: ${err.message}`));
queue.on('complete', (job) => console.log(`Job ${job.id} completed`));
