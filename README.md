# voyage segmentation based on K-means algorithm
## AwesomeProject
This project uses the navigation data of a bulk carrier to divide the ship's navigation segments using the K-means algorithm, providing a solution for optimizing the ship's energy efficiency by reasonably reducing the optimization frequency and considering the impact of sea conditions on energy consumption.
## Highlights
- ✅ Provide a dataset of bulk carrier voyage data for open-source use.
- ✅ Classify sea conditions based on wind direction, wind speed, and current velocity from the voyage data.
- ✅ Determine the optimal number of clusters using the elbow method.
- ✅ Segment the vessel’s voyage based on the established sea condition classification.
## Data
The data was collected from sensors on the ocean-going training vessel Yuming, affiliated with Shanghai Maritime University, IMO: 9613886.
## Structure
The root folder contains the following subfolders and files.
- **data:** This folder contains raw, interim and processed datasets used in this project, in csv format.
- **data_index.py:** The code loads a CSV file, cleans and renames columns, standardizes the time format, and saves the processed data to a new CSV file.
- **data_processing.py:** The code processes a dataset by standardizing latitude/longitude, converting units, filtering out abnormal values, removing unnecessary columns, reordering columns, and saving the final data to a new CSV file.
- **determine_the_number_of_clusters.py:** The code uses the Elbow method to determine the optimal number of clusters for K-Means clustering and plots the relationship between SSE and the number of clusters.

<p align="center">
  <img src="https://github.com/ZXXXXXYY/voyage-segmentation-based-on-K-means-algorithm/blob/main/images/Fig.1.SSE%20curve%20for%20cluster%20number%20selection%20using%20the%20elbow%20method.jpg" alt="项目图片2" width="400" />
</p>

- **sea_condition_clustering.py:** The code performs K-Means clustering to divide the data into 6 sea condition categories and plots 3D scatter plots with cluster labels and cluster centers.

<p align="center">
  <img src="https://github.com/ZXXXXXYY/voyage-segmentation-based-on-K-means-algorithm/blob/main/images/Fig.2.a.Clustered%20navigation%20data%20by%20sea%20condition%20features.jpg" alt="项目图片1" width="260" />
  <img src="https://github.com/ZXXXXXYY/voyage-segmentation-based-on-K-means-algorithm/blob/main/images/Fig.2.b.Cluster%20centers.jpg" alt="项目图片2" width="260" />
</p>

- **voyage_segmentation.py:** The code segments the voyage based on sea condition types and displays the ship's trajectory on two maps: one with sea condition classifications and the other without.

<p align="center">
  <img src="https://github.com/ZXXXXXYY/voyage-segmentation-based-on-K-means-algorithm/blob/main/images/Fig.3.a.Navigation%20route.jpg" alt="项目图片1" width="230" />
  <img src="https://github.com/ZXXXXXYY/voyage-segmentation-based-on-K-means-algorithm/blob/main/images/Fig.3.b.Voyage%20segmentation%20by%20sea%20conditions.jpg" alt="项目图片2" width="230" />
</p>

## Conclusions
- Achieved basic data processing.
- Used the elbow method to classify sea conditions into six categories.
- Applied the K-means algorithm to divide the vessel's operational conditions into six categories.
- Divided the voyage into eight segments based on the defined sea condition classifications.
## Shortcoming
- Due to the wind direction range being 0-360°, both 0° and 360° represent the same direction (north). However, since the K-means clustering algorithm calculates the distance of data points from the cluster center based on Euclidean distance, it inadvertently amplifies the difference between 0° and 360°, leading to an unreasonable calculation of SSE (Sum of Squared Errors). This, in turn, affects the determination of the optimal number of clusters.
- It can be observed from the segmentation results of the 'voyage_segmentation.py' file that some segments are mixed with different sea conditions, which increases the complexity of segmentation.
## Attention
- To address the first issue mentioned in the above shortcomings, this project, when using the elbow method to determine the optimal number of clusters, ignores the sharp drop in SSE caused by the transition from 360° to 0° in wind direction (i.e., the change between K=2 and K=3). The choice of K=6 as the number of clusters was based on the subjective judgment of the project owner and may not be entirely reasonable. If there are suggestions for improvement, we welcome participation in the extension and modification of this project or contact with the author.
- To address the second issue mentioned in the above shortcomings, delete certain data points from different sea conditions based on their proportion in the voyage. The deleted data is saved in the file '05-YuMing_final_processed_with_clusters.CSV' located in the 'data' folder.
## Contact Details
- Email: xinyuezhang1117@163.com
- Wechat： awordzxy

