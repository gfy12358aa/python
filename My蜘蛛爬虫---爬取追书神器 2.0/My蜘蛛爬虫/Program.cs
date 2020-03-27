using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace My蜘蛛爬虫
{
    class Program
    {
        static void Main(string[] args)
        {
            //   try
            //  {
            //       SQLhelper s = new SQLhelper();
            //               SqlConnection e = new SqlConnection(@"Data Source = LAPTOP-V3FES89C\SQLEXPRESS; Initial Catalog = books; Integrated Security = SSPI");
            //e.Open();
            //               SqlCommand com = new SqlCommand("INSERT INTO readl values ('wang','kehuan',12.0,500,'d','www.com')", e);
            //              int i = com.ExecuteNonQuery();
            //            Console.WriteLine(i);
            //            e.Close();
            //   }
            //    catch (Exception ex)
            //   {
            //        Console.WriteLine(ex.ToString());
            //       Console.ReadKey();
            //  }
            //
            
                MainLogic ml = new MainLogic(@"https://www.bilibili.com/bangumi/media/md6360", 100);
                Console.WriteLine("开始");
               var p= ml.Cal();
            film[] d = new film   [p.Count];
            string[] s = new string[Crawlers.Working.Count + ml.NORead.Count];
            string[] history = new string[Crawlers.history_visited.Count];
            for (int i = 0; i < p.Count; i++)
                d[i] = p[i];
            for (int i = 0; i < Crawlers.Working.Count; i++)
                s[i] = Crawlers.Working.Dequeue();
            for (int i = 0; i < ml.NORead.Count; i++)
                    s[i + Crawlers.Working.Count] = ml.NORead[i];
            IOHelper.writeTXT(@"save.txt", s);
            IOHelper.writeTXT(@"ran.txt", d);
            Crawlers.history_visited.CopyTo(history, 0, Crawlers.history_visited.Count);
                IOHelper.writeTXT(@"history.txt", history  );
              
            
        }
    }
}
