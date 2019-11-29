try:
    n=int(input())
except ValueError:
    raise ValueError("value error occured")
except KeyboardInterrupt:
    raise KeyboardInterrupt("Keyboard Interrupt error occured")
except EOFError:
    raise EOFError("end of file error occured")
