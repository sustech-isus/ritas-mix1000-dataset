# RITAS-Mix1000 数据集 / RITAS-Mix1000 Dataset

RITAS-Mix1000 数据集是南方科技大学斯发基斯可信自主系统研究院（Research Institute of Trustworthy Autonomous Systems, Southern University of Science and Technology）设计面向自动驾驶的难例情况仿真数据集。

RITAS-Mix1000 is a simulation-based difficult-scenario dataset for autonomous driving, developed by the Research Institute of Trustworthy Autonomous Systems (RITAS), Southern University of Science and Technology (SUSTech).

<table>
<tr>
<td><img src="misc/1_EnvNight_CameraNoise(CAM_F)_CaseWrongWayBike.gif" width="100%"></td>
<td><img src="misc/1_EnvNight_CaseLongCargoMany.gif" width="100%"></td>
</tr>
<tr>
<td><img src="misc/1_EnvNoon_CaseHighwayMissExit.gif" width="100%"></td>
<td><img src="misc/1_EnvNoon_RoadFlodding_CaseVehicleDartOut.gif" width="100%"></td>
</tr>
<tr>
<td><img src="misc/1_EnvSunset_CaseFrontAeb.gif" width="100%"></td>
<td><img src="misc/1_EnvSunset_CaseRuntimeObstacle.gif" width="100%"></td>
</tr>
</table>

数据集使用 CARLA 作为基本仿真环境，以自动驾驶行业通用的 nuScence 格式输出。该数据集包含了 26 种难例天气情形、13 种传感器异常情形、18 种难例交通场景，并选取其中对自动驾驶系统影响最为显著的 1300 余种组合采集构建了完整的数据集。

The dataset is generated using CARLA as the underlying simulation platform and exported in the nuScenes-compatible format, widely adopted in the autonomous-driving community. It includes 26 types of adverse weather, 13 sensor-fault conditions, and 18 challenging traffic scenarios. From these, more than 1,300 high-impact scenario combinations were selected and recorded to construct the full dataset.

目前，采集车辆（EGO VEHICLE / HERO）使用 CARLA TrafficManager AutoPilot 进行行动，具备基本的行进间避障能力，该工作后续将会引入 Autoware / E2E / VLA 模型提供更加符合真实自动驾驶车辆的运行行为。

At the current stage, the ego vehicle (EGO / HERO) operates using CARLA TrafficManager AutoPilot, providing basic obstacle-avoidance capabilities during navigation. Future iterations will integrate Autoware, end-to-end (E2E) models, and Vision-Language-Action (VLA) models to produce driving behaviors that more closely reflect real autonomous vehicles.

> **💡 NOTICE**
> 
> 目前该数据集处在早期工程阶段（Develop Alpha），数据集的组合方式、数据结构可能会随项目推进而变更。
>
> This dataset is currently in the early engineering stage (Develop Alpha). Both the scenario-combination strategy and the dataset structure may evolve as the project progresses.

## 下载与使用 / Download and Usage

为了便利使用，我们将每条数据打包为了 `.7z` 文件, 您可以按需下载。完整数据集清单详见 [此处](./LIST.md)。

For ease of use, each sample is packaged as a .7z archive, and you may download only the items you need. The complete dataset index is available [here](./LIST.md).

采集车辆（EGO VEHICLE / HERO）按照与 nuScence 数据集一致的方式配置，包含 6 个针孔相机组成的环视相机组和 1 个位于车顶部的 128 线激光雷达。

The ego vehicle (EGO / HERO) follows the same sensor configuration as the nuScenes dataset, featuring a six-camera surround-view rig with pinhole models and a roof-mounted 128-beam LiDAR.

## 包含内容 / Contents

数据集包含以下难例单因子的组合, 括号内为因子的名称以便于您在 [下载页](./LIST.md) 进行检索：

The dataset includes combinations of the following difficult single-factor conditions. The names in parentheses correspond to the identifiers used on the [download page](./LIST.md) for easy lookup:

### 难例天气与光照 - 26 / Adverse Weather and Lighting Conditions - 26

