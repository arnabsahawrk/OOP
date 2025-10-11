try:
    result = 45 / 0
    print(result)
except Exception as e:
    print("Error Happened: ", e)
finally:
    print("Done")
