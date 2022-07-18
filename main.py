from notify_visa_wait_times import NotifyVisaWaitTimes


def main():
    job = NotifyVisaWaitTimes('resources/cid.yaml')
    job.load()
    job.run()


if __name__ == '__main__':
    main()