---
layout: default
title: "RadHARSimulator V2: Video to Doppler Generator"
---

# RadHARSimulator V2: Video to Doppler Generator

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.09022" class="toolbar-btn" target="_blank">📄 arXiv: 2511.09022v1</a>
  <a href="https://arxiv.org/pdf/2511.09022.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.09022v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.09022v1', 'RadHARSimulator V2: Video to Doppler Generator')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weicheng Gao

**分类**: eess.SP, cs.CV

**发布日期**: 2025-11-12

**备注**: 19 pages, 16 figures, 8 tables

**🔗 代码/项目**: [GITHUB](https://github.com/JoeyBGOfficial/RadHARSimulatorV2-Video-to-Doppler-Generator)

---

## 💡 一句话要点

**RadHARSimulator V2：提出一种视频到多普勒谱的雷达人体活动识别模拟器。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `雷达人体活动识别` `模拟器` `多普勒谱` `计算机视觉` `雷达信号处理` `深度学习` `姿态估计`

## 📋 核心要点

1. 现有的雷达人体活动识别模拟软件依赖模型或动作捕捉数据，缺乏灵活性，难以满足多样化场景需求。
2. RadHARSimulator V2通过计算机视觉模块从视频中提取人体姿态，再通过雷达模块模拟多普勒谱，实现灵活的雷达数据生成。
3. 实验验证了该模拟器的有效性，并提出了一种混合神经网络架构，为雷达人体活动识别提供了新的研究工具。

## 📝 摘要（中文）

本文提出了一种雷达人体活动识别(HAR)的综合模拟方法RadHARSimulator V2，该模拟器可以直接从录制的视频素材生成多普勒谱。该模拟器包含计算机视觉和雷达两个模块。在计算机视觉模块中，首先使用带有全局最近邻的目标检测实时模型来检测和跟踪视频中的人体目标。然后，使用高分辨率网络来估计检测到的人体目标的二维姿势。接下来，通过最近匹配方法获得检测到的人体目标的三维姿势。最后，通过卡尔曼滤波实现平滑的时间三维姿势估计。在雷达模块中，首先通过Savitzky-Golay方法实现姿势插值和平滑。其次，使用延迟模型和镜像方法来模拟自由空间和穿墙场景中的回波。然后，使用脉冲压缩、动目标指示和DnCNN生成距离-时间图。接下来，使用短时傅里叶变换和DnCNN再次生成多普勒-时间图(DTM)。最后，使用最大局部能量法提取DTM上的脊特征。此外，还提出了一种用于基于雷达的HAR的混合并行-串行神经网络架构。通过数值实验验证了所设计的模拟器和所提出的网络模型的有效性。该工作的开源代码可在https://github.com/JoeyBGOfficial/RadHARSimulatorV2-Video-to-Doppler-Generator找到。

## 🔬 方法详解

**问题定义**：现有的雷达人体活动识别（HAR）模拟方法主要依赖于预定义的模型或动作捕捉数据，这限制了模拟的灵活性和真实性。难以模拟复杂环境和各种人体活动，从而影响了雷达HAR算法的开发和评估。

**核心思路**：本文的核心思路是从视频数据中提取人体姿态信息，然后利用雷达信号处理技术，将这些姿态信息转化为雷达多普勒谱。通过这种方式，可以利用大量的视频数据来生成各种场景下的雷达数据，从而提高模拟的灵活性和真实性。

**技术框架**：RadHARSimulator V2包含计算机视觉模块和雷达模块。计算机视觉模块负责从视频中检测和跟踪人体目标，并估计其三维姿态。该模块使用目标检测模型、高分辨率姿态估计网络和卡尔曼滤波等技术。雷达模块负责根据人体姿态信息生成雷达多普勒谱。该模块使用延迟模型、镜像方法、脉冲压缩、动目标指示、短时傅里叶变换和DnCNN等技术。整体流程是从视频输入开始，经过计算机视觉处理得到人体姿态，再经过雷达信号处理生成多普勒谱。

**关键创新**：该论文的关键创新在于提出了一种基于视频的雷达HAR模拟方法。与传统的基于模型或动作捕捉数据的模拟方法相比，该方法具有更高的灵活性和真实性。此外，该论文还提出了一种混合并行-串行神经网络架构，用于雷达HAR。

**关键设计**：在计算机视觉模块中，使用了带有全局最近邻的目标检测实时模型和高分辨率网络进行姿态估计。在雷达模块中，使用Savitzky-Golay滤波器进行姿态平滑，使用延迟模型和镜像方法模拟回波，使用DnCNN进行去噪。此外，还设计了一种混合并行-串行神经网络架构，用于雷达HAR，具体结构和参数设置未知。

## 📊 实验亮点

论文通过数值实验验证了所设计的模拟器的有效性。虽然没有给出具体的性能数据，但实验结果表明，该模拟器可以生成高质量的雷达多普勒谱，并且所提出的混合神经网络架构在雷达HAR任务中表现良好。具体的性能提升幅度未知。

## 🎯 应用场景

该研究成果可应用于雷达人体活动识别算法的开发、测试和评估。例如，可以利用该模拟器生成各种场景下的雷达数据，用于训练和评估雷达HAR算法。此外，该模拟器还可以用于研究雷达在智能家居、安全监控、医疗健康等领域的应用，例如跌倒检测、行为分析等。

## 📄 摘要（原文）

> Radar-based human activity recognition (HAR) still lacks a comprehensive simulation method. Existing software is developed based on models or motion-captured data, resulting in limited flexibility. To address this issue, a simulator that directly generates Doppler spectra from recorded video footage (RadHARSimulator V2) is presented in this paper. Both computer vision and radar modules are included in the simulator. In computer vision module, the real-time model for object detection with global nearest neighbor is first used to detect and track human targets in the video. Then, the high-resolution network is used to estimate two-dimensional poses of the detected human targets. Next, the three-dimensional poses of the detected human targets are obtained by nearest matching method. Finally, smooth temporal three-dimensional pose estimation is achieved through Kalman filtering. In radar module, pose interpolation and smoothing are first achieved through the Savitzky-Golay method. Second, the delay model and the mirror method are used to simulate echoes in both free-space and through-the-wall scenarios. Then, range-time map is generated using pulse compression, moving target indication, and DnCNN. Next, Doppler-time map (DTM) is generated using short-time Fourier transform and DnCNN again. Finally, the ridge features on the DTM are extracted using the maximum local energy method. In addition, a hybrid parallel-serial neural network architecture is proposed for radar-based HAR. Numerical experiments are conducted and analyzed to demonstrate the effectiveness of the designed simulator and the proposed network model. The open-source code of this work can be found in: https://github.com/JoeyBGOfficial/RadHARSimulatorV2-Video-to-Doppler-Generator.

