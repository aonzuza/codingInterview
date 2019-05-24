

def generate_pascal_triangle(total_rows):
    triangle = [];

    for row_index in range(total_rows):
        row = [];
        for col_index in range(row_index + 1):
            value = 1;
            if col_index != 0 and col_index != row_index:
                value = triangle[row_index-1][col_index-1] + triangle[row_index - 1][col_index];
            row.append(value);
        triangle.append(row);


triangle = generate_pascal_triangle(7);
# print(triangle);
