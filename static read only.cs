using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
     class Class1
    {
        static readonly int var; //static reaonly var
        static Class1() //static constructor
        {
            Class1.var = 200;
        }
       static void Main(string[] args)
        {
            Console.WriteLine(Class1.var); //access var by class level
            Console.ReadLine();
        }
    }
}
