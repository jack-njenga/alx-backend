import {createQueue} from 'kue';

const queue = createQueue();
const jobData = {
  phoneNumber: '+254739078101',
  message: 'Hello, call back when you get this'
};
const job = queue.create('push_notification_code', jobData);

job.on('complete', () => {
  console.log('Notification job completed');
});
job.on('failed', () => {
  console.log('Notification job failed');
});
job.save(() => {
  console.log(`Notification job created: ${job.id}`);
});