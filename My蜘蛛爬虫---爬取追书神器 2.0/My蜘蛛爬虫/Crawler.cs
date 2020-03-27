using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading;
using System.Threading.Tasks;

namespace My蜘蛛爬虫
{
    public enum CrawlerType
    {
        suspend,
        working,
        downing
    }

    public class Crawlers
    {
        //单个爬虫最大网页数目
        public static int maxurl = 1000;
        //基地址
        public static Uri baseUri;
        //基主机
        public static string baseHost = string.Empty;
        /// <summary>
        /// 工作队列
        /// </summary>
        public static Queue<string> Working = new Queue<string>();
        /// <summary>
        /// 已访问且未解决的队列
        /// </summary>
        public static HashSet<string> visited = new HashSet<string>();
        /// <summary>
        /// 已访问的历史纪录
        /// </summary>
        public static HashSet<string> history_visited = new HashSet<string>();
        /// <summary>
        /// 初始化爬虫
        /// </summary>
        /// <param name="url"></param>
        public Crawlers(string url)
        {
            if (url != "")
            {
                baseUri = new Uri("https://www.bilibili.com/");
                //基域
                baseHost = baseUri.Host.Substring(baseUri.Host.IndexOf('.'));
                //抓取首地址入队
                Working.Enqueue(url);
            }
            visited.Clear();
        }

        /// <summary>
        /// 提取Url
        /// </summary>
        /// <param name="html"></param>
        public void RefineUrl(string html)
        {
          MatchCollection mc=    RegexHelper.GetRegex(html,@"(?is)<a[^>]*?href=(['""]?)(?<url>[^'""\s>]+)\1[^>]*>(?<text>(?:(?!</?a\b).)*)</a>");
            foreach (Match m in mc)
            {
                string url = m.Groups["url"].Value;
                if (url == "#")
                    continue;
                //相对路径转换为绝对路径
                Uri uri = new Uri(baseUri, url);
                //剔除外网链接(获取顶级域名)
                if (!uri.Host.EndsWith(baseHost))
                    continue;
                if (!visited.Contains(uri.ToString()))
                {
                    Working.Enqueue(uri.ToString());
                }
            }
        }
        /// <summary>
        /// 搜索网址
        /// </summary>
        public void DownLoad()
        {
            while (Working.Count > 0 && visited.Count < maxurl)
            {
                string currentUrl = Working.Dequeue();
                if (history_visited.Contains(currentUrl)) continue;
                //当前url标记为已访问过
                visited.Add(currentUrl);
                history_visited.Add(currentUrl);
                try
                {
                    HttpWebRequest request = WebRequest.Create(currentUrl) as HttpWebRequest;
                    HttpWebResponse response = request.GetResponse() as HttpWebResponse;
                    StreamReader sr = new StreamReader(response.GetResponseStream());
                    //提取url，将未访问的放入todo表中
                    RefineUrl(sr.ReadToEnd());
                    Thread.Sleep(30);
                }
                catch (WebException ex)
                {
                    if (ex.Message.IndexOf("404") != -1)
                    {
                        history_visited.Remove(currentUrl);
                        visited.Remove(currentUrl);
                        string str = currentUrl.Remove(0, (@"https://www.bilibili.com/").Length);
                        if (Regex.IsMatch(str, "[a-zA-Z]"))
                            Working.Enqueue(currentUrl);
                        else
                            Console.WriteLine(String.Format("url:{0}", currentUrl));

                        Console.WriteLine(String.Format("url:{0}  {1}", currentUrl, ex.ToString()));
                    }
                    else
                    {
                        continue;
                    }
                }
                catch { continue; }
                print(visited.Count);
            }
        }
        private void print(int m)
        {
            Console.Clear();
            Console.WriteLine("正在分析中");
            int mid = (int)((m) * 100.0 / maxurl);
            Console.Write("[");
            for (int i = 0; i < mid; i++)
                Console.Write("*");
            for (int i = mid; i < 100; i++)
                Console.Write(" ");
            Console.Write("] {0}/{1}   得到{2}/{3}", m, maxurl, visited.Count, Working.Count);
            Console.WriteLine();
        }
    }

    public struct CrawleHistroy
    {
        public string Url { get; set; }
        /// <summary>
        /// 最后一次访问记录
        /// </summary>
        public DateTime Timestamp { get; set; }
        public long Size { get; set; }
    }
}