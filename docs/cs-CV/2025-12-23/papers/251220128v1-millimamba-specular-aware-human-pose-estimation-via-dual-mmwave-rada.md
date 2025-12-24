---
layout: default
title: milliMamba: Specular-Aware Human Pose Estimation via Dual mmWave Radar with Multi-Frame Mamba Fusion
---

# milliMamba: Specular-Aware Human Pose Estimation via Dual mmWave Radar with Multi-Frame Mamba Fusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20128" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20128v1</a>
  <a href="https://arxiv.org/pdf/2512.20128.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20128v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20128v1', 'milliMamba: Specular-Aware Human Pose Estimation via Dual mmWave Radar with Multi-Frame Mamba Fusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Niraj Prakash Kini, Shiau-Rung Tsai, Guan-Hsun Lin, Wen-Hsiao Peng, Ching-Wen Ma, Jenq-Neng Hwang

**分类**: cs.CV

**发布日期**: 2025-12-23

**备注**: Accepted at WACV 2026

**🔗 代码/项目**: [GITHUB](https://github.com/NYCU-MAPL/milliMamba)

---

## 💡 一句话要点

**milliMamba：基于双毫米波雷达和多帧Mamba融合的抗镜面反射人体姿态估计**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `人体姿态估计` `毫米波雷达` `Mamba` `时空建模` `镜面反射`

## 📋 核心要点

1. 毫米波雷达为人体姿态估计提供了一种保护隐私且不受光照影响的替代方案，但镜面反射导致雷达信号稀疏，特征提取困难。
2. milliMamba通过交叉视角融合Mamba编码器提取时空特征，并使用时空交叉注意力解码器预测关节坐标，从而利用上下文信息推断缺失关节。
3. 实验表明，milliMamba在TransHuPR和HuPR数据集上分别超越基线11.0 AP和14.6 AP，验证了其有效性。

## 📝 摘要（中文）

本文提出milliMamba，一个基于雷达的2D人体姿态估计框架，旨在解决毫米波雷达因镜面反射导致的信号稀疏问题。该框架联合建模特征提取和解码阶段的时空依赖性。具体而言，针对雷达输入的高维度特性，采用交叉视角融合Mamba编码器，以线性复杂度高效提取长序列的时空特征。然后，使用时空交叉注意力解码器预测多帧的关节坐标。这种时空建模流程使模型能够利用相邻帧和关节的上下文线索，推断因镜面反射而缺失的关节。为了增强运动平滑性，在训练过程中，除了标准关键点损失外，还引入了速度损失。在TransHuPR和HuPR数据集上的实验表明，该方法取得了显著的性能提升，分别超过基线11.0 AP和14.6 AP，同时保持了合理的复杂度。代码已开源。

## 🔬 方法详解

**问题定义**：毫米波雷达在人体姿态估计中面临的主要问题是镜面反射导致的信号稀疏性。传统的基于雷达的人体姿态估计方法难以从稀疏信号中提取鲁棒的特征，导致姿态估计精度下降。现有方法通常无法有效利用时空上下文信息来弥补因镜面反射造成的关节信息缺失。

**核心思路**：milliMamba的核心思路是利用Mamba架构强大的序列建模能力，同时在编码器和解码器中融入时空信息。通过Mamba编码器提取长序列的时空特征，并利用时空交叉注意力解码器融合多帧信息，从而实现对缺失关节的推断。这种设计旨在充分利用雷达信号的时空上下文信息，提高对镜面反射的鲁棒性。

**技术框架**：milliMamba框架主要包含两个阶段：特征提取和解码。首先，使用交叉视角融合Mamba编码器从雷达数据中提取时空特征。然后，使用时空交叉注意力解码器，结合多帧信息预测人体关节坐标。为了保证运动的平滑性，在训练阶段引入了速度损失。

**关键创新**：milliMamba的关键创新在于将Mamba架构引入到雷达人体姿态估计中，并设计了交叉视角融合Mamba编码器和时空交叉注意力解码器。Mamba架构能够以线性复杂度处理长序列，有效提取时空特征。交叉视角融合能够整合来自不同雷达视角的信号，提高特征的鲁棒性。时空交叉注意力解码器能够融合多帧信息，弥补因镜面反射造成的关节信息缺失。

**关键设计**：交叉视角融合Mamba编码器：具体实现方式未知，但推测是将不同雷达视角的特征进行融合后输入Mamba模块。时空交叉注意力解码器：具体实现方式未知，但推测是利用注意力机制对不同帧和关节的信息进行加权融合。速度损失：用于约束相邻帧之间关节运动的平滑性，具体形式未知，但通常是计算相邻帧之间关节速度的差异，并将其作为损失函数的一部分。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20128v1/fig/pipeline_7.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20128v1/fig/mamba_scan_4.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20128v1/fig/preprocessing_6.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

milliMamba在TransHuPR和HuPR数据集上取得了显著的性能提升，分别超过基线11.0 AP和14.6 AP。这些结果表明，milliMamba能够有效解决毫米波雷达人体姿态估计中因镜面反射导致的信号稀疏问题，并显著提高姿态估计的精度。同时，该方法保持了合理的计算复杂度。

## 🎯 应用场景

milliMamba在智能家居、健康监测、安防监控等领域具有广泛的应用前景。例如，可以在智能家居中用于识别人体行为，实现智能控制；在健康监测中用于评估人体运动状态，提供个性化健康建议；在安防监控中用于检测异常行为，提高安全性。由于其隐私保护特性，在对隐私敏感的场景下具有独特的优势。

## 📄 摘要（原文）

> Millimeter-wave radar offers a privacy-preserving and lighting-invariant alternative to RGB sensors for Human Pose Estimation (HPE) task. However, the radar signals are often sparse due to specular reflection, making the extraction of robust features from radar signals highly challenging. To address this, we present milliMamba, a radar-based 2D human pose estimation framework that jointly models spatio-temporal dependencies across both the feature extraction and decoding stages. Specifically, given the high dimensionality of radar inputs, we adopt a Cross-View Fusion Mamba encoder to efficiently extract spatio-temporal features from longer sequences with linear complexity. A Spatio-Temporal-Cross Attention decoder then predicts joint coordinates across multiple frames. Together, this spatio-temporal modeling pipeline enables the model to leverage contextual cues from neighboring frames and joints to infer missing joints caused by specular reflections. To reinforce motion smoothness, we incorporate a velocity loss alongside the standard keypoint loss during training. Experiments on the TransHuPR and HuPR datasets demonstrate that our method achieves significant performance improvements, exceeding the baselines by 11.0 AP and 14.6 AP, respectively, while maintaining reasonable complexity. Code: https://github.com/NYCU-MAPL/milliMamba

