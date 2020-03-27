using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace My蜘蛛爬虫
{
    class IOHelper
    {
        public static Collection<string> readTXT(string filename)
        {
            Collection<string> array = new Collection<string>();
            if (!File.Exists(filename))
                File.Create(filename);
            else
                using (StreamReader sr = new StreamReader(filename, Encoding.Default))
                {
                    string s;
                    while ((s = sr.ReadLine()) != null)
                    {
                        if (s != string.Empty)
                            array.Add(s);
                    }
                }

            return array;
        }

        //默认覆盖文件
        public static bool writeTXT(string filename, string[] array, bool append = false)
        {
            using (StreamWriter sw = new StreamWriter(filename, append, Encoding.Default))
            {
                for (int i = 0; i < array.Length; i++)
                {
                    if (array[i] != null)
                        if (array[i].Length > 5)
                            sw.WriteLine(array[i]);
                }
            }
            return true;
        }
        //默认覆盖文件
        public static bool writeTXT(string filename, film[] array, bool append = false)
        {
            append = true;
            using (StreamWriter sw = new StreamWriter(filename, append, Encoding.Default))
            {
                for (int i = 0; i < array.Length; i++)
                {
                    if (array[i] != null)
                        if (array[i].name.Length > 0)
                            sw.WriteLine(array[i].name+" "+array[i].url+" "+array[i].people+ " "+array[i].score );
                }
            }
            return true;
        }

        //
        public static bool writebook(string title, string body)
        {        ///默认覆盖文件
            title = title.Replace("/", "");
            title = title.Replace("-", "");
            title = title.Replace("?","");
            title = title.Replace("\\", "");

            using (StreamWriter sw = new StreamWriter("1//" + title + ".txt", false, Encoding.Default))
            {
                if (body.Length > 5)
                    sw.WriteLine(body);
            }
            return true;
        }
    }
}