using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace My蜘蛛爬虫
{
    ////////////数据库帮助类//////////////////////////////////////////////////
    //2018/1/1
    //2018/2/4 修改：【新增 测试方法：测试新建数据库->新建表->删除表->删除数据库】
    ////////////////////////////////////////////////////////////////////////////

    class SQLhelper
    {
        /// <summary>
        /// 连接词
        /// </summary>
        private  static SqlConnection conn = new SqlConnection ( @"Data Source = LAPTOP-V3FES89C\SQLEXPRESS; Initial Catalog = read; Integrated Security = SSPI");
        public static  bool OPEN()
        {
            try { conn.Open(); return true; }
            catch (SqlException ex)
            {
                Console.WriteLine(ex.ToString());
                return false;
            }
        }
        public static int ExecuteNonQuery(string sql)
        {
            try
            {       
                SqlCommand cmd = new SqlCommand(sql, conn);
                return cmd.ExecuteNonQuery();
            }
            catch (SqlException ex)
            {
                Console.WriteLine(ex.ToString());
                return -1;
            }
        }
        public static SqlDataReader SQLDataReader(string sql)
        {
           
            try
            { 
                SqlCommand cmd = new SqlCommand(sql, conn);
                return cmd.ExecuteReader();
            }
            catch (SqlException ex)
            {
                Console.WriteLine(ex.ToString());
                return null;
            }
        }
        public static void SQLExit()
        {
            conn.Close();
        }
    }
}