# class SpinalTraversal:
#
#     def __init__(self,matrix):
#         self.matrix    = matrix;
#         self.totalRows = len(self.matrix);
#         self.totalCols = len(self.matrix[0]);
#         self.totalRounds = self.totalRows * self.totalCols;
#
#
#         self.right = 0;
#         self.down  = 1;
#         self.left  = 2;
#         self.up    = 3;
#         self.directions = [self.right,self.down,self.left,self.up];
#
#     def next_direction(self,current_direction):
#         if current_direction == self.right:
#             return self.down;
#         elif current_direction == self.down:
#             return self.left;
#         elif current_direction == self.left:
#             return self.up;
#         else:
#             return self.right;
#
#     def next_position(self,current_direction,row,col):
#         if current_direction == self.right:
#             return (row,col+1);
#         elif current_direction == self.down:
#             return (row+1,col);
#         elif current_direction == self.left:
#             return (row,col-1);
#         else:
#             return (row-1,col);
#     def should_change_direction(self,row,col):
#
#         is_in_row  = 0 <= row < self.totalRows;
#         is_in_col  = 0 <= col < self.totalCols;
#
#         if is_in_row and is_in_col:
#             if self.matrix[row][col] is None:
#                 return True;
#             return False;
#         return True;
#
#     def startTravel(self):
#         row = 0;
#         col = 0;
#         current_direction = self.right;
#         while self.totalRounds > 0:
#
#             print(self.matrix[row][col]);
#             self.matrix[row][col] = None;
#             self.totalRounds -=1;
#             next_position = self.next_position(current_direction,row,col);
#
#             if self.should_change_direction(next_position[0],next_position[1]):
#                 current_direction = self.next_direction(current_direction);
#                 next_position = self.next_position(current_direction,row,col);
#                 row = next_position[0];
#                 col = next_position[1];
#             else:
#                 row = next_position[0];
#                 col = next_position[1];

#
#
#
# x = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#
# spinal = SpinalTraversal(x);
# spinal.startTravel();



# # print(spinal.totalRows);
#
# x = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# #
# totalRows = len(x);
# totalCols = len(x[0]);
#
# colMax = totalCols-1;
# colMin = 0;
#
# rowMax = totalRows-1;
# rowMin = 0;
#
# round = totalRows * totalCols;
#
# isAdd = True;
# col = 0;
# row = 0;
# for _ in range(round+3):
#
#     if isAdd:
#         if col < colMax:
#             # print('add col');
#             print(x[row][col]);
#             col +=1;
#             if col + 1 == colMax:
#                 rowMin +=1;
#         elif row < rowMax:
#             # print('add row');
#             print(x[row][col]);
#             row +=1;
#             if row + 1 == rowMax:
#                 colMax -=1;
#         else:
#             isAdd = False;
#     else:
#         if col > colMin:
#             # print('minus col');
#             print(x[row][col]);
#             col -=1;
#             if col - 1 == colMin:
#                 rowMax -=1;
#         elif row > rowMin:
#             # print('minus row');
#             print(x[row][col]);
#             row -=1;
#             if row - 1 == rowMin:
#                 colMin +=1;
#         else:
#             isAdd = True;
