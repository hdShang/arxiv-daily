---
layout: default
title: Towards Better Optimization For Listwise Preference in Diffusion Models
---

# Towards Better Optimization For Listwise Preference in Diffusion Models

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.01540" target="_blank" class="toolbar-btn">arXiv: 2510.01540v1</a>
    <a href="https://arxiv.org/pdf/2510.01540.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01540v1" 
            onclick="toggleFavorite(this, '2510.01540v1', 'Towards Better Optimization For Listwise Preference in Diffusion Models')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Jiamu Bai, Xin Yu, Meilong Xu, Weitao Lu, Xin Pan, Kiwan Maeng, Daniel Kifer, Jian Wang, Yu Wang

**分类**: cs.CV

**发布日期**: 2025-10-02

---

## 💡 一句话要点

**提出Diffusion-LPO，用于扩散模型中基于列表偏好的优化，提升图像质量和偏好对齐。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `扩散模型` `偏好学习` `列表偏好优化` `直接偏好优化` `Plackett-Luce模型`

## 📋 核心要点

1. 现有扩散模型偏好学习主要依赖成对偏好，忽略了人工反馈中更精确的列表排序信息。
2. Diffusion-LPO通过聚合用户反馈为排序列表，并基于Plackett-Luce模型扩展DPO目标，实现列表偏好优化。
3. 实验表明，Diffusion-LPO在文本到图像生成、图像编辑和个性化偏好对齐等任务上，显著优于成对DPO基线。

## 📝 摘要（中文）

本文提出了一种名为Diffusion-LPO的简单有效的框架，用于扩散模型中基于列表数据的列表偏好优化。尽管直接偏好优化(DPO)因其计算效率和避免显式奖励建模而被广泛采用，但其在扩散模型中的应用主要依赖于成对偏好。对列表偏好的精确优化在很大程度上仍未得到解决。实际上，关于图像偏好的人工反馈通常包含隐式排序信息，这比成对比较传达了更精确的人工偏好。给定一个标题，我们将用户反馈聚合到一个排序的图像列表中，并在Plackett-Luce模型下推导出DPO目标的列表扩展。Diffusion-LPO通过鼓励每个样本优于所有排名较低的替代方案来强制执行整个排名的一致性。经验证表明，Diffusion-LPO在各种任务中都有效，包括文本到图像生成、图像编辑和个性化偏好对齐。Diffusion-LPO在视觉质量和偏好对齐方面始终优于成对DPO基线。

## 🔬 方法详解

**问题定义**：现有基于人类反馈的扩散模型训练方法，如DPO，主要依赖于成对偏好数据。然而，实际应用中，用户对图像的偏好往往以排序列表的形式给出，包含更丰富的信息。直接使用成对偏好忽略了列表中的排序关系，导致优化效率降低，无法充分利用人类反馈。

**核心思路**：Diffusion-LPO的核心思路是将用户的列表偏好信息纳入优化过程中。它通过将用户反馈聚合为排序的图像列表，并在此基础上扩展DPO的目标函数，从而实现对列表偏好的直接优化。这种方法能够更充分地利用人类反馈中的排序信息，提高模型的训练效率和生成质量。

**技术框架**：Diffusion-LPO的整体框架包括以下几个主要步骤：1) 收集用户对给定文本描述生成的多个图像的偏好排序；2) 将这些排序信息转化为列表偏好数据；3) 基于Plackett-Luce模型，推导出DPO目标的列表扩展；4) 使用扩展后的DPO目标函数训练扩散模型。该框架可以直接应用于现有的扩散模型训练流程中，无需修改模型结构。

**关键创新**：Diffusion-LPO的关键创新在于提出了一个针对列表偏好的DPO目标函数扩展。与传统的成对DPO相比，该方法能够直接利用列表中的排序信息，从而更精确地对齐模型与人类偏好。此外，Diffusion-LPO还通过Plackett-Luce模型对列表偏好进行建模，保证了优化过程的合理性和有效性。

**关键设计**：Diffusion-LPO的关键设计包括：1) 使用Plackett-Luce模型对列表偏好进行建模，该模型假设每个图像被选择的概率与其“吸引力”成正比；2) 基于Plackett-Luce模型，推导出DPO目标的列表扩展，该目标函数鼓励模型生成更符合用户偏好的图像；3) 在训练过程中，使用梯度下降等优化算法，最小化列表DPO目标函数，从而更新扩散模型的参数。

## 📊 实验亮点

实验结果表明，Diffusion-LPO在文本到图像生成、图像编辑和个性化偏好对齐等任务上均取得了显著的性能提升。与成对DPO基线相比，Diffusion-LPO在视觉质量和偏好对齐方面均有明显优势。具体而言，Diffusion-LPO能够生成更符合用户偏好的图像，并且在图像质量方面也优于基线方法。这些结果验证了Diffusion-LPO的有效性和优越性。

## 🎯 应用场景

Diffusion-LPO具有广泛的应用前景，可用于提升文本到图像生成、图像编辑等任务的质量和用户满意度。通过更好地对齐模型与人类偏好，可以生成更符合用户需求的图像内容。此外，该方法还可以应用于个性化图像生成，根据用户的特定偏好定制图像内容。未来，Diffusion-LPO有望在创意设计、内容生成、虚拟现实等领域发挥重要作用。

## 📄 摘要（原文）

> Reinforcement learning from human feedback (RLHF) has proven effectiveness for aligning text-to-image (T2I) diffusion models with human preferences. Although Direct Preference Optimization (DPO) is widely adopted for its computational efficiency and avoidance of explicit reward modeling, its applications to diffusion models have primarily relied on pairwise preferences. The precise optimization of listwise preferences remains largely unaddressed. In practice, human feedback on image preferences often contains implicit ranked information, which conveys more precise human preferences than pairwise comparisons. In this work, we propose Diffusion-LPO, a simple and effective framework for Listwise Preference Optimization in diffusion models with listwise data. Given a caption, we aggregate user feedback into a ranked list of images and derive a listwise extension of the DPO objective under the Plackett-Luce model. Diffusion-LPO enforces consistency across the entire ranking by encouraging each sample to be preferred over all of its lower-ranked alternatives. We empirically demonstrate the effectiveness of Diffusion-LPO across various tasks, including text-to-image generation, image editing, and personalized preference alignment. Diffusion-LPO consistently outperforms pairwise DPO baselines on visual quality and preference alignment.

