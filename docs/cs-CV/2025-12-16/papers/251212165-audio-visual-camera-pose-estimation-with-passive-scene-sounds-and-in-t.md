---
layout: default
title: Audio-Visual Camera Pose Estimation with Passive Scene Sounds and In-the-Wild Video
---

# Audio-Visual Camera Pose Estimation with Passive Scene Sounds and In-the-Wild Video

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.12165" class="toolbar-btn" target="_blank">📄 arXiv: 2512.12165</a>
  <a href="https://arxiv.org/pdf/2512.12165.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.12165" onclick="toggleFavorite(this, '2512.12165', 'Audio-Visual Camera Pose Estimation with Passive Scene Sounds and In-the-Wild Video')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daniel Adebi, Sagnik Majumder, Kristen Grauman

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出一种利用被动场景声音进行相机位姿估计的音视频融合框架**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `相机位姿估计` `音视频融合` `被动声音` `方向估计` `机器人感知`

## 📋 核心要点

1. 视觉方法在相机位姿估计中面临视觉退化（如模糊、遮挡）的挑战，限制了其在复杂环境下的应用。
2. 该论文提出一种音视频融合框架，利用场景中的被动声音信息，辅助视觉信息进行更准确的相机位姿估计。
3. 实验结果表明，该方法在两个大型数据集上优于纯视觉基线，并在视觉信息受损时表现出更强的鲁棒性。

## 📝 摘要（中文）

相机运动估计是具身感知和3D场景理解中的一个基本问题。虽然视觉方法发展迅速，但它们在视觉退化条件下（如运动模糊或遮挡）常常表现不佳。本文表明，被动场景声音为真实场景视频的相对相机位姿估计提供了补充线索。我们引入了一个简单而有效的音视频框架，将到达方向(DOA)谱和双耳嵌入集成到最先进的纯视觉位姿估计模型中。在两个大型数据集上的结果表明，相对于强大的视觉基线，我们的方法获得了持续的性能提升，并且在视觉信息损坏时表现出鲁棒性。据我们所知，这是第一个成功利用音频进行真实场景视频中相对相机位姿估计的工作，并将偶然的、日常的音频确立为解决经典空间挑战的一种意想不到但很有希望的信号。

## 🔬 方法详解

**问题定义**：论文旨在解决在视觉信息不足或质量较差的情况下，相机位姿估计精度下降的问题。现有方法主要依赖视觉信息，在运动模糊、遮挡等情况下表现不佳，缺乏鲁棒性。

**核心思路**：论文的核心思路是利用场景中自然存在的被动声音作为视觉信息的补充，通过音视频融合的方式，提高相机位姿估计的准确性和鲁棒性。声音信息对视觉退化具有一定的互补性，可以提供额外的空间线索。

**技术框架**：该框架将音频和视频信息融合到现有的视觉位姿估计模型中。主要包含以下模块：1) 音频处理模块：提取音频的到达方向(DOA)谱和双耳嵌入特征。2) 视觉处理模块：使用现有的视觉位姿估计模型提取视觉特征。3) 融合模块：将音频和视觉特征进行融合，共同预测相机位姿。

**关键创新**：该论文的关键创新在于首次将场景中的被动声音信息用于相机位姿估计，并提出了一种有效的音视频融合框架。与传统方法仅依赖视觉信息不同，该方法利用了音频提供的额外空间线索，提高了位姿估计的鲁棒性。

**关键设计**：音频特征提取方面，使用了DOA谱和双耳嵌入，分别捕捉声音的方向信息和空间信息。融合方式上，将音频特征与视觉特征进行拼接或加权融合，具体融合方式未知。损失函数方面，可能使用了位姿预测的回归损失，具体细节未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.12165/imgs/cvpr_teaser_image_small.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.12165/imgs/full_method_diagram.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.12165/imgs/qual_cvpr_2026.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法在两个大型数据集上均优于纯视觉基线，证明了音频信息在相机位姿估计中的有效性。特别是在视觉信息受损的情况下，该方法的性能提升更为显著，体现了其鲁棒性。具体的性能提升数据未知。

## 🎯 应用场景

该研究成果可应用于机器人导航、增强现实、虚拟现实等领域。在光照条件差、存在遮挡或运动模糊等情况下，该方法能够提供更准确的相机位姿估计，提高系统的稳定性和可靠性。未来，该技术有望应用于自动驾驶、无人机等领域，提升其在复杂环境下的感知能力。

## 📄 摘要（原文）

> Understanding camera motion is a fundamental problem in embodied perception and 3D scene understanding. While visual methods have advanced rapidly, they often struggle under visually degraded conditions such as motion blur or occlusions. In this work, we show that passive scene sounds provide complementary cues for relative camera pose estimation for in-the-wild videos. We introduce a simple but effective audio-visual framework that integrates direction-ofarrival (DOA) spectra and binauralized embeddings into a state-of-the-art vision-only pose estimation model. Our results on two large datasets show consistent gains over strong visual baselines, plus robustness when the visual information is corrupted. To our knowledge, this represents the first work to successfully leverage audio for relative camera pose estimation in real-world videos, and it establishes incidental, everyday audio as an unexpected but promising signal for a classic spatial challenge. Project:this http URL.

