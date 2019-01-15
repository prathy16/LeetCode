// Using min-max heap
// priority_queue<int> => max heap
// priority_queue<int, vector<int>, greater<int>> => min heap

#include<iostream>
#include<queue>
#include<vector>

using namespace std;

vector<double> runningtimeMedian(vector<int>& A){
  vector<double> res;
  priority_queue<int, vector<int>, greater<int>> min_heap;
  priority_queue<int> max_heap;

  double median = 0;

  for(int i=0; i < A.size(); i++){
    if(A[i] <= median){
      max_heap.push(A[i]);
    }
    else{
      min_heap.push(A[i]);
    }

    if(min_heap.size() > max_heap.size()+1){
      max_heap.push(min_heap.top());
      min_heap.pop();
    }
    else if(max_heap.size() > min_heap.size()+1){
      min_heap.push(max_heap.top());
      max_heap.pop();
    }

    if(min_heap.size() == max_heap.size()){
      median = (min_heap.top() + max_heap.top())/2.0;
    }
    else if(min_heap.size() > max_heap.size()){
      median = min_heap.top();
    }
    else if(max_heap.size() > min_heap.size()){
      median = max_heap.top();
    }

    res.push_back(median);
  }

  return res;
}

int main()
{
  vector<int> A = {1, 2, 3, 4, 5};
  vector<double> median = runningtimeMedian(A);

  for(double d: median){
    cout << d << " ";
  }

  return 0;
}
