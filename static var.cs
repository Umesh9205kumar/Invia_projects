using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        static int b = 10; //static variable 
        static void Main(string[] args)
        {
            int a = Program.b; 
            Console.WriteLine(a);   
            Console.ReadLine();
        }
    }
}
