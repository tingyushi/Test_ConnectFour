import java.util.Scanner;

public class HumanPlayer extends Player{
	
	public HumanPlayer(char symbol, Board board, String name) {
        super(symbol, board, name);
    }

    @Override
    public void makeMove(Board board) {
        Scanner input = new Scanner(System.in);
        
        /*print message*/
        System.out.print(name + ", please input your move: ");
        
        /*receive input*/
        int colNum = Integer.valueOf(input.nextLine());
        
        /*make sure that user will enter number between [1, 7]*/
        while (! (colNum >= 1 && colNum <= 7)) {
        	System.out.print(name + ", please input a valid move: ");
        	colNum = Integer.valueOf(input.nextLine());
        }
        
        /*If this column is full, remind the user to change a column*/
        while (board.isColumnFull(colNum)) {
            input = new Scanner(System.in);
            System.out.print(name + ", please input a valid move: ");
            colNum = Integer.valueOf(input.nextLine());
        }
        
        /*add checker*/
        board.addChecker(colNum, symbol);      
    }
}
