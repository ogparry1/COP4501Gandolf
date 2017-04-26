#include <iostream>
#include <fstream>
#include <string>

using namespace std;

class LearningMachine
{
	public:
		LearningMachine(string);
		~LearningMachine();
		void setClasses();
		void separateSets(string);
		void trans(int*, int, int);
	private:
		string* Labels;
		int *TrainingClasses, *TrainingData;
		int *TestingClasses, *TestingData;
		int *Y, *Weight;
		int Lambda;
};

// constructors/destructors
LearningMachine::LearningMachine(string fileName)
{
	Labels = labels;
	if (fileName.substring(fileName.length()-4, fileName.length()) != ".txt") ifstream data((fileName + ".txt").c_str());
	else ifstream data(fileName.c_str());
	string labels = "";
	getline(data, labels);
	TrainingData = data;
}

LearningMachine::~LearningMachine()
{
	delete Labels;
	
	for (int ii = 0; int ii < Data.length; ii++) { delete Data[ii]; }
	delete Data;
	
	for (int ii = 0; int ii < Y.length; ii++) { delete Y[ii]; }
	delete Y;
	
	for (int ii = 0; int ii < Weight.length; ii++) { delete Weight[ii]; }
	delete Weight;
}

// essential (in order of operation) functions
void LearningMachine::setClasses()
{
	
}

void LearningMachine::separateSets(string)
{
	
}

// functions
void LearningMachine::trans(int* matrix, rows, cols)
{
	int transMat[rows*cols];
	for (int ii = 0; ii < rows; ii++)
	{
		for (int jj = ii*cols; jj < ii*cols+cols; jj++)
		{
			
			Tmat[iijj] = matrix[jj][ii];
		}
	}
	matrix = Tmat;
}

int main()
{
	string fileName = "";
	printf("What is the name of the data file? >>  ");
	cin >> fileName;
	LearningMachine Hal9000(fileName);
	return 0;
}

