public class Board {

	private final int NUM_OF_COLUMNS = 7;
	private final int NUM_OF_ROW = 6;
	private String b[][];
	
	/* 
	 * The board object must contain the board state in some manner.
	 * You must decide how you will do this.
	 * 
	 * You may add addition private/public methods to this class is you wish.
	 * However, you should use best OO practices. That is, you should not expose
	 * how the board is being implemented to other classes. Specifically, the
	 * Player classes.
	 * 
	 * You may add private and public methods if you wish. In fact, to achieve
	 * what the assignment is asking, you'll have to
	 * 
	 */
	
	public Board() {
		this.b = new String[NUM_OF_ROW][NUM_OF_COLUMNS];
		this.reset();
	}
	
	
	public void printBoard() {
		for(int i = 0; i < NUM_OF_ROW; i++) {
			System.out.println("---------------");
			System.out.print("|");
			
			for (int j = 0; j < NUM_OF_COLUMNS; j++) {
				if(b[i][j].isEmpty()) {
					System.out.print(" ");
					System.out.print("|");
				}else {
					System.out.print(b[i][j]);
					System.out.print("|");
				}
			}
			
			System.out.print("\n");
		}
		System.out.println("---------------");
	}
	
	
	public boolean containsWin() {
		for(int i = 0; i < NUM_OF_ROW; i++) {
			for (int j = 0; j < NUM_OF_COLUMNS; j++) {
				if ((!b[i][j].isEmpty()) && this.checkFour(i, j)) {
					return true;
				}
			}
		}
		return false;
	}
	
	
	public boolean isTie() {
		if(this.isBoardFull() && !this.containsWin()) {
			return true;
		}
		return false;
	}
	
	
	public void reset() {
		for(int i = 0; i < NUM_OF_ROW; i++) {
			for (int j = 0; j < NUM_OF_COLUMNS; j++) {
				b[i][j] = "";
			}
		}
	}
	
	
	/*add one checker to a specific column*/
	public void addChecker(int colNum, char symbol) {
		/*If this column is full, can not add any checker*/
		if(this.isColumnFull(colNum)) {
			return;
		}
		
		int colIndex = colNum - 1;
		int rowIndex = NUM_OF_ROW - 1;
		while(!b[rowIndex][colIndex].isEmpty()) {
			rowIndex -= 1;
		}
		b[rowIndex][colIndex] = String.valueOf(symbol);
	}
	
	
	/* Input: a column number
	 * If this column is full ---> return true
	 * Otherwise              ---> return false
	 * */
	public boolean isColumnFull(int colNum) {
		int colIndex = colNum - 1;
		for(int i = 0; i < NUM_OF_ROW; i++) {
			if(b[i][colIndex].isEmpty()) {
				return false;
			}
		}
		return true;
	}
	
	
	public int getRowNum() {
		return NUM_OF_ROW;
	}
	
	
	public int getColNum() {
		return NUM_OF_COLUMNS;
	}
	
	
	/* if next move is symbol, is it possible to win
	 * if yes, return which column can win
	 * if no, return -1*/
	public int winPossible(char symbol) {
		String[][] boardCopy = new String[NUM_OF_ROW][NUM_OF_COLUMNS];
		this.copyBoard(this.b, boardCopy);
		int ans = -1;
		int colNum = 1;
		
		while (colNum <= 7) {
			this.addChecker(colNum, symbol);
			if(this.containsWin()) {
				ans = colNum;
				break;
			}
			this.copyBoard(boardCopy, this.b);
			colNum++;
		}
		
		this.copyBoard(boardCopy, this.b);
		return ans;
	}
	
	
	/*
	 * checking if 'symbol' can block the other player is the same as checking if the other player can win
	 * yes ---> return which column to block
	 * no  ---> return -1
	 * */
	public int blockPossible(char symbol) {
		String self = String.valueOf(symbol);
		String other = "";
		
		/*find other player first*/
		for(int i = 0; i < NUM_OF_ROW; i++) {
			for (int j = 0; j < NUM_OF_COLUMNS; j++) {
				if(!b[i][j].isEmpty() && !b[i][j].equals(self) ) {
					other = b[i][j];
				}
			}
		}
		return this.winPossible(other.charAt(0));
	}
	
	
	/*
	 * If the board is full ---> True
	 * Otherwise            ---> False*/
	private boolean isBoardFull() {
		for(int i = 0; i < NUM_OF_ROW; i++) {
			for (int j = 0; j < NUM_OF_COLUMNS; j++) {
				if(b[i][j].isEmpty()) {
					return false;
				}
			}
		}
		return true;
	}
	
	
	private void copyBoard(String[][] source, String[][] dest) {
		for(int i = 0; i < NUM_OF_ROW; i++) {
			for(int j = 0; j < NUM_OF_COLUMNS; j++) {
				dest[i][j] = source[i][j];
			}
		}
	}
	
	
	/*given a coordinate(index number) (row, column)
	 * make sure that b[row][column] is not an empty string
	 * check if we can connect four staring at (row, column)
	 * If yes ---> true
	 * If No  ---> false*/
	private boolean checkFour(int row, int col) {
		String checker = b[row][col];
		
		/*direction up*/
		int[] row1 = {row - 1, row - 2, row - 3};
		int[] col1 = {col, col, col};
		if (isIn(row1, col1)) {
			if(b[row1[0]][col1[0]].equals(checker) && 
			   b[row1[1]][col1[1]].equals(checker) &&
			   b[row1[2]][col1[2]].equals(checker)) {
				return true;
			}
		}
		
		/*direction: left*/
		int[] row2 = {row, row, row};
		int[] col2 = {col - 1, col - 2, col - 3};
		if (isIn(row2, col2)) {
			if(b[row2[0]][col2[0]].equals(checker) && 
			   b[row2[1]][col2[1]].equals(checker) &&
			   b[row2[2]][col2[2]].equals(checker)) {
				return true;
			}
		}
		
		/*direction: up left*/
		int[] row3 = {row - 1, row - 2, row - 3};
		int[] col3 = {col - 1, col - 2, col - 3};
		if (isIn(row3, col3)) {
			if(b[row3[0]][col3[0]].equals(checker) && 
			   b[row3[1]][col3[1]].equals(checker) &&
			   b[row3[2]][col3[2]].equals(checker)) {
				return true;
			}
		}
		
		/*direction: up right*/
		int[] row4 = {row - 1, row - 2, row - 3};
		int[] col4 = {col + 1, col + 2, col + 3};
		if (isIn(row4, col4)) {
			if(b[row4[0]][col4[0]].equals(checker) && 
			   b[row4[1]][col4[1]].equals(checker) &&
			   b[row4[2]][col4[2]].equals(checker)) {
				return true;
			}
		}
		
		return false;
	}
	
	
	/* given three coordinates in one direction
	 * check if all the coordinates are in the board*/
	private boolean isIn(int[] rows, int[] cols) {
		for(int i = 0; i < rows.length; i++) {
			if(! (rows[i] >= 0 && rows[i] <= NUM_OF_ROW - 1)) {
				return false;
			}
		}
		
		for (int i = 0; i < cols.length; i++) {
			if(! (cols[i] >= 0 && cols[i] <= NUM_OF_COLUMNS - 1)) {
				return false;
			}
		}
		return true;
	}
	
}