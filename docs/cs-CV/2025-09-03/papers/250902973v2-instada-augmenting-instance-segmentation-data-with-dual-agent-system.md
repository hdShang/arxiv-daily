---
layout: default
title: "InstaDA: Augmenting Instance Segmentation Data with Dual-Agent System"
---

# InstaDA: Augmenting Instance Segmentation Data with Dual-Agent System

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02973" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02973v2</a>
  <a href="https://arxiv.org/pdf/2509.02973.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02973v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02973v2', 'InstaDA: Augmenting Instance Segmentation Data with Dual-Agent System')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xianbao Hou, Yonghao He, Zeyd Boukhers, John See, Hu Su, Wei Sui, Cong Yang

**分类**: cs.CV

**发布日期**: 2025-09-03 (更新: 2025-11-25)

---

## 💡 一句话要点

**InstaDA：利用双Agent系统增强实例分割数据，无需训练。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `实例分割` `数据增强` `大型语言模型` `扩散模型` `双Agent系统`

## 📋 核心要点

1. 实例分割数据标注成本高昂，且数据集存在严重的类别不平衡问题，限制了模型性能。
2. InstaDA采用双Agent系统，通过文本Agent和图像Agent协同工作，无需训练即可增强实例分割数据集。
3. 实验表明，InstaDA在LVIS 1.0验证集上显著提升了实例分割性能，优于现有领先模型DiverGen。

## 📝 摘要（中文）

高质量实例分割数据的获取面临标注工作量大和数据集类别不平衡的挑战。本文提出InstaDA，一种新颖的、无需训练的双Agent系统，用于增强实例分割数据集。该系统包含一个文本Agent (T-Agent)，通过大型语言模型(LLM)和扩散模型的协作来增强数据多样性，并引入Prompt Rethink机制迭代优化提示词。同时，一个图像Agent (I-Agent)通过生成以训练图像为条件的新实例来丰富数据分布。两个Agent独立且自动运行，提升了可用性。在LVIS 1.0验证集上的实验表明，InstaDA相比基线模型，在box AP上提升了+4.0，mask AP上提升了+3.3，并且优于DiverGen模型，在常见类别上的box AP提升了+0.7，mask AP提升了+0.2，在频繁类别上的mask AP提升了+0.5。

## 🔬 方法详解

**问题定义**：实例分割任务中，高质量标注数据的获取成本高昂，特别是对于长尾分布的数据集，类别不平衡问题严重。现有方法如Copy-Paste和扩散模型在数据增强方面取得了一定进展，但缺乏LLM和扩散模型之间的深度协作，且未能充分利用现有训练数据中的信息。

**核心思路**：InstaDA的核心在于构建一个双Agent系统，分别从文本和图像两个维度增强数据。文本Agent利用LLM和扩散模型生成多样化的图像，图像Agent则基于现有训练图像生成新的实例，从而丰富数据集的整体分布。这种双管齐下的策略旨在更有效地利用现有数据，并生成更具多样性的合成数据。

**技术框架**：InstaDA包含两个主要模块：文本Agent (T-Agent) 和图像Agent (I-Agent)。T-Agent首先利用LLM生成描述场景的文本提示，然后使用扩散模型根据提示生成图像。Prompt Rethink机制迭代地根据生成的图像反馈优化提示，提升图像质量和多样性。I-Agent则以训练图像为条件，生成新的实例并将其添加到训练集中。两个Agent独立运行，形成一个自动化的数据增强流程。

**关键创新**：InstaDA的关键创新在于Prompt Rethink机制和双Agent协同。Prompt Rethink机制通过迭代优化提示，实现了LLM和扩散模型之间的深度协作，提高了图像生成质量。双Agent系统则从文本和图像两个维度增强数据，更全面地解决了数据多样性和类别不平衡问题。与现有方法相比，InstaDA无需训练，更易于部署和使用。

**关键设计**：T-Agent中的Prompt Rethink机制涉及LLM对生成图像的分析和反馈，并基于此调整提示。I-Agent的实现细节包括如何选择合适的训练图像作为条件，以及如何生成逼真的新实例。具体的参数设置和损失函数选择取决于所使用的LLM和扩散模型。

## 📊 实验亮点

InstaDA在LVIS 1.0验证集上取得了显著的性能提升。相比于基线模型，InstaDA在box AP上提升了+4.0，mask AP上提升了+3.3。更重要的是，InstaDA超越了现有的领先模型DiverGen，在常见类别上的box AP提升了+0.7，mask AP提升了+0.2，在频繁类别上的mask AP提升了+0.5。这些结果表明InstaDA在提升实例分割性能方面的有效性。

## 🎯 应用场景

InstaDA可广泛应用于实例分割任务的数据增强，尤其适用于标注数据稀缺或类别不平衡的场景。例如，在自动驾驶、医疗影像分析、遥感图像处理等领域，可以利用InstaDA生成更多样化的训练数据，提升模型的泛化能力和鲁棒性。该方法无需训练，易于集成到现有实例分割流程中，具有很高的实用价值。

## 📄 摘要（原文）

> Acquiring high-quality instance segmentation data is challenging due to the labor-intensive nature of the annotation process and significant class imbalances within datasets. Recent studies have utilized the integration of Copy-Paste and diffusion models to create more diverse datasets. However, these studies often lack deep collaboration between large language models (LLMs) and diffusion models, and underutilize the rich information within the existing training data. To address these limitations, we propose InstaDA, a novel, training-free Dual-Agent system designed to augment instance segmentation datasets. First, we introduce a Text-Agent (T-Agent) that enhances data diversity through collaboration between LLMs and diffusion models. This agent features a novel Prompt Rethink mechanism, which iteratively refines prompts based on the generated images. This process not only fosters collaboration but also increases image utilization and optimizes the prompts themselves. Additionally, we present an Image-Agent (I-Agent) aimed at enriching the overall data distribution. This agent augments the training set by generating new instances conditioned on the training images. To ensure practicality and efficiency, both agents operate as independent and automated workflows, enhancing usability. Experiments conducted on the LVIS 1.0 validation set indicate that InstaDA achieves significant improvements, with an increase of +4.0 in box average precision (AP) and +3.3 in mask AP compared to the baseline. Furthermore, it outperforms the leading model, DiverGen, by +0.3 in box AP and +0.1 in mask AP, with a notable +0.7 gain in box AP on common categories and mask AP gains of +0.2 on common categories and +0.5 on frequent categories.

