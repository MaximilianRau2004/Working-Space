import java.util.Scanner;


public class TicTacToe {
    
	  static char[][] board = new char[3][3];
	  char currentPlayer = 'X';
	 
 
	    public TicTacToe() {
	        board = new char[3][3];
	        currentPlayer = 'X';
	        initializeBoard();
	    }	  
	  
	public static void main(String[] args) {
		 TicTacToe game = new TicTacToe();
	     Scanner scanner = new Scanner(System.in);
	     int row, col;
	     
	     System.out.println("Willkommen bei Tic-Tac-Toe!");

	     while (!game.isBoardFull() && !game.checkWin()) {
	          game.printBoard();
	          System.out.println("Spieler " + game.currentPlayer + ", geben Sie Ihre Koordinaten (Reihe und Spalte) ein:");
	          row = scanner.nextInt();
	          col = scanner.nextInt();
	          game.makeMove(row, col);
	        }

	        game.printBoard();

	        if (game.checkWin()) {
	            System.out.println("Sie haben gewonnen!");
	        } else {
	            System.out.println("Unentschieden!");
	        }
	        scanner.close();
	    }

	private static void printBoard() {
		  System.out.println("-------------");
		  for (int i = 0; i < 3; i++) {
	            System.out.print("| ");
	            for (int j = 0; j < 3; j++) {
	                System.out.print(board[i][j] + " | ");
	            }
	            System.out.println();
	            System.out.println("-------------");
	        }
		
	}

	private static void initializeBoard() {
		for (int i=0; i < 3; i++) {
			for (int j=0; j< 3; j++) {
				board[i][j] = ' ';
			}
		}
		
	}

    // Überprüft, ob das Spiel unentschieden ist
    public boolean isBoardFull() {
	    for (int i = 0; i < 3; i++) {
	         for (int j = 0; j < 3; j++) {
	        	 if (board[i][j] == ' ') {
	                return false;
	                }
	         }
	     }
	    return true;
	}
    // Überprüft, ob ein Spieler gewonnen hat
    public boolean checkWin() {
        return (checkRows() || checkColumns() || checkDiagonals());
    }

    private boolean checkRows() {
        for (int i = 0; i < 3; i++) {
            if (checkRowCol(board[i][0], board[i][1], board[i][2])) {
                return true;
            }
        }
        return false;
    }

    private boolean checkColumns() {
        for (int i = 0; i < 3; i++) {
            if (checkRowCol(board[0][i], board[1][i], board[2][i])) {
                return true;
            }
        }
        return false;
    }

    private boolean checkDiagonals() {
        return (checkRowCol(board[0][0], board[1][1], board[2][2]) || checkRowCol(board[0][2], board[1][1], board[2][0]));
    }

    private boolean checkRowCol(char c1, char c2, char c3) {
        return ((c1 != ' ') && (c1 == c2) && (c2 == c3));
    }

    public void makeMove(int row, int col) {
        if (row >= 0 && row < 3 && col >= 0 && col < 3 && board[row][col] == ' ') {
            board[row][col] = currentPlayer;
            if (currentPlayer == 'X') {
                currentPlayer = 'O';
            } else {
                currentPlayer = 'X';
            }
        } else {
            System.out.println("Ungültiger Zug! Bitte versuchen Sie es erneut.");
        }
    }

}
