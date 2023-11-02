// creates a queue with kue

const kue = require('kue');
const queue = kue.createQueue();
const bbqFixins = {
  phoneNumber: '5555555555',
  message: 'WAZZUP',
}
const newJob = queue.create('push_notification_code', bbqFixins)

newJob.save((err) => {
    if (!err) {
        console.log(`Notification job created: ${newJob.id}`);
    }
});
newJob.on('complete', () => console.log('Notification job copmleted'));
newJob.on('failed', () => console.log('Notification job failed'));
