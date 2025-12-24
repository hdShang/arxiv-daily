---
layout: default
title: "HART: Human Aligned Reconstruction Transformer"
---

# HART: Human Aligned Reconstruction Transformer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26621" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26621v1</a>
  <a href="https://arxiv.org/pdf/2509.26621.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26621v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26621v1', 'HART: Human Aligned Reconstruction Transformer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiyi Chen, Shaofei Wang, Marko Mihajlovic, Taewon Kang, Sergey Prokudin, Ming Lin

**分类**: cs.CV

**发布日期**: 2025-09-30

**备注**: Project page: https://xiyichen.github.io/hart

---

## 💡 一句话要点

**HART：提出一种对齐人体的重建Transformer，用于稀疏视角人体重建。**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `人体重建` `Transformer网络` `稀疏视角` `SMPL-X模型` `高斯溅射` `新视角合成` `遮挡感知`

## 📋 核心要点

1. 现有方法难以处理宽松服装、人与物体的交互，且对相机参数有较强假设，限制了真实场景的应用。
2. HART通过预测逐像素的3D信息和人体对应关系，结合遮挡感知泊松重建，恢复完整且与人体结构对齐的几何形状。
3. 实验表明，HART在服装网格重建、SMPL-X估计和新视角合成方面均取得了显著的性能提升，优于现有技术。

## 📝 摘要（中文）

本文介绍了一种统一的稀疏视角人体重建框架HART。给定少量未校准的人体RGB图像作为输入，HART输出一个水密的服装网格、对齐的SMPL-X人体网格以及用于逼真新视角渲染的高斯溅射表示。现有服装人体重建方法要么优化参数化模板，忽略宽松服装和人与物体的交互，要么在简化的相机假设下训练隐式函数，限制了在真实场景中的应用。相比之下，HART预测逐像素的3D点云图、法线和人体对应关系，并采用遮挡感知的泊松重建来恢复完整的几何形状，即使在自遮挡区域也是如此。这些预测还与参数化的SMPL-X人体模型对齐，确保重建的几何形状与人体结构保持一致，同时捕捉宽松的服装和交互。这些人体对齐的网格初始化高斯溅射，进一步实现稀疏视角渲染。尽管仅在2.3K个合成扫描上进行训练，HART实现了最先进的结果：服装网格重建的Chamfer距离提高了18-23%，SMPL-X估计的PA-V2V降低了6-27%，新视角合成的LPIPS在各种数据集上降低了15-27%。这些结果表明，前馈Transformer可以作为一种可扩展的模型，用于在真实世界环境中进行鲁棒的人体重建。代码和模型将会开源。

## 🔬 方法详解

**问题定义**：现有服装人体重建方法主要存在两个痛点：一是基于参数化模板的方法难以捕捉宽松的服装和人与物体的交互；二是基于隐式函数的方法通常需要简化的相机假设，限制了其在真实场景中的应用。因此，如何在稀疏视角下，鲁棒地重建具有复杂服装和交互的真实人体几何结构是一个关键问题。

**核心思路**：HART的核心思路是利用Transformer网络直接预测逐像素的3D点云、法线和人体对应关系，从而避免了对参数化模板的过度依赖和对相机参数的强假设。通过将预测的几何信息与SMPL-X人体模型对齐，保证重建结果与人体结构的一致性。同时，采用遮挡感知的泊松重建来处理自遮挡区域，恢复完整的几何形状。

**技术框架**：HART的整体框架包含以下几个主要模块：1) 特征提取模块：使用Transformer网络从输入的稀疏视角RGB图像中提取逐像素的特征表示。2) 3D预测模块：基于提取的特征，预测每个像素的3D坐标、法线和SMPL-X人体对应关系。3) 几何重建模块：利用预测的3D点云和法线，采用遮挡感知的泊松重建算法生成水密的服装网格。4) 渲染模块：使用重建的网格初始化高斯溅射，用于新视角的渲染。

**关键创新**：HART最重要的创新点在于其直接预测逐像素3D信息的框架，避免了对参数化模板的过度依赖，从而能够更好地处理宽松服装和人与物体的交互。此外，遮挡感知的泊松重建算法能够有效地处理自遮挡区域，恢复更完整的几何形状。与现有方法相比，HART在真实场景中具有更强的鲁棒性和泛化能力。

**关键设计**：HART的关键设计包括：1) 使用Transformer网络进行特征提取和3D预测，充分利用了Transformer的全局建模能力。2) 设计了专门的损失函数来约束预测的3D信息与SMPL-X人体模型的一致性。3) 采用了遮挡感知的泊松重建算法，并对其参数进行了优化，以更好地处理自遮挡区域。

## 📊 实验亮点

HART在多个数据集上取得了显著的性能提升。在服装网格重建方面，Chamfer距离降低了18-23%。在SMPL-X人体姿态估计方面，PA-V2V降低了6-27%。在新视角合成方面，LPIPS降低了15-27%。这些结果表明，HART在服装人体重建方面达到了最先进的水平。

## 🎯 应用场景

HART具有广泛的应用前景，包括虚拟现实/增强现实、游戏、动画制作、虚拟试衣、人体姿态估计等领域。该技术可以用于创建逼真且可交互的虚拟人物，提升用户体验，并为相关应用提供更准确的人体几何信息。

## 📄 摘要（原文）

> We introduce HART, a unified framework for sparse-view human reconstruction. Given a small set of uncalibrated RGB images of a person as input, it outputs a watertight clothed mesh, the aligned SMPL-X body mesh, and a Gaussian-splat representation for photorealistic novel-view rendering. Prior methods for clothed human reconstruction either optimize parametric templates, which overlook loose garments and human-object interactions, or train implicit functions under simplified camera assumptions, limiting applicability in real scenes. In contrast, HART predicts per-pixel 3D point maps, normals, and body correspondences, and employs an occlusion-aware Poisson reconstruction to recover complete geometry, even in self-occluded regions. These predictions also align with a parametric SMPL-X body model, ensuring that reconstructed geometry remains consistent with human structure while capturing loose clothing and interactions. These human-aligned meshes initialize Gaussian splats to further enable sparse-view rendering. While trained on only 2.3K synthetic scans, HART achieves state-of-the-art results: Chamfer Distance improves by 18-23 percent for clothed-mesh reconstruction, PA-V2V drops by 6-27 percent for SMPL-X estimation, LPIPS decreases by 15-27 percent for novel-view synthesis on a wide range of datasets. These results suggest that feed-forward transformers can serve as a scalable model for robust human reconstruction in real-world settings. Code and models will be released.

