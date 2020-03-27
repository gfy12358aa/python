using HtmlAgilityPack;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace My蜘蛛爬虫
{
    public static class HTMLHELPER
    {
        /// <summary>
        /// 获取html文档
        /// </summary>
        /// <param name="html"></param>
        /// <returns></returns>
        public static string GetHtml(string html, int deep = 0)
        {
            try
            {
                HttpWebRequest re = WebRequest.Create(html) as HttpWebRequest;
                HttpWebResponse r = re.GetResponse() as HttpWebResponse;

                StreamReader stream = new  StreamReader (r.GetResponseStream(),Encoding.GetEncoding("utf-8"));
                return stream .ReadToEnd();
            }
            catch (WebException ex)
            {
                if (ex.Message.IndexOf("404") != -1 && deep < 3) return GetHtml(html, deep + 1);
                return null;
            }
        }


        /// <summary>
        /// 获取满足xpath的第一个节点
        /// </summary>
        /// <param name="node"></param>
        /// <param name="xPath"></param>
        /// <returns></returns>
        public static HtmlNode getHtmlNode(HtmlNode node, string xPath)
        {
            return node.SelectSingleNode(xPath);
        }

        public static HtmlNodeCollection getHtmlNodes(HtmlNode node, string xPath)
        {
            return node.SelectNodes(xPath);
        }
        public static bool SaveBit(string webhtml, string filename, int deep = 0)
        {
            int i = Directory.GetFiles(filename).Length;
            int p = i;
            try
            {
                WebClient wc = new WebClient();
                string ima = filename + @"\" + p + ".jpg";

                if (!Directory.Exists(filename))
                {
                    Directory.CreateDirectory(filename);
                }
                wc.DownloadFile(webhtml, ima);
                return true;
            }

            catch (WebException ex)
            {
                if (ex.Message.IndexOf("404") != -1 && deep < 3)
                    return SaveBit(webhtml, filename, deep + 1);
                return false;
            }

        }

        /// <summary>
        /// 下载文档
        /// </summary>
        /// <param name="web"></param>
        /// <param name="deep"></param>
        /// <returns></returns>
        public static bool SaveWrite(HtmlNode node, int deep = 0)
        {
            if (!File.Exists(@"E:\1\1.txt"))
                File.Create(@"E:\1\1.txt");
            StreamWriter sw = new StreamWriter(@"E:\1\1.txt", true, Encoding.UTF8);
            HtmlNodeCollection nodes = getHtmlNodes(node, "//*[@id=\"QuestionAnswers-answers\"]/div/div/div/div/div/div/div/span/p");
            if (nodes != null)
                foreach (HtmlNode n in nodes)
                {
                    if (n != null)
                    {
                        sw.WriteLine(n.InnerHtml);
                    }
                }
            sw.Close();
            return true;
        }
    }
}