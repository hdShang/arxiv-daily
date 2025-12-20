---
layout: default
title: Instant Expressive Gaussian Head Avatar via 3D-Aware Expression Distillation
---

# Instant Expressive Gaussian Head Avatar via 3D-Aware Expression Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16893" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16893v1</a>
  <a href="https://arxiv.org/pdf/2512.16893.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16893v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16893v1', 'Instant Expressive Gaussian Head Avatar via 3D-Aware Expression Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaiwen Jiang, Xueting Li, Seonwook Park, Ravi Ramamoorthi, Shalini De Mello, Koki Nagano

**分类**: cs.CV

**发布日期**: 2025-12-18

**备注**: Project website is https://research.nvidia.com/labs/amri/projects/instant4d

---

## 💡 一句话要点

**提出基于3D感知表达蒸馏的快速高表现力高斯头部Avatar方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `人脸动画` `3D人脸` `高斯溅射` `知识蒸馏` `扩散模型` `实时渲染` `数字孪生`

## 📋 核心要点

1. 2D人像动画在质量上取得了显著提升，但通常牺牲了3D一致性和速度，限制了其在数字孪生等场景中的应用。
2. 该方法通过将2D扩散模型的知识提炼到前馈编码器中，实现快速生成3D一致且富有表现力的可动画人脸。
3. 该方法采用轻量级局部融合策略，在保证动画质量的同时，实现了107.31 FPS的快速动画和姿态控制。

## 📝 摘要（中文）

本文提出了一种新的方法，旨在结合基于扩散模型的2D人像动画和基于显式3D表示（如神经辐射场或高斯溅射）的3D人脸动画的优点。该方法通过将知识从2D扩散模型提炼到一个前馈编码器中，实现从单张图像到3D一致、快速且富有表现力的可动画表示的即时转换。动画表示与人脸的3D表示解耦，并从数据中隐式地学习运动，从而消除了对预定义参数模型的依赖。采用轻量级的局部融合策略，以实现高动画表现力，避免了以往计算密集型的全局融合机制。该方法在动画和姿态控制方面以107.31 FPS的速度运行，同时实现了与最先进方法相当的动画质量。

## 🔬 方法详解

**问题定义**：现有2D人像动画方法虽然质量高，但缺乏3D一致性且速度慢，难以应用于实时场景。而基于3D表示的人脸动画方法虽然保证了3D一致性和速度，但动画细节表现力不足。因此，需要一种既能保证3D一致性和速度，又能实现高表现力动画的方法。

**核心思路**：核心思路是将高质量的2D扩散模型的知识蒸馏到基于3D表示的前馈网络中，从而结合两者的优点。通过这种方式，可以快速生成具有丰富表情细节且3D一致的人脸动画。同时，将动画表示与3D结构解耦，并采用轻量级的局部融合策略，进一步提升了效率和表现力。

**技术框架**：该方法包含一个前馈编码器，用于将单张输入图像转换为3D人脸表示和动画参数。该3D人脸表示基于高斯溅射，保证了渲染速度和质量。动画参数则用于控制人脸的表情和姿态。为了融合3D结构和动画信息，采用了轻量级的局部融合模块。整个框架通过蒸馏学习进行训练，利用2D扩散模型生成的动画序列作为监督信号。

**关键创新**：该方法的关键创新在于：1) 采用蒸馏学习的方式，将2D扩散模型的知识迁移到3D人脸动画中；2) 将动画表示与3D结构解耦，从而可以独立控制表情和姿态；3) 采用轻量级的局部融合策略，避免了计算密集型的全局融合，提高了效率。

**关键设计**：在网络结构方面，编码器采用卷积神经网络，用于提取图像特征。高斯溅射表示采用标准的3D高斯参数化。局部融合模块采用多个卷积层和注意力机制，用于融合3D结构和动画信息。损失函数包括重建损失、3D一致性损失和动画损失。重建损失用于保证生成的人脸图像与输入图像相似。3D一致性损失用于保证生成的人脸在不同视角下的一致性。动画损失用于保证生成的动画与2D扩散模型生成的动画相似。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16893v1/fig/expressiveness_vs_consistency_colored.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16893v1/fig/pipeline-2.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16893v1/fig/residual_features.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该方法在动画和姿态控制方面实现了107.31 FPS的速度，同时达到了与最先进方法相当的动画质量。与现有方法相比，该方法在速度和质量之间取得了更好的平衡。实验结果表明，该方法在表情细节和3D一致性方面均优于其他基于3D表示的人脸动画方法。

## 🎯 应用场景

该研究成果可广泛应用于数字孪生、远程呈现、虚拟会议、游戏角色生成等领域。通过该方法，可以快速生成逼真且富有表现力的3D人脸Avatar，为用户提供更加沉浸式的交互体验。此外，该方法还可以用于人脸表情识别、人脸动画编辑等任务，具有重要的实际应用价值。

## 📄 摘要（原文）

> Portrait animation has witnessed tremendous quality improvements thanks to recent advances in video diffusion models. However, these 2D methods often compromise 3D consistency and speed, limiting their applicability in real-world scenarios, such as digital twins or telepresence. In contrast, 3D-aware facial animation feedforward methods -- built upon explicit 3D representations, such as neural radiance fields or Gaussian splatting -- ensure 3D consistency and achieve faster inference speed, but come with inferior expression details. In this paper, we aim to combine their strengths by distilling knowledge from a 2D diffusion-based method into a feed-forward encoder, which instantly converts an in-the-wild single image into a 3D-consistent, fast yet expressive animatable representation. Our animation representation is decoupled from the face's 3D representation and learns motion implicitly from data, eliminating the dependency on pre-defined parametric models that often constrain animation capabilities. Unlike previous computationally intensive global fusion mechanisms (e.g., multiple attention layers) for fusing 3D structural and animation information, our design employs an efficient lightweight local fusion strategy to achieve high animation expressivity. As a result, our method runs at 107.31 FPS for animation and pose control while achieving comparable animation quality to the state-of-the-art, surpassing alternative designs that trade speed for quality or vice versa. Project website is https://research.nvidia.com/labs/amri/projects/instant4d

