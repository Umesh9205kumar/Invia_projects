using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp2
{
    class palindrome
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter you input: ");
            string s = Console.ReadLine();
            int n = s.Length;
            int b=0;
            for(int i=0; i<n/2-1; i++)
            {
               
                if(s[i] != s[n-i-1])
                {
                    b = 1;
                }
            }
            if(b==1)
            {
                Console.WriteLine("String is not palindrom");
            }
            else
            {
                Console.WriteLine("This string is palindrom");
            }
            Console.ReadLine();
        }
    }
}
