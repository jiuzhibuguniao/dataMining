#include<iostream>
#include<vector>
#include<string>
#include<ctime>
#include<fstream>
#include<algorithm>
#include<numeric>
#define PI 3.141592653

using namespace std; using std::vector; using std::string; using std::fstream;

typedef unsigned int uint;

//函数random生成a-b之间的随机数
int random(int a, int b)
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
double distance(vector<double> ivec1, vector<double> ivec2)
{
	double Lat1 = rad(ivec1[1]);
	double Lat2 = rad(ivec2[1]);
	double a = Lat1 - Lat2;
	double b = rad(ivec1[0]) - rad(ivec2[0]);
	double s = 2 * asin(sqrt(pow(sin(a / 2), 2) + cos(Lat1)*cos(Lat2)*pow(sin(b / 2), 2)));
	s = s * 6378137;
	return s;
}

struct Cluster
{
	vector<double> centerid;
	vector<size_t> samples;
};


//k-means聚类函数
vector<Cluster> k_means(vector<vector<double>> trainX, uint k, uint maxepoches)
{
	const uint row_num = trainX.size();
	const uint col_num = trainX[0].size();

	//初始化聚类，选取K个聚类中心点
	vector<Cluster> clusters(k);
	uint seed = (uint)time(NULL);
	for (uint i = 0; i<k; i++)
	{
		srand(seed);
		int c = rand() % row_num;
		clusters[i].centerid = trainX[c];
		seed = rand();
	}

	//多次迭代直至收敛，本次试验迭代1000次
	for (uint it = 0; it<maxepoches; it++)
	{
		//每一次重新计算样本点所属类别之前，清空原来样本
		for (uint i = 0; i<k; i++)
		{
			clusters[i].samples.clear();
		}

		//求出每个样本点距应该属于哪一个聚类
		for (uint j = 0; j<row_num; j++)
		{
			//都初始化属于第0个聚类
			uint c = 0;
			double min_distance = distance(trainX[j], clusters[c].centerid);
			for (uint i = 1; i<k; i++)
			{
				double distances = distance(trainX[j], clusters[i].centerid);
				if (distances<min_distance)
				{
					min_distance = distances;
					c = i;
				}
			}
			clusters[c].samples.push_back(j);
		}
		//更新聚类中心
		for (uint i = 0; i<k; i++)
		{
			vector<double> val(col_num, 0.0);
			for (uint j = 0; j<clusters[i].samples.size(); j++)
			{
				uint sample = clusters[i].samples[j];
				for (uint d = 0; d<col_num; d++)
				{
					val[d] += trainX[sample][d];
					if (j == clusters[i].samples.size() - 1)
					{
						clusters[i].centerid[d] = val[d] / clusters[i].samples.size();
					}
				}
			}
		}
	}
	return clusters;
}


//读取文件函数
vector<vector<double>> f_input()
{
	vector<vector<double>> ivec(30557);  //储存所有摩拜单车的经纬度
	double longitude;                    //单车的经度
	double latitude;                     //单车的维度
	ifstream input;                      //读取文件内容

	input.open("C:\\Users\\Rooobins\\Desktop\\DataXXYY.txt", fstream::in);

	if (!input.is_open())
	{
		cerr << "OPEN FILE ERROR!" << endl;
	}
	else
	{
		for (size_t i = 0; i != 30557; ++i)
		{
			input >> longitude >> latitude;
			ivec[i].push_back(longitude);
			ivec[i].push_back(latitude);
		}
	}

	input.close();

	return ivec;
}

//主函数
int main()
{
	vector<vector<double>> ivecii;
	ivecii = f_input();
	k_means(ivecii, 300, 1);
	system("pause");
}