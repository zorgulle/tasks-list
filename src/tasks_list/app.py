if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("init", action='store_true', help="Init project")
    args = parser.parse_args()

    print(args.init)

    import logging
    logging.basicConfig()