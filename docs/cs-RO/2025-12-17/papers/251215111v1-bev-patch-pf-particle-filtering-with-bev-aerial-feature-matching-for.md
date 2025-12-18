---
layout: default
title: BEV-Patch-PF: Particle Filtering with BEV-Aerial Feature Matching for Off-Road Geo-Localization
---

# BEV-Patch-PF: Particle Filtering with BEV-Aerial Feature Matching for Off-Road Geo-Localization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15111" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15111v1</a>
  <a href="https://arxiv.org/pdf/2512.15111.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15111v1" onclick="toggleFavorite(this, '2512.15111v1', 'BEV-Patch-PF: Particle Filtering with BEV-Aerial Feature Matching for Off-Road Geo-Localization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dongmyeong Lee, Jesse Quattrociocchi, Christian Ellis, Rwik Rana, Amanda Adkins, Adam Uccello, Garrett Warnell, Joydeep Biswas

**分类**: cs.RO, cs.CV

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**提出BEV-Patch-PF，利用BEV特征匹配的粒子滤波实现越野环境无GPS定位**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `越野定位` `粒子滤波` `鸟瞰图` `特征匹配` `无GPS定位`

## 📋 核心要点

1. 现有越野定位方法依赖GPS或视觉特征，但在无GPS或光照变化剧烈的环境中表现不佳，鲁棒性不足。
2. BEV-Patch-PF利用车载RGB-D数据构建BEV特征图，并与航拍特征图进行匹配，实现无GPS的鲁棒定位。
3. 实验表明，BEV-Patch-PF在真实越野数据集上显著优于基于检索的基线方法，且能在Tesla T4上实时运行。

## 📝 摘要（中文）

本文提出了一种名为BEV-Patch-PF的无GPS序列地理定位系统，该系统集成了粒子滤波与学习到的鸟瞰图（BEV）和航拍特征图。系统首先从车载RGB和深度图像构建BEV特征图。对于每个3自由度的粒子姿态假设，系统从围绕近似位置查询的局部航拍图像计算出的航拍特征图中裁剪相应的patch。BEV-Patch-PF通过匹配BEV特征与航拍patch特征来计算每个粒子的对数似然。在两个真实世界的越野数据集上，我们的方法在已见过的路线上的绝对轨迹误差（ATE）降低了7.5倍，在未见过的路线上的ATE降低了7.0倍，同时保持了在密集树冠和阴影下的准确性。该系统在NVIDIA Tesla T4上以10 Hz的实时运行，从而实现了实际的机器人部署。

## 🔬 方法详解

**问题定义**：论文旨在解决越野环境下，在缺乏可靠GPS信号或光照条件恶劣的情况下，机器人进行精确定位的问题。现有方法，如依赖GPS或纯视觉特征的方法，在这些场景下表现出鲁棒性不足的缺点，容易受到环境干扰的影响。

**核心思路**：论文的核心思路是利用车载传感器构建的鸟瞰图（BEV）特征与预先构建的航拍特征图进行匹配，从而实现定位。通过粒子滤波框架，对不同的姿态假设进行评估，并选择最优的姿态估计。这种方法结合了局部感知和全局信息，提高了定位的准确性和鲁棒性。

**技术框架**：BEV-Patch-PF系统的整体框架包括以下几个主要模块：1) **BEV特征提取**：利用车载RGB-D图像构建BEV特征图。2) **航拍特征图查询**：根据机器人的近似位置，从预先构建的航拍特征图中查询对应的区域。3) **粒子滤波**：使用粒子滤波框架，每个粒子代表一个可能的机器人姿态。4) **特征匹配**：对于每个粒子，从航拍特征图中裁剪对应的patch，并与BEV特征图进行匹配，计算相似度。5) **权重更新**：根据特征匹配的相似度，更新每个粒子的权重。6) **重采样**：根据粒子的权重进行重采样，选择更优的粒子。

**关键创新**：该方法最重要的创新点在于将BEV特征与航拍特征图相结合，用于粒子滤波的权重更新。这种方法能够有效地利用全局信息，提高定位的准确性和鲁棒性。此外，该方法还能够在计算资源有限的嵌入式平台上实现实时运行。

**关键设计**：论文中关键的设计包括：1) 使用深度学习方法提取BEV和航拍特征，以提高特征的表达能力。2) 设计了一种有效的特征匹配方法，用于计算BEV特征和航拍patch之间的相似度。3) 优化了粒子滤波算法，以提高计算效率。4) 采用对数似然函数计算粒子的权重，以提高定位的精度。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15111v1/figures/thumbnail/fig1_rgb.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15111v1/figures/thumbnail/fig1_depth.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15111v1/figures/thumbnail/fig1_map.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，BEV-Patch-PF在两个真实世界的越野数据集上显著优于基于检索的基线方法。在已见过的路线上的绝对轨迹误差（ATE）降低了7.5倍，在未见过的路线上的ATE降低了7.0倍。此外，该系统能够在NVIDIA Tesla T4上以10 Hz的实时运行，证明了其在实际机器人部署中的可行性。

## 🎯 应用场景

BEV-Patch-PF在农业机器人、搜救机器人、矿业机器人等需要在复杂越野环境中进行自主导航的领域具有广泛的应用前景。该技术能够提高机器人在无GPS或恶劣光照条件下的定位精度和鲁棒性，从而实现更可靠的自主作业。未来，该技术有望应用于自动驾驶、环境监测等更多领域。

## 📄 摘要（原文）

> We propose BEV-Patch-PF, a GPS-free sequential geo-localization system that integrates a particle filter with learned bird's-eye-view (BEV) and aerial feature maps. From onboard RGB and depth images, we construct a BEV feature map. For each 3-DoF particle pose hypothesis, we crop the corresponding patch from an aerial feature map computed from a local aerial image queried around the approximate location. BEV-Patch-PF computes a per-particle log-likelihood by matching the BEV feature to the aerial patch feature. On two real-world off-road datasets, our method achieves 7.5x lower absolute trajectory error (ATE) on seen routes and 7.0x lower ATE on unseen routes than a retrieval-based baseline, while maintaining accuracy under dense canopy and shadow. The system runs in real time at 10 Hz on an NVIDIA Tesla T4, enabling practical robot deployment.

