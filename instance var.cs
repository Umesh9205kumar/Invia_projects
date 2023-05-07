using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
   class office
    {
        readonly int ID;
        string name;
        double salary;
        office(int a, string n, double c)
        {
            this.ID = a;
            this.name = n;
            this.salary = c;
        }
        public void print()
        {
            
            Console.Write(ID+" ");
            Console.Write(name +" ");
            Console.WriteLine(salary+" ");
        }
        public void changing(int s, string n)
        {
            this.salary = s;
            this.name = n;
        }
        public static void Main(string[] args)
        {
            Console.WriteLine("ID" + " " + "Name" + " " + "Salary");
            office obj = new office(11, "Umesh", 5000);
            office obj1 = new office(10, "Deepa", 6000);
            obj1.changing(5000, "Deepak");
            obj1.print();
            obj.print();
            Console.ReadLine();
        }
    }
}
