from my_modules import operators as ops
from my_modules import printrs as prntrs


def main():
    print("sum = ", ops.op_sum(5, 10, 12, 15))
    print("average = ", ops.op_average(10, 12, 11, 10, 12, 12, 17))
    prntrs.print_name("Stella")
    
if __name__ == "__main__":
    main()