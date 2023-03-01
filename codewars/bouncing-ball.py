def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1

    passes = 1
    bounce_height = h

    while True:
        bounce_height *= bounce
        if bounce_height > window:
            passes += 2
        else:
            break
    return passes


if __name__ == "__main__":
    bouncing_ball(30, 0.66, 1.5)
