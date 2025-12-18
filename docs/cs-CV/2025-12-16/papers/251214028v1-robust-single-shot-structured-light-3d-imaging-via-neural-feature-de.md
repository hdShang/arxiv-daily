---
layout: default
title: Robust Single-shot Structured Light 3D Imaging via Neural Feature Decoding
---

# Robust Single-shot Structured Light 3D Imaging via Neural Feature Decoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14028" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14028v1</a>
  <a href="https://arxiv.org/pdf/2512.14028.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14028v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14028v1', 'Robust Single-shot Structured Light 3D Imaging via Neural Feature Decoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaheng Li, Qiyu Dai, Lihan Li, Praneeth Chakravarthula, He Sun, Baoquan Chen, Wenzheng Chen

**分类**: cs.CV

**发布日期**: 2025-12-16

**🔗 代码/项目**: [PROJECT_PAGE](https://namisntimpot.github.io/NSLweb/)

---

## 💡 一句话要点

**提出基于神经特征解码的鲁棒单目结构光3D成像方法，提升复杂场景下的深度估计精度。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `结构光` `三维成像` `神经特征` `深度估计` `特征匹配` `代价体` `单目深度估计`

## 📋 核心要点

1. 传统结构光方法在遮挡、精细结构和非朗伯表面等复杂场景下，由于像素域匹配的局限性，鲁棒性较差。
2. 该论文提出一种基于神经特征解码的框架，在特征空间进行对应匹配，并结合几何先验，提升鲁棒性。
3. 实验表明，该方法在合成数据上训练后，能很好地泛化到真实环境，且优于商业结构光系统和被动立体视觉方法。

## 📝 摘要（中文）

本文研究了使用单目结构光系统进行主动3D成像的问题，该系统广泛应用于商业3D传感设备，如Apple Face ID和Intel RealSense。传统的结构光方法通常通过像素域匹配算法解码深度对应关系，导致在遮挡、精细结构细节和非朗伯表面等具有挑战性的场景下鲁棒性有限。受神经特征匹配最新进展的启发，我们提出了一种基于学习的结构光解码框架，该框架在特征空间而非脆弱的像素域中执行鲁棒的对应匹配。我们的方法从投影图案和捕获的红外(IR)图像中提取神经特征，通过在特征空间中构建代价体来显式地结合它们的几何先验，从而显著提高了像素域解码方法的性能。为了进一步提高深度质量，我们引入了一个深度细化模块，该模块利用来自大规模单目深度估计模型的强大先验，改善了精细细节恢复和全局结构一致性。为了促进有效的学习，我们开发了一个基于物理的结构光渲染管线，生成了近一百万个具有不同物体和材料的合成图案-图像对，用于室内环境。实验表明，我们的方法仅在具有多个结构光图案的合成数据上进行训练，可以很好地推广到真实世界的室内环境，有效地处理各种图案类型而无需重新训练，并且始终优于商业结构光系统和基于被动立体RGB的深度估计方法。

## 🔬 方法详解

**问题定义**：论文旨在解决单目结构光3D成像在复杂场景下鲁棒性不足的问题。传统方法依赖像素域的匹配，容易受到遮挡、精细结构和非朗伯表面等因素的影响，导致深度估计精度下降。

**核心思路**：论文的核心思路是将像素域的匹配问题转化为特征空间的匹配问题。通过提取投影图案和红外图像的神经特征，并在特征空间构建代价体，利用学习到的特征进行更鲁棒的对应关系匹配。这种方法能够更好地利用图像的上下文信息和几何先验，从而提高深度估计的准确性和鲁棒性。

**技术框架**：整体框架包含三个主要模块：1) 特征提取模块：使用神经网络从投影图案和红外图像中提取特征。2) 特征匹配模块：在特征空间中构建代价体，并使用神经网络进行特征匹配，得到初始深度图。3) 深度细化模块：利用单目深度估计模型的先验知识，对初始深度图进行细化，提高深度图的质量和结构一致性。

**关键创新**：最重要的创新点在于将结构光解码问题从像素域转移到特征域。通过学习到的特征进行匹配，能够更好地应对复杂场景下的干扰因素，提高深度估计的鲁棒性。此外，利用单目深度估计模型的先验知识进行深度细化，进一步提升了深度图的质量。

**关键设计**：论文设计了一个基于物理的结构光渲染管线，生成了大量合成数据用于训练。代价体的构建方式和特征匹配网络的结构是关键的设计细节。深度细化模块使用了预训练的单目深度估计模型，并针对结构光数据的特点进行了微调。损失函数的设计也至关重要，需要平衡深度估计的准确性和鲁棒性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14028v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14028v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14028v1/imgs2/fig3_effect_dav2/00003-102-D415-lir.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该方法在合成数据上训练后，能够很好地泛化到真实世界的室内环境，并且无需针对不同的结构光图案进行重新训练。实验结果表明，该方法在深度估计精度和鲁棒性方面均优于商业结构光系统和基于被动立体RGB的深度估计方法，尤其是在处理遮挡、精细结构和非朗伯表面等复杂场景时，优势更加明显。

## 🎯 应用场景

该研究成果可应用于人脸识别、三维重建、机器人导航、增强现实等领域。特别是在对精度和鲁棒性要求较高的场景下，例如移动设备的3D传感、工业自动化中的物体识别和定位等，具有重要的应用价值。未来，该方法有望进一步推广到室外环境和更复杂的场景中。

## 📄 摘要（原文）

> We consider the problem of active 3D imaging using single-shot structured light systems, which are widely employed in commercial 3D sensing devices such as Apple Face ID and Intel RealSense. Traditional structured light methods typically decode depth correspondences through pixel-domain matching algorithms, resulting in limited robustness under challenging scenarios like occlusions, fine-structured details, and non-Lambertian surfaces. Inspired by recent advances in neural feature matching, we propose a learning-based structured light decoding framework that performs robust correspondence matching within feature space rather than the fragile pixel domain. Our method extracts neural features from the projected patterns and captured infrared (IR) images, explicitly incorporating their geometric priors by building cost volumes in feature space, achieving substantial performance improvements over pixel-domain decoding approaches. To further enhance depth quality, we introduce a depth refinement module that leverages strong priors from large-scale monocular depth estimation models, improving fine detail recovery and global structural coherence. To facilitate effective learning, we develop a physically-based structured light rendering pipeline, generating nearly one million synthetic pattern-image pairs with diverse objects and materials for indoor settings. Experiments demonstrate that our method, trained exclusively on synthetic data with multiple structured light patterns, generalizes well to real-world indoor environments, effectively processes various pattern types without retraining, and consistently outperforms both commercial structured light systems and passive stereo RGB-based depth estimation methods. Project page: https://namisntimpot.github.io/NSLweb/.

