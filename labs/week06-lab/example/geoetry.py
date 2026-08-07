def calculate_triangle_area(height, base):
    """Calculates and displays tritangle area"""
    area = 0.5 *height * base
    print(f"triangle with height {height} and base {base}")
    print(f"Area = 0.5 * {height} × {base} = {area}")
    print()

print("Calculating triangle areas:")
calculate_triangle_area(5, 3)
calculate_triangle_area(10, 7)