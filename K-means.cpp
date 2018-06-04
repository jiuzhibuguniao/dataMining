#include<iostream>
#include<string>
#include<vector>
#include<ctime>
#include<fstream>
#include<algorithm>
#include<numeric>

#define PI 3.151592653


using namespace std;
using std::vector;
using std::string;
using std::fstream;



//函数random生成a-b之间的随机数
int random(int a,int b)
{
	int dis = b - a;
	return rand() % dis + a;
}


//函数rad转度数为弧度
double rad(double a)
{
	return a * PI / 180;
}



//函数distance计算两个经纬度之间的距离
double distance(double longitude1, double latitude1, double longitude2, double latitude2)
{
	double Lat1 = rad(latitude1);
	double Lat2 = rad(latitude2);
	double a = Lat1 - Lat2;
	double b = rad(longitude1) - rad(longitude2);
	double s = 2 * asin(sqrt(pow(sin(a / 2), 2) + cos(Lat1)*cos(Lat2)*pow(sin(b / 2), 2)));
	s = s * 6378137;
	return s;
}



//主函数
int main()
{
 
	ifstream input;                    //读取文件信息
	ofstream output;                   //输出文件信息
	double longistude;                 //共享单车经度
	double latitude;                   //共享单车维度
	vector<double> ivecii;             //暂存每辆单车的经纬度信息
	vector<vector<double>> ivec;       //储存所有单车的经纬度
	vector<int> position;              //储存随机生成的位置点
	vector<vector<vector<double>>> end(500);   //选择生成500个区域

	vector<double>  result;            //储存每个点到所选所有位置点的距离


	vector<double> longistudei;        //储存某个区域所有的经度
	vector<double> latitudei;          //储存某个区域所有的维度


	double a;                          //
	double b;                          //






	input.open("C:\\Users\\Rooobins\\Desktop\\DataXXYY.txt", fstream::in);
	

	//读取每辆单车的位置信息并储存
	if (!input.is_open())
	{
		cout << "Open file error!" << endl;
	}
	else
	{
		for (int i = 0; i != 30557; ++i)
		{
			input >> longistude >> latitude;
			ivecii.push_back(longistude);
			ivecii.push_back(latitude);
			ivec.push_back(ivecii);
			ivecii.clear();
		}
	}
	input.close();


    //生成500个区域的初始位置点
	for (int i = 0; i != 500; ++i)
	{
		position.push_back(random(0, ivec.size()));
	}

	


	for (auto i = 0; i != ivec.size(); ++i)
	{
		for (auto j = 0; j != position.size(); ++j)
		{
			
             result.push_back(distance(ivec[i][0],ivec[i][1],ivec[position[j]][0],ivec[position[j]][1]));
		}

		auto MIN=min_element(result.begin(),result.end());
		int P=*MIN-result.begin();
		end[P].push_back(ivec[i]);
	}


	for(auto i=0;i!=end.size();++i)
	{
		double a1=0;
		double b1=0;
		for(auto j=0;j!=end[i].size();++j)
		{
			a1+=end[i][j][0];
			b1++end[i][j][1];
		}
	}

	system("pause");
}