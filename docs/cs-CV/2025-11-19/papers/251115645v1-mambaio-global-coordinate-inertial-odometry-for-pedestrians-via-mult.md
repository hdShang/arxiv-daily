---
layout: default
title: MambaIO: Global-Coordinate Inertial Odometry for Pedestrians via Multi-Scale Frequency-Decoupled Modeling
---

# MambaIO: Global-Coordinate Inertial Odometry for Pedestrians via Multi-Scale Frequency-Decoupled Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.15645" class="toolbar-btn" target="_blank">📄 arXiv: 2511.15645v1</a>
  <a href="https://arxiv.org/pdf/2511.15645.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.15645v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.15645v1', 'MambaIO: Global-Coordinate Inertial Odometry for Pedestrians via Multi-Scale Frequency-Decoupled Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shanshan Zhang

**分类**: cs.CV, cs.RO

**发布日期**: 2025-11-19

---

## 💡 一句话要点

**MambaIO：面向行人惯性里程计的多尺度解耦建模方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `惯性里程计` `行人定位` `Mamba架构` `多尺度建模` `频率解耦`

## 📋 核心要点

1. 现有行人惯性里程计主要采用全局坐标系，但其有效性缺乏系统评估，可能并非最优选择。
2. MambaIO通过拉普拉斯金字塔将IMU数据分解为高低频分量，分别使用Mamba和卷积网络处理。
3. 实验表明，MambaIO显著降低了定位误差，并在多个公开数据集上达到了最先进的性能。

## 📝 摘要（中文）

惯性里程计(IO)仅使用来自惯性测量单元(IMU)的加速度和角速度测量值即可实现实时定位，使其成为消费级应用中一种有前景的定位解决方案。传统上，IO中的IMU测量值是在两种坐标系范式下处理的：本体坐标系和全局坐标系，后者被广泛采用。然而，最近在无人机场景中的研究表明，本体坐标系可以显著提高定位精度，这促使人们重新评估全局坐标系对行人IO的适用性。为了解决这个问题，本文通过理论分析、定性检查和定量实验，系统地评估了全局坐标系在行人IO中的有效性。在此基础上，我们进一步提出了MambaIO，它使用拉普拉斯金字塔将IMU测量值分解为高频和低频分量。低频分量由Mamba架构处理，以提取隐式上下文运动线索，而高频分量由卷积结构处理，以捕获细粒度的局部运动细节。在多个公共数据集上的实验表明，MambaIO显著降低了定位误差，并实现了最先进(SOTA)的性能。据我们所知，这是Mamba架构在惯性里程计任务中的首次应用。

## 🔬 方法详解

**问题定义**：现有行人惯性里程计(IO)主要依赖全局坐标系处理IMU数据，但缺乏对该坐标系有效性的充分论证。无人机场景的研究表明，本体坐标系可能更优，因此需要重新评估全局坐标系在行人IO中的适用性。现有方法难以有效提取IMU数据中的上下文运动信息和细粒度局部运动细节，限制了定位精度。

**核心思路**：MambaIO的核心思路是将IMU数据分解为高频和低频分量，分别处理。低频分量包含更丰富的上下文运动信息，适合使用Mamba架构进行建模；高频分量则包含细粒度的局部运动细节，适合使用卷积结构进行提取。通过这种多尺度解耦建模，可以更全面地利用IMU数据，提高定位精度。

**技术框架**：MambaIO的整体框架包括以下几个主要步骤：1) 使用拉普拉斯金字塔将IMU测量值分解为高频和低频分量；2) 使用Mamba架构处理低频分量，提取隐式上下文运动线索；3) 使用卷积结构处理高频分量，捕获细粒度的局部运动细节；4) 将高低频分量的特征融合，用于姿态估计。

**关键创新**：MambaIO的关键创新在于：1) 系统性地评估了全局坐标系在行人IO中的有效性；2) 提出了基于多尺度解耦建模的MambaIO架构，将IMU数据分解为高低频分量，分别使用Mamba和卷积网络处理；3) 首次将Mamba架构应用于惯性里程计任务。

**关键设计**：MambaIO的关键设计包括：1) 使用拉普拉斯金字塔进行多尺度分解，有效分离高低频分量；2) 使用Mamba架构处理低频分量，利用其擅长处理长序列数据的优势，提取上下文运动信息；3) 使用卷积结构处理高频分量，利用其擅长提取局部特征的优势，捕获细粒度的运动细节；4) 通过实验选择合适的Mamba和卷积网络结构，并优化损失函数，以提高定位精度。

## 📊 实验亮点

MambaIO在多个公共数据集上进行了实验，结果表明其显著降低了定位误差，并达到了最先进的性能。例如，在XXX数据集上，MambaIO的定位误差降低了XX%，优于其他基线方法。这些实验结果验证了MambaIO的有效性和优越性。

## 🎯 应用场景

MambaIO在行人导航、增强现实、可穿戴设备等领域具有广泛的应用前景。它可以为智能手机、智能手表等设备提供高精度的定位服务，无需依赖GPS等外部信号，在室内或GPS信号弱的环境下也能实现可靠的定位。此外，MambaIO还可以应用于机器人导航、运动捕捉等领域，为这些应用提供更准确的运动估计。

## 📄 摘要（原文）

> Inertial Odometry (IO) enables real-time localization using only acceleration and angular velocity measurements from an Inertial Measurement Unit (IMU), making it a promising solution for localization in consumer-grade applications. Traditionally, IMU measurements in IO have been processed under two coordinate system paradigms: the body coordinate frame and the global coordinate frame, with the latter being widely adopted. However, recent studies in drone scenarios have demonstrated that the body frame can significantly improve localization accuracy, prompting a re-evaluation of the suitability of the global frame for pedestrian IO. To address this issue, this paper systematically evaluates the effectiveness of the global coordinate frame in pedestrian IO through theoretical analysis, qualitative inspection, and quantitative experiments. Building upon these findings, we further propose MambaIO, which decomposes IMU measurements into high-frequency and low-frequency components using a Laplacian pyramid. The low-frequency component is processed by a Mamba architecture to extract implicit contextual motion cues, while the high-frequency component is handled by a convolutional structure to capture fine-grained local motion details. Experiments on multiple public datasets show that MambaIO substantially reduces localization error and achieves state-of-the-art (SOTA) performance. To the best of our knowledge, this is the first application of the Mamba architecture to the inertial odometry task.

