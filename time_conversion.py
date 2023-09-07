def time_conversion(seconds):
    return f"{seconds // 3600} час(а/ов) и {(seconds % 3600) // 60} минут(а/ы)"


print(time_conversion(int(input("Ведите количество секун: "))))
