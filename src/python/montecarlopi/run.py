import time


def bench_python():
    from .montecarlopy import mcpi as mcpy  # noqa
    start = time.time()
    pi, calcs_p_sec = mcpy(1_000_000)
    stop = time.time()
    print("=" * 12)
    print("   PYTHON")
    print("=" * 12)

    print(f"{stop - start:.2f}secs runtime")
    print(pi)
    print(f"{calcs_p_sec} calculations per second")


def bench_rust():
    from .montecarlo3pi import mcpi as mcrs  # noqa

    start = time.time()
    pi, calcs_p_sec = mcrs(1_000_000)
    stop = time.time()
    print("=" * 12)
    print("    RUST")
    print("=" * 12)
    print(f"{stop - start:.2f}secs runtime")
    print(pi)
    print(f"{calcs_p_sec} calculations per second")


def main():
    bench_python()
    print("\n")
    bench_rust()


if __name__ == "__main__":
    main()
