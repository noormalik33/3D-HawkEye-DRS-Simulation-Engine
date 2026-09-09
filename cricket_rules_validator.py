def calculate_umpires_call(final_y, final_z, ball_radius=0.036):
    # O(1) Rule Logic
    STUMP_H, STUMP_W = 0.72, 0.23
    half_w = STUMP_W / 2

    if (0.0 <= final_y <= STUMP_H) and (-half_w <= final_z <= half_w):
        if (STUMP_H - final_y) < ball_radius or (half_w - abs(final_z)) < ball_radius:
            return "UMPIRE'S CALL"
        return "OUT"
    return "MISS / NOT OUT"