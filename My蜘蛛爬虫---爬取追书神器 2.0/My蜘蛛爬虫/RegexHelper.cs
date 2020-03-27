using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace My蜘蛛爬虫
{
    class RegexHelper
    {
        public static MatchCollection GetRegex(string str,string regex)
        {
            Regex reg = new Regex(regex);
           return reg.Matches(str);
        }
    }
}
