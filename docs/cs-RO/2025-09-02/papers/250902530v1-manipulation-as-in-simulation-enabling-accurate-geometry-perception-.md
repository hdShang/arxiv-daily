---
layout: default
title: "Manipulation as in Simulation: Enabling Accurate Geometry Perception in Robots"
---

# Manipulation as in Simulation: Enabling Accurate Geometry Perception in Robots

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02530" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02530v1</a>
  <a href="https://arxiv.org/pdf/2509.02530.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02530v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02530v1', 'Manipulation as in Simulation: Enabling Accurate Geometry Perception in Robots')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Minghuan Liu, Zhengbang Zhu, Xiaoshen Han, Peng Hu, Haotong Lin, Xinyao Li, Jingxiao Chen, Jiafeng Xu, Yichu Yang, Yunfeng Lin, Xinghang Li, Yong Yu, Weinan Zhang, Tao Kong, Bingyi Kang

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-09-02

**备注**: 32 pages, 18 figures, project page: https://manipulation-as-in-simulation.github.io/

---

## 💡 一句话要点

**提出相机深度模型（CDM），提升机器人操作中深度感知的准确性。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `机器人操作` `深度感知` `深度相机` `模拟到真实` `相机深度模型`

## 📋 核心要点

1. 现有机器人操作依赖2D视觉，泛化性差，而深度相机精度不足，限制了3D几何信息的应用。
2. 提出相机深度模型（CDM），通过模拟噪声模式生成高质量数据，提升深度预测精度。
3. 实验证明，CDM使模拟训练的策略能直接应用于真实机器人，完成复杂操作任务。

## 📝 摘要（中文）

现代机器人操作主要依赖于2D彩色图像进行技能学习，但泛化能力较差。人类更多地依赖距离、大小和形状等物理属性与物体交互。虽然深度相机可以提供3D几何信息，但其精度有限且易受噪声影响。本文提出了相机深度模型（CDM），这是一个简单的插件，可用于日常使用的深度相机，它以RGB图像和原始深度信号作为输入，输出去噪的、准确的度量深度。为此，我们开发了一个神经数据引擎，通过模拟深度相机的噪声模式，从模拟中生成高质量的配对数据。结果表明，CDM在深度预测方面实现了接近模拟水平的精度，有效地弥合了模拟到真实的差距。实验首次证明，在原始模拟深度上训练的策略，无需添加噪声或进行真实世界的微调，即可无缝地泛化到真实世界的机器人上，完成涉及铰接、反射和细长物体的两个具有挑战性的长程任务，且性能几乎没有下降。我们希望我们的发现能够激发未来在通用机器人策略中利用模拟数据和3D信息的研究。

## 🔬 方法详解

**问题定义**：现有机器人操作主要依赖2D彩色图像，缺乏对物体3D几何信息的准确感知，导致泛化能力不足。深度相机虽然可以提供3D信息，但其固有的噪声和精度限制，使得直接使用深度数据进行机器人控制变得困难。因此，需要解决的问题是如何提高深度相机的精度，使其能够为机器人提供可靠的3D几何信息，从而提升操作技能的泛化能力。

**核心思路**：核心思路是利用模拟环境生成大量带有噪声的深度数据，训练一个深度相机模型（CDM），使其能够从真实深度相机获取的RGB图像和原始深度信号中，预测出准确的、去噪的度量深度。通过模拟真实深度相机的噪声模式，可以有效地弥合模拟环境和真实环境之间的差距，从而实现从模拟到真实的迁移。

**技术框架**：整体框架包含两个主要部分：神经数据引擎和相机深度模型（CDM）。神经数据引擎负责在模拟环境中生成高质量的配对数据，包括RGB图像和带有噪声的深度图像。CDM是一个神经网络，以RGB图像和原始深度信号作为输入，输出去噪的、准确的度量深度。训练好的CDM可以作为一个插件，直接应用于真实世界的深度相机。

**关键创新**：最重要的创新点在于利用神经数据引擎模拟深度相机的噪声模式，从而生成高质量的训练数据。这种方法避免了直接在真实世界中收集大量数据的困难，并且能够有效地弥合模拟环境和真实环境之间的差距。此外，CDM的设计也考虑了深度相机的特性，能够有效地去除噪声并提高深度预测的精度。

**关键设计**：神经数据引擎通过对深度相机噪声进行建模，例如高斯噪声、椒盐噪声等，并调整噪声的强度和分布，生成逼真的模拟数据。CDM采用了一种卷积神经网络结构，利用RGB图像提供纹理信息，并结合原始深度信号进行深度预测。损失函数包括深度预测的均方误差和一些正则化项，以防止过拟合。具体的网络结构和参数设置需要根据具体的深度相机型号和应用场景进行调整。

## 📊 实验亮点

实验结果表明，CDM能够显著提高深度预测的精度，使其接近模拟水平。使用CDM后，在模拟环境中训练的机器人策略可以直接应用于真实机器人，完成涉及铰接、反射和细长物体的复杂操作任务，且性能几乎没有下降。这表明CDM有效地弥合了模拟到真实的差距，为利用模拟数据进行机器人训练提供了新的途径。

## 🎯 应用场景

该研究成果可广泛应用于机器人操作、自动驾驶、增强现实等领域。通过提高深度感知的准确性，可以使机器人在复杂环境中更好地理解和操作物体，从而实现更智能、更可靠的自动化系统。例如，在工业机器人领域，可以利用该技术实现更精确的装配和检测；在服务机器人领域，可以实现更自然的交互和更灵活的操作。

## 📄 摘要（原文）

> Modern robotic manipulation primarily relies on visual observations in a 2D color space for skill learning but suffers from poor generalization. In contrast, humans, living in a 3D world, depend more on physical properties-such as distance, size, and shape-than on texture when interacting with objects. Since such 3D geometric information can be acquired from widely available depth cameras, it appears feasible to endow robots with similar perceptual capabilities. Our pilot study found that using depth cameras for manipulation is challenging, primarily due to their limited accuracy and susceptibility to various types of noise. In this work, we propose Camera Depth Models (CDMs) as a simple plugin on daily-use depth cameras, which take RGB images and raw depth signals as input and output denoised, accurate metric depth. To achieve this, we develop a neural data engine that generates high-quality paired data from simulation by modeling a depth camera's noise pattern. Our results show that CDMs achieve nearly simulation-level accuracy in depth prediction, effectively bridging the sim-to-real gap for manipulation tasks. Notably, our experiments demonstrate, for the first time, that a policy trained on raw simulated depth, without the need for adding noise or real-world fine-tuning, generalizes seamlessly to real-world robots on two challenging long-horizon tasks involving articulated, reflective, and slender objects, with little to no performance degradation. We hope our findings will inspire future research in utilizing simulation data and 3D information in general robot policies.

