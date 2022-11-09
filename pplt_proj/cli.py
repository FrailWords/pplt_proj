import click


@click.command()
@click.option('--profile', required=True, metavar='profile', help='Profile Number')
def main(profile):
    print(profile)


if __name__ == "__main__":
    main()
