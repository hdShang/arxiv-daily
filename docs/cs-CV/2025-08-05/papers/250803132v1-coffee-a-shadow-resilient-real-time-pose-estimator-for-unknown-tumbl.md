---
layout: default
title: "COFFEE: A Shadow-Resilient Real-Time Pose Estimator for Unknown Tumbling Asteroids using Sparse Neural Networks"
---

# COFFEE: A Shadow-Resilient Real-Time Pose Estimator for Unknown Tumbling Asteroids using Sparse Neural Networks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03132" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03132v1</a>
  <a href="https://arxiv.org/pdf/2508.03132.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03132v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03132v1', 'COFFEE: A Shadow-Resilient Real-Time Pose Estimator for Unknown Tumbling Asteroids using Sparse Neural Networks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arion Zimmermann, Soon-Jo Chung, Fred Hadaegh

**分类**: cs.CV, cs.RO

**发布日期**: 2025-08-05

**备注**: in Proc. 75th Int. Astronautical Congress (IAC-24), Milan, Italy, Oct. 2024

---

## 💡 一句话要点

**提出COFFEE以解决未知翻滚小行星的实时姿态估计问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `姿态估计` `小行星探测` `深度学习` `稀疏神经网络` `图神经网络` `实时处理` `航天技术`

## 📋 核心要点

1. 现有姿态估计方法在实时性和准确性之间存在权衡，尤其在处理翻滚小行星时，阴影影响导致估计偏差。
2. COFFEE框架通过结合太阳相位角信息，检测与阴影不变的稀疏特征，提升了姿态估计的准确性和实时性。
3. 实验表明，COFFEE在合成数据和翻滚小行星的渲染上，姿态估计速度比现有深度学习方法快一个数量级，且无偏差。

## 📝 摘要（中文）

准确估计太空中未知物体的状态是一个关键挑战，涉及从跟踪太空垃圾到小天体形状估计等应用。现有方法如SIFT、ORB和AKAZE虽然实现了实时性，但姿态估计不准确，而现代深度学习方法虽然提供了更高质量的特征，但计算资源需求较高，难以在空间合格硬件上实现。此外，现有方法对物体表面高度不透明的自投影阴影缺乏鲁棒性。本文提出COFFEE（Celestial Occlusion Fast FEature Extractor），一种实时姿态估计框架，利用航天器上常见的太阳跟踪传感器提供的太阳相位角信息，通过将显著轮廓与其投影阴影关联，检测出一组稀疏特征，且对阴影运动不变。稀疏神经网络与基于注意力的图神经网络特征匹配模型联合训练，提供连续帧之间的对应关系。实验结果表明，该方法无偏差、比经典姿态估计管道更准确，并且在合成数据和翻滚小行星Apophis的渲染上速度比其他最先进的深度学习管道快一个数量级。

## 🔬 方法详解

**问题定义**：本文解决的是在未知翻滚小行星的实时姿态估计中，现有方法由于阴影影响而导致的估计偏差问题。现有的经典方法和深度学习方法在准确性和计算资源上均存在不足。

**核心思路**：COFFEE框架的核心思路是利用太阳相位角信息，结合显著轮廓与其投影阴影的关系，检测出对阴影运动不变的稀疏特征，从而提高姿态估计的准确性。

**技术框架**：该框架包括两个主要模块：首先是稀疏特征提取模块，通过太阳相位角信息识别特征；其次是特征匹配模块，使用稀疏神经网络和图神经网络进行特征匹配，提供连续帧之间的对应关系。

**关键创新**：COFFEE的主要创新在于其对阴影的鲁棒性，利用太阳相位角信息和稀疏特征提取，克服了传统方法在阴影影响下的偏差问题。

**关键设计**：在网络结构上，稀疏神经网络与图神经网络的结合是关键设计，损失函数的选择也确保了特征匹配的准确性和效率。

## 📊 实验亮点

实验结果显示，COFFEE在合成数据和翻滚小行星Apophis的渲染上，姿态估计速度比现有最先进的深度学习方法快一个数量级，且无偏差，显著提升了姿态估计的准确性和实时性。

## 🎯 应用场景

该研究的潜在应用领域包括太空探测、卫星导航和小行星采矿等。通过提高对翻滚小行星的姿态估计能力，能够有效支持未来的太空任务，降低任务失败的风险，提升航天器的自主导航能力。

## 📄 摘要（原文）

> The accurate state estimation of unknown bodies in space is a critical challenge with applications ranging from the tracking of space debris to the shape estimation of small bodies. A necessary enabler to this capability is to find and track features on a continuous stream of images. Existing methods, such as SIFT, ORB and AKAZE, achieve real-time but inaccurate pose estimates, whereas modern deep learning methods yield higher quality features at the cost of more demanding computational resources which might not be available on space-qualified hardware. Additionally, both classical and data-driven methods are not robust to the highly opaque self-cast shadows on the object of interest. We show that, as the target body rotates, these shadows may lead to large biases in the resulting pose estimates. For these objects, a bias in the real-time pose estimation algorithm may mislead the spacecraft's state estimator and cause a mission failure, especially if the body undergoes a chaotic tumbling motion. We present COFFEE, the Celestial Occlusion Fast FEature Extractor, a real-time pose estimation framework for asteroids designed to leverage prior information on the sun phase angle given by sun-tracking sensors commonly available onboard spacecraft. By associating salient contours to their projected shadows, a sparse set of features are detected, invariant to the motion of the shadows. A Sparse Neural Network followed by an attention-based Graph Neural Network feature matching model are then jointly trained to provide a set of correspondences between successive frames. The resulting pose estimation pipeline is found to be bias-free, more accurate than classical pose estimation pipelines and an order of magnitude faster than other state-of-the-art deep learning pipelines on synthetic data as well as on renderings of the tumbling asteroid Apophis.

