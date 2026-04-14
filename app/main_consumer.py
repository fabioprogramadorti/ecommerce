from app.etl.consumer import OrderConsumer


def main():

    worker = OrderConsumer()
    worker.run()


if __name__ == "__main__":
    main()