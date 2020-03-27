using HtmlAgilityPack;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Net;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading;
using System.Threading.Tasks;

namespace My蜘蛛爬虫
{class film
    {
        public string name;
        public string url;
        public  string people;
        public double score;
    }
    class MainLogic
    {
        WebClient wc = new WebClient();
        HtmlDocument document = new HtmlDocument();
        private Crawlers s;
        private List<string> finishHtml = new List<string>();
        public  List<string> NORead = new List<string>();
        public MainLogic(string url, int max = 50)
        {
            restart(url, max);
        }
        public void restart(string url, int max)
        {
            Crawlers.maxurl = max;
            s = null;
            Crawlers.visited.Clear();
            Crawlers.Working.Clear();
            s = new Crawlers(url);
            LoadTxt();
            s.DownLoad();
            finishHtml.Clear();
            finishHtml.AddRange(Crawlers.visited);
        }

        public List<film> Cal()
        {
            List<film> read = new List<film>();
            Collection<HtmlNode> p = new Collection<HtmlNode>();
            //   StreamWriter sw = new StreamWriter(@"E:\新建文件夹(2)\1.txt", true, Encoding.UTF8);
            for (int i = 0; i < finishHtml.Count; i++)
            {film f=new film();
                f.url = finishHtml[i];
                //  if (!finishHtml[i].Contains(".html")) continue;
                string html = HTMLHELPER.GetHtml(finishHtml[i]);
                HtmlNode root, t;
                if (html == null) continue;
                document.LoadHtml(html);
                root = document.DocumentNode;
                if (root == null) continue;
                //删除所有注释
                if (root.SelectNodes("//comment()") != null)
                    foreach (var node in root.SelectNodes("//comment()"))
                        node.RemoveAll();

                f.name = strXPATH(getxpath_title(root));
                if (f.name.Length < 1)
                {
                    continue;
                }
                f.people = strXPATH(getxpath_people(root));
                f.score = Convert.ToDouble(strXPATH(getxpath_score(root))) ;
                Console.Write("");
                read.Add(f);
                /*
                 string context = "";
                  if (mb != null)
                 { 
                     foreach (Match m in mb)
                     {
                         if (m.Success)
                         {
                            context += m.Groups[1].Value;
                         }
                     }
                 }

                 WebClient client = new WebClient();
                 client.Proxy.Credentials = CredentialCache.DefaultCredentials;

                 //添加日期
                 mb = RegexHelper.GetRegex(finishHtml[i], "http://bj.huatu.com/([0-9]+)/([0-9]+)/([0-9]+).html");
                 int year=0, month=0, day=0,id=0;
                 DateTime time;
                 if (mb != null)
                 {
                     foreach (Match m in mb)
                     {
                         if (m.Success)
                         {
                             year = Convert.ToInt32(m.Groups[1].Value);
                             int c = Convert.ToInt32(m.Groups[2].Value);
                             month = c / 100;
                             day = c % 100;
                             id = Convert.ToInt32(m.Groups[3].Value);
                         }
                     }
                 }
                 if (year == 0 && month == 0 && day == 0) continue;
                  a = getxpath_title(root);
                 lv = strXPATH(a);

                 try
                 {
                     client.DownloadFile(context, @"E:\Script\c++应用程序\仙女楼 - 副本\My蜘蛛爬虫---爬取追书神器 2.0\My蜘蛛爬虫\bin\Debug\1\" + year + "-" + month + "-" + day + "-" + id + "-" + lv + ".xlsx");
                 }
                 catch (ArgumentException ex)
                 { Console.WriteLine("失败 -1"); }
                 finally { Console.WriteLine("成功 +1"); }
                if (context.Length > 20)
                {
                    u = RegexHelper.GetRegex(context, @"<.*?>");
                    if (u != null)
                    {
                        foreach (Match m in u)
                        {
                            if (m.Success)
                            {
                                context = context.Replace(m.Groups[0].Value, "");
                            }
                        }
                    }

                }
                IOHelper.writebook(titles, context);   */
                Thread.Sleep(30);
            }return read;
        }

        private static string strXPATH(HtmlNode node)
        {
            string str = "";
            if (node != null)
            {
                string s = node.InnerHtml;
                if (s.Length > 0)
                {
                    foreach (char c in s)
                    {
                        if (c != '\r' && c != ' ' && c != '\n' && c != '\t')
                            str += c;
                    }
                }
            }
            return str;
        }

        /// <summary>
        /// 获得观看人数
        /// </summary>
        /// <param name="root"></param>
        /// <returns></returns>
        private HtmlNode getxpath_people(HtmlNode root)
        {
            return root.SelectSingleNode(@"/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/span[2]/em");
        }
        /// <summary>
        /// 获得观看人数
        /// </summary>
        /// <param name="root"></param>
        /// <returns></returns>
        private HtmlNode getxpath_score(HtmlNode root)
        {
            return root.SelectSingleNode(@"/ html / body / div / div[1]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]");
        }
        /// <summary>
        /// 获得标题
        /// </summary>
        /// <param name="root"></param>
        /// <returns></returns>
        private HtmlNode getxpath_title(HtmlNode root)
        { 
            return root.SelectSingleNode(@"/html/body/div/div[1]/div[2]/div/div[2]/div[1]/span[1]");
        }

        /// <summary>
        /// 读取文档
        /// </summary>
        private void LoadTxt()
        {
            List<string> save = new List<string>(), history = new List<string>();
            save.AddRange(IOHelper.readTXT("save.txt"));
            history.AddRange(IOHelper.readTXT("history.txt"));
            
            foreach (string s in history )
                Crawlers.history_visited.Add(s);
            for (int ll = 0; ll < save.Count; ll++)
            {
                string s = save[ll];
                if (Crawlers.history_visited.Contains(save[ll]))
                    continue;
                if (save[ll].Length < 5) continue;
           /*     if (!save[ll].Contains(@"http://www.xiannvlou.com/"))
                {
                    continue;
                }*/
                if (Crawlers.Working.Count < Crawlers.maxurl * 2)
                    Crawlers.Working.Enqueue(save[ll]);
                else
                    NORead.Add(save[ll]);
            }
        }
    }
}   