| 名称<br>Name | 说明<br>Description | 相机影响<br>Camera Impact | 激光雷达影响<br>LiDAR Impact | 车辆控制影响<br>Vehicle Control Impact |
|----|----|------|--------|--------|
| EnvNoon_HeavyRain | 昼间暴雨<br>Noon heavy rain | + |  |  |
| EnvNoon_RoadFlodding | 昼间路面大量积水<br>Noon road flooding | + |  |  |
| EnvNoon_HeavyRain_RoadFlodding | 昼间暴雨且路面大量积水<br>Noon heavy rain with road flooding | ++ |  |  |
| EnvNoon_MediumFog | 昼间中等雾<br>Noon medium fog | + | + |        |
| EnvNoon_HeavyFog | 昼间浓雾<br>Noon heavy fog | ++ | ++ |        |
| EnvNoon_DustStorm | 昼间沙尘暴, 重度影响激光雷达<br>Noon dust storm, severely affects LiDAR | ++ | ++++ |        |
| EnvNoon_SuddenRain | 昼间突发暴雨<br>Noon sudden heavy rain | ++ |  |        |
| EnvNoon_RoadIceing | 昼间路面积冰<br>Noon road icing |  |  | + |
| EnvSunset_HeavyRain | 黄昏/清晨暴雨<br>Sunset/dawn heavy rain | ++ |  |  |
| EnvSunset_RoadFlodding | 黄昏/清晨路面大量积水<br>Sunset/dawn road flooding | ++ |  |  |
| EnvSunset_HeavyRain_RoadFlodding | 黄昏/清晨暴雨且路面大量积水<br>Sunset/dawn heavy rain with road flooding | +++ |  |  |
| EnvSunset_MediumFog | 黄昏/清晨中等雾<br>Sunset/dawn medium fog | ++ | + |  |
| EnvSunset_HeavyFog | 黄昏/清晨浓雾<br>Sunset/dawn heavy fog | +++ | ++ |  |
| EnvSunset_DustStorm | 黄昏/清晨沙尘暴, 重度影响激光雷达<br>Sunset/dawn dust storm, severely affects LiDAR | +++ | ++++ |  |
| EnvSunset_SuddenRain | 黄昏/清晨突发暴雨<br>Sunset/dawn sudden heavy rain | +++ |  |  |
| EnvSunset_RoadIceing | 黄昏/清晨路面积冰<br>Sunset/dawn road icing |  |  | + |
| EnvNight | 夜间低光照情形<br>Night low-light conditions | ++ |  |  |
| EnvNight_NoLight | 夜间低光照情形且无环境照明<br>Night low-light conditions without ambient lighting | +++ |  |  |
| EnvNight_HeavyRain | 夜间暴雨<br>Night heavy rain | +++ |  |  |
| EnvNight_RoadFlodding | 夜间路面大量积水<br>Night road flooding | +++ |  |  |
| EnvNight_HeavyRain_RoadFlodding | 夜间暴雨且路面大量积水<br>Night heavy rain with road flooding | ++++ |  |  |
| EnvNight_MediumFog | 夜间中等雾<br>Night medium fog | +++ | + |  |
| EnvNight_HeavyFog | 夜间浓雾<br>Night heavy fog | ++++ | ++ |  |
| EnvNight_DustStorm | 夜间沙尘暴, 重度影响激光雷达<br>Night dust storm, severely affects LiDAR | ++++ | ++++ |  |
| EnvNight_SuddenRain | 夜间突发暴雨<br>Night sudden heavy rain | ++++ |  |  |
| EnvNight_RoadIceing | 夜间路面积冰<br>Night road icing |  |  | + |

### 传感器缺陷因素 - 13 / Sensor Fault Conditions - 13

| 名称<br>Name | 说明<br>Description | 相机影响<br>Camera Impact | 激光雷达影响<br>LiDAR Impact |
|----|----|------|--------|
| SensorNoData | 传感器无数据<br>Sensor no data | +++ | +++ |
| SensorHeavyLost | 传感器传输丢帧, 且肉眼可见<br>Sensor heavy packet loss, visibly noticeable | +++ | +++ |
| SensorDelay | 传感器延迟造成错帧<br>Sensor delay causing frame misalignment | ++ | ++ |
| SensorCalibError | 传感器与原始标定不符, 常见于维修后的错误安装<br>Sensor calibration error, common after incorrect post-repair installation | ++ | ++ |
| CameraBrokenLines | 相机存在CMOS坏道<br>Camera CMOS dead pixels | ++ |  |
| CameraLostChannel | 相机丢失RGB通道中的一个<br>Camera lost one RGB channel | ++ |  |
| CameraBlur | 相机模糊, 常见于镜头失焦<br>Camera blur, common with lens defocus | ++ |  |
| CameraTrail | 相机拖滞, 常见于IPC算法参数错误<br>Camera trailing, common with IPC algorithm parameter errors | ++ |  |
| CameraNoise | 相机噪声, 常见于IPC算法参数错误或出于极暗环境<br>Camera noise, common with IPC algorithm parameter errors or extreme low-light conditions | + |  |
| CameraJelly | 相机果冻状拖影, 常见于扫描式快门相机, 但经过IPC处理<br>Camera jelly effect, common with rolling shutter cameras, post-IPC processed | ++ |  |
| CameraTera | 相机撕裂状拖影, 常见于扫描式快门相机, 未经过IPC处理<br>Camera tearing effect, common with rolling shutter cameras, unprocessed | ++ |  |
| LidarBlock | 雷达区域遮挡, 常见于雷达小于最小量程部分被遮挡<br>LiDAR partial occlusion, common when near-range areas are blocked |  | ++ |
| LidarRuntimeBlock | 雷达区域遮挡, 相比于 LidarBlock 呈现为动态状态<br>LiDAR dynamic occlusion, dynamic state compared to LidarBlock |  | ++ |

