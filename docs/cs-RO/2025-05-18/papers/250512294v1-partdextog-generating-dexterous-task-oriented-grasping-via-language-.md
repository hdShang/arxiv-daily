---
layout: default
title: "PartDexTOG: Generating Dexterous Task-Oriented Grasping via Language-driven Part Analysis"
---

# PartDexTOG: Generating Dexterous Task-Oriented Grasping via Language-driven Part Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12294" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12294v1</a>
  <a href="https://arxiv.org/pdf/2505.12294.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12294v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12294v1', 'PartDexTOG: Generating Dexterous Task-Oriented Grasping via Language-driven Part Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weishang Wu, Yifei Shi, Zhizhong Chen, Zhipong Cai

**分类**: cs.RO

**发布日期**: 2025-05-18

---

## 💡 一句话要点

**提出PartDexTOG以解决灵巧任务导向抓取问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱四：生成式动作 (Generative Motion)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `灵巧抓取` `任务导向` `部件分析` `条件扩散模型` `机器人操作` `语言驱动` `几何一致性`

## 📋 核心要点

1. 现有方法在灵巧手的任务导向抓取方面存在不足，缺乏对物体功能的深入分析。
2. 提出的PartDexTOG方法通过语言驱动的部件分析生成灵巧抓取，提升了抓取的精度与适应性。
3. 在OakInk-shape数据集上，PartDexTOG方法在多个指标上超越了现有最优方法，显示出良好的通用性。

## 📝 摘要（中文）

任务导向抓取是机器人操作中的一个关键而具有挑战性的任务。尽管近年来取得了一些进展，但现有方法很少关注灵巧手的任务导向抓取。灵巧手提供了更好的精度和多功能性，使机器人能够更有效地执行任务导向抓取。本文提出PartDexTOG方法，通过语言驱动的部件分析生成灵巧的任务导向抓取。该方法以3D物体和通过语言表示的操作任务为输入，首先生成与操作任务相关的类别级和部件级抓取描述。然后，开发了一种类别-部件条件扩散模型，基于生成的描述分别为每个部件生成灵巧抓取。通过几何一致性度量选择最合理的抓取和相应部件组合。实验表明，该方法在处理不同几何形状和操作任务的物体时，受益于LLMs对物体部件的开放世界知识推理，且在OakInk-shape数据集上表现优异，超越了所有现有方法。

## 🔬 方法详解

**问题定义**：本文旨在解决灵巧手在任务导向抓取中的应用问题，现有方法未能充分利用物体部件的功能信息，导致抓取效果不理想。

**核心思路**：通过语言驱动的部件分析，PartDexTOG方法能够生成与操作任务相关的抓取描述，从而为每个部件生成灵巧抓取，提升抓取的准确性和灵活性。

**技术框架**：该方法首先接收3D物体和操作任务的语言描述，利用大型语言模型（LLMs）生成抓取描述，然后通过类别-部件条件扩散模型为每个部件生成抓取，最后通过几何一致性度量选择最佳抓取组合。

**关键创新**：PartDexTOG的创新在于结合了语言驱动的部件分析与条件扩散模型，显著提升了灵巧抓取的生成能力，与传统方法相比，能够更好地适应不同几何形状和操作任务。

**关键设计**：模型中使用了几何一致性度量作为选择抓取组合的标准，确保生成的抓取在物理上可行。此外，采用了特定的损失函数来优化抓取的精度和稳定性。

## 📊 实验亮点

在OakInk-shape数据集上，PartDexTOG方法在渗透体积、抓取位移和P-FID等指标上分别提升了3.58%、2.87%和41.43%，显示出其在灵巧抓取任务中的显著优势，且在处理新类别和任务时表现出良好的通用性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人抓取、自动化仓储、智能家居等。通过提升灵巧手的抓取能力，能够显著提高机器人在复杂环境中的操作效率，具有重要的实际价值和广泛的市场前景。

## 📄 摘要（原文）

> Task-oriented grasping is a crucial yet challenging task in robotic manipulation. Despite the recent progress, few existing methods address task-oriented grasping with dexterous hands. Dexterous hands provide better precision and versatility, enabling robots to perform task-oriented grasping more effectively. In this paper, we argue that part analysis can enhance dexterous grasping by providing detailed information about the object's functionality. We propose PartDexTOG, a method that generates dexterous task-oriented grasps via language-driven part analysis. Taking a 3D object and a manipulation task represented by language as input, the method first generates the category-level and part-level grasp descriptions w.r.t the manipulation task by LLMs. Then, a category-part conditional diffusion model is developed to generate a dexterous grasp for each part, respectively, based on the generated descriptions. To select the most plausible combination of grasp and corresponding part from the generated ones, we propose a measure of geometric consistency between grasp and part. We show that our method greatly benefits from the open-world knowledge reasoning on object parts by LLMs, which naturally facilitates the learning of grasp generation on objects with different geometry and for different manipulation tasks. Our method ranks top on the OakInk-shape dataset over all previous methods, improving the Penetration Volume, the Grasp Displace, and the P-FID over the state-of-the-art by $3.58\%$, $2.87\%$, and $41.43\%$, respectively. Notably, it demonstrates good generality in handling novel categories and tasks.

