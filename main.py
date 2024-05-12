import motor_controller as mc

def main():
    try:
        mc.setup()
        mc.set_motor_speed1(40)
        mc.set_motor_speed2(80)
        mc.forward(2)
        mc.reverse(2)
        mc.left(2)
        mc.right(2)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        mc.cleanup()

if __name__ == "__main__":
    main()
