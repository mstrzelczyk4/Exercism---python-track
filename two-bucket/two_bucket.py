def measure(bucket_one, bucket_two, goal, start_bucket):
    one = 0
    two = 0
    count_move = 1
    if start_bucket == "one":
        one = bucket_one
        bucket = 1
        if bucket_two == goal:
            return 2, "two", bucket_one
    else:
        two = bucket_two
        bucket = 2
        if bucket_one == goal:
            return 2, "one", bucket_two

    while True:
        if one == goal:
            return count_move, "one", two
        elif two == goal:
            return count_move, "two", one

        if bucket == 1:
            if not one:
                one = bucket_one
            elif two == bucket_two:
                two = 0
            else:
                if two + one <= bucket_two:
                    two += one
                    one = 0
                else:
                    one -= bucket_two - two
                    two = bucket_two
        else:
            if not two:
                two = bucket_two
            elif one == bucket_one:
                one = 0
            else:
                if two + one <= bucket_one:
                    one += two
                    two = 0
                else:
                    two -= bucket_one - one
                    one = bucket_one
        count_move += 1
