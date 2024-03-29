
function createPushNotificationsJobs(jobs, queue){
  if (!(jobs instanceof Array)){
     console.error('Jobs is not an array');
     throw new Error('Jobs is not an array');
  }
  jobs.forEach((jobData) => {
  const job = queue.create('push_notification_code_3', jobData);

  job.on('enqueue', () => {
    console.log('Notification job created:', job.id);
  });
  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });
  job.on('failed', (err) => {
    console.error(`Notification job ${job.id} failed: ${err}`);
  });
  job.on('progress', (progress) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });
  job.save();
  });

}

export default createPushNotificationsJobs;