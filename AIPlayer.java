import java.util.Random;

public class AIPlayer extends Player{
	
	private int AIMoveCount;
	private int randomCol;
	private Random random;
	
	public AIPlayer(char symbol, Board board, String name) {
        super(symbol, board, name);
        AIMoveCount = 0;
        randomCol = 0;
        random = new Random();
    }
	
	@Override
	public void makeMove(Board board) {
		int canWin;
		
		//In the first two moves, nobody can win
		if(AIMoveCount < 2) {
			
			randomCol = random.nextInt(board.getColNum());
			board.addChecker(randomCol + 1, symbol);
			
			AIMoveCount++;

			return;
		} 
		
		//If AI can win
		canWin = board.winPossible(symbol);
		if(canWin != -1) {
			board.addChecker(canWin, symbol);	
			return;
		}
		
		// If the other player can win, we block this column with own symbol
		canWin = board.blockPossible(symbol);
		if (canWin != -1) {
			board.addChecker(canWin, symbol);
			return;
		}
		
		//Nobody can win, random move
		randomCol = random.nextInt(board.getColNum());
		//make sure AI can always pick a non-full column
		while(this.board.isColumnFull(randomCol + 1)) {
			randomCol = random.nextInt(board.getColNum());
		}
		board.addChecker(randomCol + 1, symbol);
    }
}