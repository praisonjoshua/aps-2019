import java.util.Scanner;
import java.util.ArrayList;
import java.io.BufferedReader; 
import java.io.IOException; 
import java.io.InputStreamReader; 
import java.util.Scanner;
import java.util.ArrayList;

class beautiful{
    public static void main(String[] args)
    {
        int testcase;
        Scanner input=new Scanner(System.in);
		
        testcase=input.nextInt();
        for(int jodi=0;jodi<testcase;jodi++)
        {
            int n=input.nextInt();
            int k=input.nextInt();
            int i,j;
			int[] N=new int[n];
			 int mu;
			 int l;
			 int o;
			 int erx;
			 int count;
			 
            
            for(i=0;i<n;i++)
            {
                N[i]=input.nextInt();
            }
            int counter=0;
            for(i=0;i<n;i++)
            {
                ArrayList<Integer> two=new ArrayList<Integer>(n);
                int[] reqf=new int[2001];
                for(j=i;j<n;j++)
                {int end=two.size()-1;
                     int beg=0;
                     
                     int mid=0;
                     while(end-beg>0)
                     {
                         mid=(beg+end)/2;
                         if(two.get(mid)<=N[j])
                         beg=mid+1;
                         else
                         end=mid;
                         
                     }
                     if(two.size()>beg&&two.get(beg)<N[j])
                     beg++;
                     two.add(beg,N[j]);
					 l=j-i+1;
                     
					 reqf[N[j]]++;
                     
                    mu=(int)Math.ceil((double)k/(double)l);
                    o=(k-1)/m;
                     erx=two.get(temp);
            count=reqf[erx];
                     if(count<2001&&reqf[count]>0)
                     counter++;
                }
            }
            System.out.println(counter);
        }    
    }
    
}