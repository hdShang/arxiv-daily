---
layout: default
title: RePose-NeRF: Robust Radiance Fields for Mesh Reconstruction under Noisy Camera Poses
---

# RePose-NeRF: Robust Radiance Fields for Mesh Reconstruction under Noisy Camera Poses

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.08545" class="toolbar-btn" target="_blank">📄 arXiv: 2511.08545v1</a>
  <a href="https://arxiv.org/pdf/2511.08545.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.08545v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.08545v1', 'RePose-NeRF: Robust Radiance Fields for Mesh Reconstruction under Noisy Camera Poses')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sriram Srinivasan, Gautam Ramachandra

**分类**: cs.CV

**发布日期**: 2025-11-11

**备注**: Several figures are included to illustrate the reconstruction and rendering quality of the proposed method, which is why the submission exceeds the 50MB file size limit. > Several figures are included to illustrate the reconstruction and rendering quality of the proposed method, which is why the submission exceeds the 50,000 KB file size limit (Now this has been resolved)

---

## 💡 一句话要点

**RePose-NeRF：提出一种鲁棒的辐射场方法，用于在噪声相机位姿下进行网格重建**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `NeRF` `三维重建` `相机位姿估计` `鲁棒性` `隐式表示` `机器人` `多视角几何`

## 📋 核心要点

1. 现有NeRF方法依赖精确相机位姿，但在真实场景中获取精确位姿困难，限制了其应用。
2. 提出RePose-NeRF，联合优化相机位姿和隐式场景表示，直接从多视角图像重建高质量网格。
3. 实验表明，该方法在位姿不确定性下实现了准确鲁棒的3D重建，并生成可用于机器人工具的网格。

## 📝 摘要（中文）

从多视角图像中进行精确的3D重建对于导航、操作和环境理解等下游机器人任务至关重要。然而，即使在已知校准参数的情况下，在真实环境中获得精确的相机位姿仍然具有挑战性。这限制了现有NeRF方法的实用性，因为它们严重依赖于精确的外部参数估计。此外，它们的隐式体积表示与广泛采用的多边形网格显著不同，使得在标准3D软件中进行渲染和操作效率低下。本文提出了一种鲁棒的框架，可以直接从具有噪声外部参数的多视角图像中重建高质量、可编辑的3D网格。我们的方法联合优化相机位姿，同时学习隐式场景表示，该表示捕获精细的几何细节和逼真的外观。生成的网格与常见的3D图形和机器人工具兼容，从而可以高效地进行下游使用。在标准基准上的实验表明，我们的方法在位姿不确定性下实现了准确而鲁棒的3D重建，弥合了神经隐式表示与实际机器人应用之间的差距。

## 🔬 方法详解

**问题定义**：现有基于NeRF的3D重建方法对相机位姿精度要求高，但在实际应用中，相机位姿往往存在噪声。此外，NeRF生成的隐式体积表示与常用的多边形网格格式不同，不利于在标准3D软件和机器人工具中使用。因此，需要一种能够容忍相机位姿噪声，并直接生成可编辑网格的3D重建方法。

**核心思路**：RePose-NeRF的核心思路是联合优化相机位姿和隐式场景表示。通过在训练过程中同时优化相机位姿，可以减轻位姿噪声的影响，从而提高重建的鲁棒性。同时，通过设计合适的网络结构和损失函数，可以直接从隐式表示中提取高质量的3D网格。

**技术框架**：RePose-NeRF的整体框架包括以下几个主要模块：1) 多视角图像输入；2) 相机位姿初始化（可能包含噪声）；3) 基于NeRF的隐式场景表示学习；4) 相机位姿优化；5) 网格提取。该框架通过迭代优化相机位姿和隐式场景表示，最终得到高质量的3D网格模型。

**关键创新**：RePose-NeRF的关键创新在于联合优化相机位姿和隐式场景表示，从而提高了对相机位姿噪声的鲁棒性。与传统的先估计位姿再进行重建的方法不同，RePose-NeRF将位姿估计和重建过程集成到一个统一的框架中，实现了端到端的优化。此外，该方法可以直接生成可编辑的3D网格，方便在标准3D软件和机器人工具中使用。

**关键设计**：RePose-NeRF的关键设计包括：1) 使用可微分的渲染技术，使得相机位姿优化成为可能；2) 设计合适的损失函数，例如光度一致性损失和几何约束损失，以保证重建的质量；3) 使用高效的网格提取算法，从隐式表示中提取高质量的3D网格。具体的网络结构和参数设置未知，需要参考论文细节。

## 📊 实验亮点

RePose-NeRF在标准benchmark上进行了实验，证明了其在位姿不确定性下的重建精度和鲁棒性。具体性能数据和对比基线未知，但摘要表明该方法优于现有方法，并能生成高质量、可编辑的3D网格，方便下游任务使用。实验结果验证了该方法在实际机器人应用中的潜力。

## 🎯 应用场景

RePose-NeRF在机器人导航、操作和环境理解等领域具有广泛的应用前景。它可以用于在未知或不确定环境中进行3D地图构建，为机器人提供准确的环境信息。此外，RePose-NeRF生成的可编辑网格模型可以方便地用于机器人仿真和规划，提高机器人的智能化水平。该研究有望推动机器人技术在复杂环境中的应用。

## 📄 摘要（原文）

> Accurate 3D reconstruction from multi-view images is essential for downstream robotic tasks such as navigation, manipulation, and environment understanding. However, obtaining precise camera poses in real-world settings remains challenging, even when calibration parameters are known. This limits the practicality of existing NeRF-based methods that rely heavily on accurate extrinsic estimates. Furthermore, their implicit volumetric representations differ significantly from the widely adopted polygonal meshes, making rendering and manipulation inefficient in standard 3D software. In this work, we propose a robust framework that reconstructs high-quality, editable 3D meshes directly from multi-view images with noisy extrinsic parameters. Our approach jointly refines camera poses while learning an implicit scene representation that captures fine geometric detail and photorealistic appearance. The resulting meshes are compatible with common 3D graphics and robotics tools, enabling efficient downstream use. Experiments on standard benchmarks demonstrate that our method achieves accurate and robust 3D reconstruction under pose uncertainty, bridging the gap between neural implicit representations and practical robotic applications.

