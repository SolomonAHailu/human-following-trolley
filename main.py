import motor_controller as mc

def main():
    try:
        mc.setup()
        # mc.set_motor_speed1(40)
        # mc.set_motor_speed2(80)
        # mc.forward(1)
        # mc.reverse(1)
        # mc.left(1)
        mc.right(1, speed1 = 40)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        mc.cleanup()

if __name__ == "__main__":
    main()
