---
layout: default
title: "DEPTHOR++: Robust Depth Enhancement from a Real-World Lightweight dToF and RGB Guidance"
---

# DEPTHOR++: Robust Depth Enhancement from a Real-World Lightweight dToF and RGB Guidance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26498" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26498v1</a>
  <a href="https://arxiv.org/pdf/2509.26498.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26498v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26498v1', 'DEPTHOR++: Robust Depth Enhancement from a Real-World Lightweight dToF and RGB Guidance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jijun Xiang, Longliang Liu, Xuan Zhu, Xianqi Wang, Min Lin, Xin Yang

**分类**: cs.CV

**发布日期**: 2025-09-30

**备注**: 15 pages, 16 figures

---

## 💡 一句话要点

**DEPTHOR++：针对真实世界dToF噪声的鲁棒深度增强框架**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `深度补全` `dToF传感器` `噪声建模` `异常检测` `深度学习` `RGB-D` `鲁棒性`

## 📋 核心要点

1. 现有深度补全方法对dToF传感器的噪声和误差敏感，限制了其在真实场景中的应用。
2. DEPTHOR++通过模拟真实噪声、异常检测和定制网络，增强了深度补全模型对噪声dToF数据的鲁棒性。
3. 实验表明，DEPTHOR++在多个数据集上显著提升了深度补全的精度，甚至超越了高端传感器性能。

## 📝 摘要（中文）

深度增强技术利用RGB图像引导，将原始dToF信号转换为稠密深度图，对于3D重建和SLAM等高精度任务至关重要。然而，现有方法通常假设理想的dToF输入和完美的dToF-RGB对齐，忽略了校准误差和异常值，限制了实际应用。本文系统地分析了真实世界轻量级dToF传感器的噪声特性，并提出了一个实用且新颖的深度补全框架DEPTHOR++，从三个关键方面增强了对噪声dToF输入的鲁棒性。首先，我们引入了一种基于合成数据集的模拟方法，生成逼真的训练样本，用于鲁棒模型训练。其次，我们提出了一种无需学习参数的异常检测机制，以识别和移除错误的dToF测量值，防止在补全过程中产生误导性的传播。第三，我们设计了一个针对噪声dToF输入的深度补全网络，该网络集成了RGB图像和预训练的单目深度估计先验，以改善在具有挑战性区域的深度恢复。在ZJU-L5数据集和真实世界样本上，我们的训练策略显著提升了现有的深度补全模型，我们的模型实现了最先进的性能，RMSE和Rel平均提高了22%和11%。在Mirror3D-NYU数据集上，通过结合异常检测方法，我们的模型在镜像区域比之前的SOTA提高了37%。在Hammer数据集上，使用来自RealSense L515的模拟低成本dToF数据，我们的方法超过了L515的测量结果，平均增益为22%，证明了其使低成本传感器优于高端设备的潜力。各种真实世界数据集上的定性结果进一步验证了我们方法的有效性和泛化性。

## 🔬 方法详解

**问题定义**：现有深度补全方法在处理真实世界dToF传感器数据时，面临着噪声大、校准误差和异常值等问题。这些问题会导致深度补全结果不准确，影响3D重建和SLAM等应用。现有方法通常假设理想的dToF输入，忽略了这些实际问题，因此在真实场景中的性能受到限制。

**核心思路**：DEPTHOR++的核心思路是提高深度补全模型对噪声dToF数据的鲁棒性。通过模拟真实噪声环境生成训练数据，利用异常检测机制去除错误的dToF测量值，并设计专门的网络结构来处理噪声输入，从而提升深度补全的精度和可靠性。

**技术框架**：DEPTHOR++框架主要包含三个阶段：1) 基于合成数据的噪声模拟，生成逼真的训练样本；2) 无需学习参数的异常检测，识别并移除错误的dToF测量值；3) 深度补全网络，融合RGB图像和单目深度估计先验，恢复稠密深度图。该网络针对噪声dToF输入进行了优化设计。

**关键创新**：DEPTHOR++的关键创新在于其对真实世界dToF传感器噪声的系统性建模和处理。它提出了一种无需学习参数的异常检测方法，能够有效去除错误的dToF测量值，避免其对深度补全过程产生负面影响。此外，该框架还设计了一个专门针对噪声dToF输入的深度补全网络，充分利用RGB图像和单目深度估计先验信息。

**关键设计**：在噪声模拟方面，论文详细描述了如何基于合成数据生成具有真实噪声特征的dToF数据。异常检测采用了一种基于统计的方法，无需额外的训练参数。深度补全网络采用了编码器-解码器结构，并引入了注意力机制来融合RGB图像和单目深度估计先验。损失函数包括深度损失、梯度损失和法向量损失，以保证深度图的准确性和平滑性。

## 📊 实验亮点

DEPTHOR++在ZJU-L5数据集上，RMSE和Rel指标平均提升了22%和11%，达到了SOTA水平。在Mirror3D-NYU数据集的镜像区域，性能提升了37%。在Hammer数据集上，使用模拟的低成本dToF数据，性能超越了RealSense L515的实测数据，平均增益为22%。

## 🎯 应用场景

DEPTHOR++可应用于机器人导航、自动驾驶、3D重建、虚拟现实等领域。通过提升低成本dToF传感器的深度感知能力，降低了相关应用的硬件成本，并提高了在复杂环境下的鲁棒性。该研究有助于推动深度感知技术在更广泛领域的应用。

## 📄 摘要（原文）

> Depth enhancement, which converts raw dToF signals into dense depth maps using RGB guidance, is crucial for improving depth perception in high-precision tasks such as 3D reconstruction and SLAM. However, existing methods often assume ideal dToF inputs and perfect dToF-RGB alignment, overlooking calibration errors and anomalies, thus limiting real-world applicability. This work systematically analyzes the noise characteristics of real-world lightweight dToF sensors and proposes a practical and novel depth completion framework, DEPTHOR++, which enhances robustness to noisy dToF inputs from three key aspects. First, we introduce a simulation method based on synthetic datasets to generate realistic training samples for robust model training. Second, we propose a learnable-parameter-free anomaly detection mechanism to identify and remove erroneous dToF measurements, preventing misleading propagation during completion. Third, we design a depth completion network tailored to noisy dToF inputs, which integrates RGB images and pre-trained monocular depth estimation priors to improve depth recovery in challenging regions. On the ZJU-L5 dataset and real-world samples, our training strategy significantly boosts existing depth completion models, with our model achieving state-of-the-art performance, improving RMSE and Rel by 22% and 11% on average. On the Mirror3D-NYU dataset, by incorporating the anomaly detection method, our model improves upon the previous SOTA by 37% in mirror regions. On the Hammer dataset, using simulated low-cost dToF data from RealSense L515, our method surpasses the L515 measurements with an average gain of 22%, demonstrating its potential to enable low-cost sensors to outperform higher-end devices. Qualitative results across diverse real-world datasets further validate the effectiveness and generalizability of our approach.

