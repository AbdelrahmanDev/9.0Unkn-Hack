import java.util.Scanner;

public class Main {

    public static boolean checkRight(int arrWidth, int arrY, int startx, char arr[][]){return arrWidth > arrY && arr[startx][arrY] == '-';}
    public static boolean checkLeft(int arrY, int startx, char arr[][]){return 0 < arrY && arr[startx][arrY] == '-';}
    public static boolean checkDown(int arrHeight, int arrX, int starty, char arr[][]){return arrHeight > arrX && arr[arrX][starty] == '-';}
    public static boolean checkUp(int arrX, int starty, char arr[][]){return 0 < arrX && arr[arrX][starty] == '-';}
    public static boolean checkNum5Up(char arr[][], int startx, int starty){return arr[startx][starty] == '*' && startx > 0;}
    public static boolean checkNum5Down(char arr[][], int startx, int starty){return arr[startx][starty] == '*' && arr.length > startx;}
    public static boolean checkNum5Left(char arr[][], int startx, int starty){return arr[startx][starty] == '*' && starty > 0;}
    public static boolean checkNum5Right(char arr[][], int startx, int starty){return arr[startx][starty] == '*' && starty < arr[startx].length;}

    public static int Rat(char arr[][], int startx, int starty, int endx, int endy) throws ArrayIndexOutOfBoundsException, StackOverflowError
    {
        if(startx == endx && starty == endy)
        {
            return 0;
        }
        else
        {
            if(checkRight(arr[0].length, starty + 1, startx, arr))
            {
                arr[startx][starty + 1] = '*';
                return Rat(arr, startx, starty + 1, endx, endy);
            }
            if(checkDown(arr.length,startx + 1, starty, arr))
            {
                arr[startx + 1][starty] = '*';
                return Rat(arr, startx + 1, starty, endx, endy);
            }
            if(checkLeft(starty - 1, startx, arr))
            {
                arr[startx][starty - 1] = '*';
                return Rat(arr, startx, starty - 1, endx, endy);
            }
            if(checkUp(startx - 1, starty, arr))
            {
                arr[startx - 1][starty] = '*';
                return Rat(arr, startx - 1, starty, endx, endy);
            }
            else
            {
                if(checkNum5Up(arr, startx - 1, starty))
                {
                    arr[startx][starty] = '#';
                    return Rat(arr, startx - 1, starty, endx, endy);
                }
                else if(checkNum5Down(arr, startx + 1, starty))
                {
                    arr[startx][starty] = '#';
                    return Rat(arr, startx + 1, starty, endx, endy);
                }
                else if(checkNum5Left(arr, startx, starty - 1))
                {
                    arr[startx][starty] = '#';
                    return Rat(arr, startx, starty - 1, endx, endy);
                }
                else if(checkNum5Right(arr, startx, starty + 1))
                {
                    arr[startx][starty] = '#';
                    return Rat(arr, startx + 1, starty, endx, endy);
                }
            }
        }
        return -1;
    }
    public static void map(int x, int y, char arr[][])
    {
        System.out.print(" ");
        for(int num = 0; num < y; num++)
            System.out.print("   " + num);
        System.out.println();
        for(int row = 0; row < x; row++)
        {
            for(int col = 0; col < y; col++)
            {
                if(col == 0)
                    System.out.print(row + " " + "| " + arr[row][col] + " ");
                else
                    System.out.print("| " + arr[row][col] + " ");
            }
            System.out.println();
            System.out.print("  ");
            for(int dash = 0; dash < y; dash++)
            {
                System.out.print("----");
            }
            System.out.println();
        }
    }
    public static void main(String [] Hell)
    {
        int x,y, StartX, StartY, EndX, EndY;
        Scanner sc = new Scanner(System.in);
        System.out.print("Please Enter The X Rows : ");
        x = sc.nextInt();
        System.out.print("Please Enter The Y Columns : ");
        y = sc.nextInt();
        char [][]arr = new char[x][y];
        for(int i = 0; i < x; i++)
            for(int j = 0; j < y; j++)
                arr[i][j] = '-';
        System.out.print("Select The Start Point 'x , y': ");
        StartX = sc.nextInt();
        StartY = sc.nextInt();
        arr[StartX][StartY] = '*';
        System.out.print("Select The End Point 'x , y' : ");
        EndX = sc.nextInt();
        EndY = sc.nextInt();

        int X = 0, Y = 0;

        while(true)
        {
            System.out.print("Enter The Point of # '-1 will exit the loop' : ");
            X = sc.nextInt();
            Y = sc.nextInt();
            if(X != -1 && Y != -1)
                arr[X][Y] = '#';
            else
                break;
        }

        int Rat = Rat(arr,StartX, StartY, EndX, EndY);
        try{
            if(Rat == -1)
                System.err.println("Can't Be Reached");
            else if(Rat == 0)
                System.out.println("Reached !!!");

        }catch(ArrayIndexOutOfBoundsException A)
        {
            System.out.println("Array out of the bound");
        }
        catch(StackOverflowError SE)
        {
            System.out.println("Stack Over Flow Error");
        }
        map(x,y,arr);


        /*for(int i = 0; i < x; i++)
        {
            for(int j = 0; j < y; j++)
                System.out.print(arr[i][j]);
            System.out.println();
        }
        */
    }
}
