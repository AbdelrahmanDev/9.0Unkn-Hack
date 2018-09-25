import java.util.Scanner;

public class fPro {
	
	public static void main(String [] Hell)
	{
		Scanner input = new Scanner(System.in);
		System.out.println("Hello All In X-O Game. ");
		// Ta3ref El-Mota3*y rat
		//-----------------------------------------------
		int fPlayer = 0, sPlayer = 0, round = 0, fIndex, sIndex;
		String arr[] = { "1" , "2" , "3" , "4" , "5" , "6" ,  "7" , "8" , "9" };
		boolean win = false;
		String fp , sp , again;
		//-----------------------------------------------
		while(true)
		{
			System.out.println("======================================");
			System.out.println("======================================");
			System.out.println("1st Player ==> " + fPlayer + " : 2nd Player ==> " + sPlayer);
			System.out.print("Please , The 1st Player Choose His Sympol : ");
			fp = input.next();
			System.out.print("Please , The 2nd Player Choose His Sympol : ");
			sp = input.next();
			while(win == false)
			{
				System.out.print(" /=============================\\\n");
				System.out.print("/---[ " + arr[0] + " ]-----[ " + arr[1] + " ]-----[ " + arr[2] + " ]---\\\n");
				System.out.print("|                                |\n");
				System.out.print("|---[ " + arr[3] + " ]-----[ " + arr[4] + " ]-----[ " + arr[5] + " ]----|\n");
				System.out.print("|                                |\n");
				System.out.print("\\---[ " + arr[6] + " ]-----[ " + arr[7] + " ]-----[ " + arr[8] + " ]---/\n");
				System.out.print(" \\=============================/\n");
				if(round % 2 == 0)
				{
					if(round == 9)
					{
						System.out.println("Closed!");
						win = true;
					}
					else
						{
						System.out.print("Please , 1st Player Chooses The Box & Write its Number : ");
						fIndex = input.nextInt();
						while(arr[fIndex - 1] == fp || arr[fIndex - 1] == sp)
						{
							System.out.print("Sorry This Place Can,t Be Placed , Please Choose Other Place : ");
							fIndex = input.nextInt();
						}
						arr[fIndex - 1] = fp;
						if((arr[0] == arr[4] && arr[4] == arr[8]) || (arr[1] == arr[4] && arr[4] == arr[7]) || (arr[6] == arr[7] && arr[7] == arr[8]) || (arr[1] == arr[0] && arr[0] == arr[2]) || (arr[2] == arr[4] && arr[4] == arr[6]) || (arr[3] == arr[4] && arr[4] == arr[5]) ||(arr[0] == arr[3] && arr[3] == arr[6]) || (arr[2] == arr[5] && arr[5] == arr[8]))
						{
							win = true;
							fPlayer++;
							System.out.println("Congratulations, 1st Player Is Winner!!");
							System.out.print(" /=============================\\\n");
							System.out.print("/---[ " + arr[0] + " ]-----[ " + arr[1] + " ]-----[ " + arr[2] + " ]---\\\n");
							System.out.print("|                                |\n");
							System.out.print("|---[ " + arr[3] + " ]-----[ " + arr[4] + " ]-----[ " + arr[5] + " ]----|\n");
							System.out.print("|                                |\n");
							System.out.print("\\---[ " + arr[6] + " ]-----[ " + arr[7] + " ]-----[ " + arr[8] + " ]---/\n");
							System.out.print(" \\=============================/\n");
							System.out.print("Press Any Char to Continue : ");
							again = input.next();
						}
							round++;
					}
				}
				else
				{
					if(round == 9)
					{
						System.out.println("Closed!");
						win = true;
					}
					else
					{
						System.out.print("Please , 2nd Player Chooses The Box & Write its Number : ");
						sIndex = input.nextInt();
						while(arr[sIndex - 1] == fp || arr[sIndex - 1] == sp)
						{
							System.out.print("Sorry This Place Can,t Be Placed , Please Choose Other Place : ");
							sIndex = input.nextInt();
						}
						arr[sIndex - 1] = sp;
						if((arr[0] == arr[4] && arr[4] == arr[8]) || (arr[1] == arr[4] && arr[4] == arr[7]) || (arr[6] == arr[7] && arr[7] == arr[8]) || (arr[1] == arr[0] && arr[0] == arr[2]) || (arr[2] == arr[4] && arr[4] == arr[6]) || (arr[3] == arr[4] && arr[4] == arr[5]) ||(arr[0] == arr[3] && arr[3] == arr[6]) || (arr[2] == arr[5] && arr[5] == arr[8]))
						{
							win = true;
							sPlayer++;
							System.out.println("Congratulations, 2nd Player Is Winner!!");
							System.out.print(" /=============================\\\n");
							System.out.print("/---[ " + arr[0] + " ]-----[ " + arr[1] + " ]-----[ " + arr[2] + " ]---\\\n");
							System.out.print("|                                |\n");
							System.out.print("|---[ " + arr[3] + " ]-----[ " + arr[4] + " ]-----[ " + arr[5] + " ]----|\n");
							System.out.print("|                                |\n");
							System.out.print("\\---[ " + arr[6] + " ]-----[ " + arr[7] + " ]-----[ " + arr[8] + " ]---/\n");
							System.out.print(" \\=============================/\n");
							System.out.print("Press Any Char to Continue : ");
							again = input.next();
						}
						else if(arr[0] == arr[1] && arr[1] == arr[2] && arr[2] == arr[3] && arr[3] == arr[4] && arr[4] == arr[5] && arr[5] == arr[6] && arr[6] == arr[7] && arr[7] == arr[8])	
						{
							System.out.println("Closed!");
							win = true;
						}
						round++;
					}
				}  
			}
		}
	}
}