==============================================
# 基于K-means算法的海况聚类与航程划分

## 项目简介
本项目使用散货船的航行数据，通过K-means算法对船舶的航行海况进行分类，随后根据海况类型对航程进行划分，提供了一种通过合理降低优化频率并考虑海洋条件对能耗影响的方式来优化船舶能效的解决方案。

## 项目亮点
- ✅ 提供开源使用的散货船航行数据集。
- ✅ 根据航程数据中的风向、风速和水流对航程中的海况条件进行分类。
- ✅ 使用肘部法则确定聚类的最佳数量。
- ✅ 基于已建立的海况条件分类对船舶航程进行划分。

## 数据
数据来自上海海事大学附属的远洋实训船“育明”号，IMO编号：9613886。

## 文件结构
根文件夹包含以下子文件夹和文件：
- **data**：此文件夹包含本项目中使用的原始数据、中间数据和处理后的数据，格式为csv。
- **data_index.py**：此代码用于加载CSV文件、清理和重命名列、标准化时间格式，并将处理后的数据保存为新的CSV文件。
- **data_processing.py**：此代码通过标准化经纬度、单位转换、过滤异常值、删除不必要的列、重新排序列，并将最终数据保存为新的CSV文件来处理数据集。
- **determine_the_number_of_clusters.py**：此代码使用肘部法则确定K-means聚类的最佳簇数，并绘制SSE与簇数之间的关系图。

<p align="center">
  <img src="https://github.com/ZXXXXXYY/voyage-segmentation-based-on-K-means-algorithm/blob/main/images/Fig.1.SSE%20curve%20for%20cluster%20number%20selection%20using%20the%20elbow%20method.jpg" alt="项目图片2" width="400" />
</p>

- **sea_condition_clustering.py**：此代码执行K-means聚类，将数据划分为6个海况条件类别，并绘制带有聚类标签和聚类中心的3D散点图。

<p align="center">
  <img src="https://github.com/ZXXXXXYY/voyage-segmentation-based-on-K-means-algorithm/blob/main/images/Fig.2.a.Clustered%20navigation%20data%20by%20sea%20condition%20features.jpg" alt="项目图片1" width="260" />
  <img src="https://github.com/ZXXXXXYY/voyage-segmentation-based-on-K-means-algorithm/blob/main/images/Fig.2.b.Cluster%20centers.jpg" alt="项目图片2" width="260" />
</p>

- **voyage_segmentation.py**：此代码根据海况条件类型对航程进行划分，并在两张地图上显示船舶轨迹：一张带有海洋条件分类，另一张不带分类。

<p align="center">
  <img src="https://github.com/ZXXXXXYY/voyage-segmentation-based-on-K-means-algorithm/blob/main/images/Fig.3.a.Navigation%20route.jpg" alt="项目图片1" width="230" />
  <img src="https://github.com/ZXXXXXYY/voyage-segmentation-based-on-K-means-algorithm/blob/main/images/Fig.3.b.Voyage%20segmentation%20by%20sea%20conditions.jpg" alt="项目图片2" width="230" />
</p>

## 结论
- 完成了基本数据处理。
- 使用肘部法则将海洋条件划分为六类。
- 应用K-means算法将船舶的运营条件划分为六类。
- 根据定义的海洋条件分类将航程划分为八个段落。

## 不足之处
- 由于风向的范围为0°到360°，0°和360°表示相同的方向（北）。然而，由于K-means聚类算法基于欧几里得距离计算数据点到聚类中心的距离，它无意中放大了0°和360°之间的差异，导致SSE（平方误差和）计算不合理，从而影响了最佳聚类数量的确定。
- 从`voyage_segmentation.py`文件的航程划分结果可以观察到，某些段航段参杂了不同的海况条件，增加了划分的复杂性。

## 注意事项
- 针对上述不足中的第一个问题，在使用肘部法则确定最佳聚类数量时，本项目忽略了由风向从360°过渡到0°造成的SSE急剧下降（即K=2到K=3之间的变化）。选择K=6作为聚类数是项目所有者的主观判断，可能并不完全合理。如果有改进建议，欢迎参与该项目的扩展和修改，或与作者联系。
- 针对上述不足中的第二个问题，根据海洋条件在航程中的比例删除某些来自不同海洋条件的数据点。删除的数据保存在`data`文件夹中的`05-YuMing_final_processed_with_clusters.CSV`文件中。

## 联系方式
- 邮箱：xinyuezhang1117@163.com
- 微信：awordzxy

