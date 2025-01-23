import __name__meaning_1

print(f"Running {__file__}")    # __file__ gives complete path

if __name__ == "__main__":
    print(f"Executing in: {__name__}")  # __name__ gives module_name of execution

else:
    print(f"Executing From: {__name__}")

# Refer to the flowchart uploaded on git for explanation