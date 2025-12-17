---
layout: default
title: LiNeXt: Revisiting LiDAR Completion with Efficient Non-Diffusion Architectures
---

# LiNeXt: Revisiting LiDAR Completion with Efficient Non-Diffusion Architectures

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.10209" class="toolbar-btn" target="_blank">📄 arXiv: 2511.10209v2</a>
  <a href="https://arxiv.org/pdf/2511.10209.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.10209v2" onclick="toggleFavorite(this, '2511.10209v2', 'LiNeXt: Revisiting LiDAR Completion with Efficient Non-Diffusion Architectures')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenzhe He, Xiaojun Chen, Ruiqi Wang, Ruihui Li, Huilong Pi, Jiapeng Zhang, Zhuo Tang, Kenli Li

**分类**: cs.CV

**发布日期**: 2025-11-13 (更新: 2025-11-30)

**备注**: 18 pages, 13 figures, Accepted to AAAI 2026

---

## 💡 一句话要点

**LiNeXt：提出高效非扩散架构，加速LiDAR点云补全并提升精度。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `LiDAR补全` `点云处理` `非扩散模型` `实时感知` `自动驾驶`

## 📋 核心要点

1. 现有LiDAR点云补全方法主要依赖扩散模型，但其多步迭代采样导致计算开销大，难以满足实时性需求。
2. LiNeXt通过噪声到粗糙(N2C)模块单步去噪，并结合细化模块进行精确结构补全，避免了耗时的迭代过程。
3. 实验表明，LiNeXt在SemanticKITTI数据集上实现了显著的加速和精度提升，参数量也大幅减少。

## 📝 摘要（中文）

本文提出LiNeXt，一个轻量级的非扩散网络，旨在优化快速且精确的点云补全。LiNeXt首先应用噪声到粗糙(N2C)模块，单次通过即可对输入的噪声点云进行去噪，避免了基于扩散方法的多步迭代采样。然后，细化模块利用来自N2C模块的粗糙点云及其中间特征，执行更精确的细化，进一步增强结构的完整性。此外，观察到LiDAR点云表现出距离相关的空间分布，近距离采样密集，远距离采样稀疏。因此，提出了距离感知的选择重复策略，以生成更均匀分布的噪声点云。在SemanticKITTI数据集上，LiNeXt实现了199.8倍的推理速度提升，减少了50.7%的Chamfer距离，并且仅使用了LiDiff 6.1%的参数。这些结果证明了LiNeXt在实时场景补全方面的卓越效率和有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决LiDAR点云补全任务中，现有基于扩散模型的方法计算复杂度高、推理速度慢的问题。这些方法需要进行多步迭代采样才能生成高质量的补全结果，严重限制了其在实时性要求高的自动驾驶等场景中的应用。

**核心思路**：LiNeXt的核心思路是设计一个高效的非扩散网络，通过单步去噪和细化操作，直接从噪声点云生成完整的点云。该方法避免了扩散模型的多步迭代过程，从而显著降低了计算复杂度，提高了推理速度。同时，针对LiDAR点云距离相关的空间分布特性，提出了距离感知的选择重复策略，以改善输入噪声点云的质量。

**技术框架**：LiNeXt主要包含两个模块：噪声到粗糙(N2C)模块和细化模块。N2C模块负责对输入的噪声点云进行初步的去噪，生成一个粗糙的补全结果。细化模块则利用N2C模块的输出和中间特征，进一步细化补全结果，提高结构的完整性和精度。此外，还采用了距离感知的选择重复策略来生成更均匀分布的噪声点云。

**关键创新**：LiNeXt最重要的技术创新在于其非扩散架构，它通过单步去噪和细化操作，避免了扩散模型的多步迭代过程，从而实现了显著的加速。与现有方法相比，LiNeXt在保证补全精度的前提下，大大降低了计算复杂度，提高了推理速度。此外，距离感知的选择重复策略也是一个重要的创新，它能够改善输入噪声点云的质量，从而提高补全性能。

**关键设计**：N2C模块和细化模块的具体网络结构未知，论文中可能使用了卷积、注意力机制等常见的神经网络层。距离感知的选择重复策略的具体实现方式未知，可能涉及到根据点云距离调整采样概率等技术细节。损失函数的设计也未知，可能使用了Chamfer Distance、Earth Mover's Distance等常见的点云距离度量指标。

## 📊 实验亮点

LiNeXt在SemanticKITTI数据集上取得了显著的性能提升。与LiDiff相比，LiNeXt实现了199.8倍的推理速度提升，减少了50.7%的Chamfer距离，并且仅使用了LiDiff 6.1%的参数。这些结果表明，LiNeXt在实时场景补全方面具有卓越的效率和有效性。

## 🎯 应用场景

LiNeXt在自动驾驶、机器人导航、三维重建等领域具有广泛的应用前景。它可以用于提高自动驾驶车辆对周围环境的感知能力，帮助机器人更好地理解和操作周围环境，以及用于生成高质量的三维模型。该研究的突破有望推动这些领域的发展，并为人们的生活带来便利。

## 📄 摘要（原文）

> 3D LiDAR scene completion from point clouds is a fundamental component of perception systems in autonomous vehicles. Previous methods have predominantly employed diffusion models for high-fidelity reconstruction. However, their multi-step iterative sampling incurs significant computational overhead, limiting its real-time applicability. To address this, we propose LiNeXt-a lightweight, non-diffusion network optimized for rapid and accurate point cloud completion. Specifically, LiNeXt first applies the Noise-to-Coarse (N2C) Module to denoise the input noisy point cloud in a single pass, thereby obviating the multi-step iterative sampling of diffusion-based methods. The Refine Module then takes the coarse point cloud and its intermediate features from the N2C Module to perform more precise refinement, further enhancing structural completeness. Furthermore, we observe that LiDAR point clouds exhibit a distance-dependent spatial distribution, being densely sampled at proximal ranges and sparsely sampled at distal ranges. Accordingly, we propose the Distance-aware Selected Repeat strategy to generate a more uniformly distributed noisy point cloud. On the SemanticKITTI dataset, LiNeXt achieves a 199.8x speedup in inference, reduces Chamfer Distance by 50.7%, and uses only 6.1% of the parameters compared with LiDiff. These results demonstrate the superior efficiency and effectiveness of LiNeXt for real-time scene completion.