### 难例交通流与场景 - 18 / Challenging Traffic Flow and Scenarios - 18

| 名称<br>Name | 说明<br>Description | 场景<br>Scene |
|----|----|----|
| TrafficLargeVehicles | 全部由大车组成的车流, 高遮挡环境<br>Traffic flow entirely composed of large vehicles, high occlusion environment | 城市<br>Urban |
| TrafficTwoWheels | 由大量两轮车辆组成的车流, 低可检测目标<br>Traffic flow with many two-wheeled vehicles, low detectability targets | 城市<br>Urban |
| TrafficCrossRoad | 十字路口开放左转, 每次采集的车辆类型不同<br>Crossroad with open left turns, varying vehicle types per recording | 城市<br>Urban |
| CaseFrontAeb | 自车前车发生紧急制动<br>Front vehicle emergency braking | 城市/高速<br>Urban/Highway |
| CaseFrontAvoid | 自车前车发生紧急避让<br>Front vehicle emergency avoidance | 城市/高速<br>Urban/Highway |
| CaseForceCutin | 自车侧边车辆强行变道<br>Adjacent vehicle forced lane change | 城市/高速<br>Urban/Highway |
| CaseStaticObstacle | 道路抛洒物(大量纸箱)<br>Static road debris (many cardboard boxes) | 城市/高速<br>Urban/Highway |
| CaseRuntimeObstacle | 道路抛洒物, 由前方货车掉落<br>Dynamic road debris, dropped from front truck | 城市/高速<br>Urban/Highway |
| CaseSingleAccident | 前方单车静止事故, 可选是否有警示标志<br>Single-vehicle stationary accident ahead, optional warning signs | 城市/高速<br>Urban/Highway |
| CaseMultiAccident | 前方多车+行人事故, 可选是否有警示标志<br>Multi-vehicle and pedestrian accident ahead, optional warning signs | 城市/高速<br>Urban/Highway |
| CaseLongCargo | 前方车辆带有长杆货物<br>Front vehicle with long cargo | 城市/高速<br>Urban/Highway |
| CaseLongCargoMany | 前方车辆带有多个长杆货物<br>Front vehicle with multiple long cargo items | 城市/高速<br>Urban/Highway |
| CaseWrongWayBike | 逆行电动车<br>Wrong-way electric bike | 城市<br>Urban |
| CaseHighwayMissExit | 高速公路错过出口连续变道<br>Highway missed exit consecutive lane changes | 高速<br>Highway |
| CaseHighwayWrongWay | 高速公路逆行<br>Highway wrong-way driving | 高速<br>Highway |
| CaseRampWrongWay | 高速匝道逆行<br>Highway ramp wrong-way driving | 高速<br>Highway |
| CasePedestrianDartOut | 行人鬼探头<br>Pedestrian dart-out | 城市<br>Urban |
| CaseVehicleDartOut | 路边停车鬼探头<br>Parked vehicle dart-out | 城市<br>Urban |

## 高级 / Advanced

如果上述数据集无法满足您的要求，或者您有下文列出的需求，可以使用 HarzedScopeX 项目的 [ritas_mix1000 分支](https://github.com/ZHAO-ZIRUI/HazardScopeX/tree/ritas-mix1000) 进行二次开发:
- 期望使用自己的自动驾驶系统
- 期望导出为其他数据集格式
- 期望修改或增加特定场景
- 期望在特定场景下进行反复多次实验
- 期望包含真值数据

If the above dataset does not meet your requirements, or if you have any of the following needs, you can use the [ritas_mix1000 branch](https://github.com/ZHAO-ZIRUI/HazardScopeX/tree/ritas-mix1000) of the HazardScopeX project for further development:
- Want to use your own autonomous driving system
- Want to export to other dataset formats
- Want to modify or add specific scenarios
- Want to conduct repeated experiments in specific scenarios
- Want to include ground truth data

> HarzedScopeX 是一个开源的仿真危害因子注入系统框架
>
> HazardScopeX is an open-source simulation hazard injection system framework

## 关于 / About

本项目归属于南方科技大学斯发基斯可信自主系统研究院, 您可以通过 Issues 与我们交流。

或者联系项目管理员邮箱: [zhaozr@mail.sustech.edu.cn](zhaozr@mail.sustech.edu.cn)

This project belongs to the Research Institute of Trustworthy Autonomous Systems (RITAS), Southern University of Science and Technology. You can communicate with us through Issues.

Alternatively, contact the project administrator at: [zhaozr@mail.sustech.edu.cn](zhaozr@mail.sustech.edu.cn)