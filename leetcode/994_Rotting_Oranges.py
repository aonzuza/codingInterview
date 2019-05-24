
class RottenOranges:

    def __init__(self,matrix):

        self.matrix = matrix;
        self.total_rows = len(matrix);
        self.total_cols = len(matrix[0])

    def check_orange_status(self):

        rotten_orange_positions = [];
        for row in range(self.total_rows):
            for col in range(self.total_cols):
                value = self.matrix[row][col];
                if value == 2:
                    #minute = 0
                    rotten_orange_positions.append([row,col,0]);

        def find_adjacent_positions(row,col):
            legitimate_positions = [];

            for potential_row, potential_col in [row-1,col],[row+1,col],[row,col-1],[row,col+1]:
                if 0 <= potential_row < self.total_rows and  0 <= potential_col < self.total_cols:
                    legitimate_positions.append([potential_row,potential_col]);

            return legitimate_positions;


        current_minute = 0;
        while len(rotten_orange_positions) > 0:
            rotten_orange_row,rotten_orange_col,current_minute = rotten_orange_positions.pop(0);

            for adjacent_row , adjacent_col in find_adjacent_positions(rotten_orange_row,rotten_orange_col):

                if self.matrix[adjacent_row][adjacent_col] == 1:
                    self.matrix[adjacent_row][adjacent_col] = 2;
                    rotten_orange_positions.append([adjacent_row,adjacent_col,current_minute + 1]);

        for row in self.matrix:
            if 1 in row:
                return -1;
        return current_minute;










inputs = [[1,1,1],[0,2,0],[0,1,1]];

rotten  = RottenOranges(inputs);
rotten_minute = rotten.check_orange_status();

print(rotten_minute);






# if inputs[-1][0]:
#     print(inputs[0][0]);
# else:
#     print('nothing');
