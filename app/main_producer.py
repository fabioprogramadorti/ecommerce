from app.etl.producer import OrderETLProducer


def main():

    etl = OrderETLProducer()
    etl.run("data/orders.csv")


if __name__ == "__main__":
    main()