"""Error check functions."""


def problem_check(response):
    """Check HTTP status code, which should be 200 at this point."""
    status = response.status_code
    if status != 200:
        print("There was a problem communicating with the spotify API")
        print("HTTP status code: " + str(status))
        print("Exiting")
        exit(-1)
