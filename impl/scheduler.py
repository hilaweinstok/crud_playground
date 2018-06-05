from apscheduler.schedulers.blocking import BlockingScheduler

# todo hila : create this


def job():
    # Make the job run once a day
    print "Decorated job"

scheduler = BlockingScheduler()
scheduler.add_job(job, 'interval', days=1)
scheduler.start()
