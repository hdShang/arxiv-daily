---
layout: default
title: QE-Catalytic: A Graph-Language Multimodal Base Model for Relaxed-Energy Prediction in Catalytic Adsorption
---

# QE-Catalytic: A Graph-Language Multimodal Base Model for Relaxed-Energy Prediction in Catalytic Adsorption

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20084" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20084v1</a>
  <a href="https://arxiv.org/pdf/2512.20084.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20084v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20084v1', 'QE-Catalytic: A Graph-Language Multimodal Base Model for Relaxed-Energy Prediction in Catalytic Adsorption')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanjie Li, Jian Xu, Xueqing Chen, Lina Yu, Shiming Xiang, Weijun Li, Cheng-lin Liu

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-23

**备注**: 25 pages

---

## 💡 一句话要点

**提出QE-Catalytic，融合图和语言模型，提升催化吸附中弛豫能量预测精度。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `催化吸附` `能量预测` `图神经网络` `语言模型` `多模态融合` `逆向设计` `E(3)-等变性`

## 📋 核心要点

1. 现有方法在催化吸附能量预测中，基于语言模型的方法精度不足，无法有效区分不同构型的相同系统。
2. QE-Catalytic通过深度耦合大型语言模型和E(3)-等变图Transformer，实现对吸附构型属性的统一预测和逆向设计。
3. 实验结果表明，QE-Catalytic在OC20数据集上显著降低了弛豫吸附能的MAE，优于现有基线模型。

## 📝 摘要（中文）

吸附能是催化反应活性的关键描述符。它从根本上定义为吸附质-表面系统的弛豫总能量与适当参考状态之间的差值；因此，弛豫能量预测的准确性直接决定了机器学习驱动的催化剂筛选的可靠性。E(3)-等变图神经网络(GNNs)可以在周期性边界条件下自然地处理三维原子坐标，并在该任务上表现出强大的性能。相比之下，基于语言模型的方法虽然能够实现人类可读的文本描述并减少对显式图的依赖——从而扩大了适用性——但在吸附构型能量预测精度和区分“具有不同构型的相同系统”方面仍然不足，即使采用类似于GAP-CATBERTa的图辅助预训练也是如此。为此，我们提出了QE-Catalytic，一个多模态框架，它将大型语言模型(Qwen)与E(3)-等变图Transformer(Equiformer-V2)深度耦合，从而能够统一支持复杂催化表面上的吸附构型属性预测和逆向设计。在预测过程中，QE-Catalytic联合利用三维结构和结构化构型文本，并通过图-文本对齐将“3D几何信息”注入到语言通道中，使其在没有精确坐标时也能作为高性能的基于文本的预测器发挥作用，同时还能自回归地生成用于目标能量驱动的结构设计和信息补全的CIF文件。在OC20上，QE-Catalytic将弛豫吸附能的MAE从0.713 eV降低到0.486 eV，并且在多个评估协议中始终优于CatBERTa和GAP-CATBERTa等基线模型。

## 🔬 方法详解

**问题定义**：论文旨在解决催化吸附过程中弛豫能量预测的准确性问题。现有基于语言模型的方法，即使经过图辅助预训练，在预测吸附构型能量和区分不同构型的相同系统方面仍然存在不足，限制了催化剂筛选的可靠性。

**核心思路**：论文的核心思路是将大型语言模型与E(3)-等变图Transformer深度耦合，构建一个多模态框架。通过图-文本对齐，将三维几何信息注入到语言通道中，使得模型既能利用结构信息，也能利用文本描述，从而提高预测精度和泛化能力。

**技术框架**：QE-Catalytic框架包含两个主要模块：大型语言模型（Qwen）和E(3)-等变图Transformer（Equiformer-V2）。该框架首先利用Equiformer-V2处理三维原子结构，提取几何特征。然后，将结构化的构型文本输入到Qwen中进行处理。通过图-文本对齐机制，将Equiformer-V2提取的几何特征注入到Qwen中，实现多模态信息的融合。最后，利用融合后的信息进行弛豫能量预测，并支持自回归生成CIF文件进行结构设计。

**关键创新**：该论文的关键创新在于多模态融合框架的设计，特别是图-文本对齐机制。通过将E(3)-等变图Transformer与大型语言模型深度耦合，实现了三维结构信息和文本信息的有效融合，克服了传统方法中仅依赖单一模态信息的局限性。此外，该框架还支持自回归生成CIF文件，为催化剂的逆向设计提供了新的途径。

**关键设计**：QE-Catalytic的关键设计包括：1）选择Qwen作为大型语言模型，利用其强大的文本处理能力；2）选择Equiformer-V2作为图神经网络，利用其E(3)-等变性处理三维原子结构；3）设计图-文本对齐机制，将几何信息注入到语言通道中；4）采用合适的损失函数进行模型训练，优化预测精度。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20084v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20084v1/hamap.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20084v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

QE-Catalytic在OC20数据集上取得了显著的性能提升，将弛豫吸附能的MAE从0.713 eV降低到0.486 eV，超越了CatBERTa和GAP-CATBERTa等基线模型。这表明该方法在催化吸附能量预测方面具有优越的性能和潜力。

## 🎯 应用场景

QE-Catalytic在催化剂设计与筛选领域具有广泛的应用前景。它可以用于预测各种催化材料的吸附能，加速新型催化剂的发现。此外，其逆向设计能力可以帮助研究人员根据目标能量需求，自动生成具有特定结构的催化材料，极大地提高催化剂研发效率。

## 📄 摘要（原文）

> Adsorption energy is a key descriptor of catalytic reactivity. It is fundamentally defined as the difference between the relaxed total energy of the adsorbate-surface system and that of an appropriate reference state; therefore, the accuracy of relaxed-energy prediction directly determines the reliability of machine-learning-driven catalyst screening. E(3)-equivariant graph neural networks (GNNs) can natively operate on three-dimensional atomic coordinates under periodic boundary conditions and have demonstrated strong performance on such tasks. In contrast, language-model-based approaches, while enabling human-readable textual descriptions and reducing reliance on explicit graph -- thereby broadening applicability -- remain insufficient in both adsorption-configuration energy prediction accuracy and in distinguishing ``the same system with different configurations,'' even with graph-assisted pretraining in the style of GAP-CATBERTa.
>   To this end, we propose QE-Catalytic, a multimodal framework that deeply couples a large language model (\textbf{Q}wen) with an E(3)-equivariant graph Transformer (\textbf{E}quiformer-V2), enabling unified support for adsorption-configuration property prediction and inverse design on complex catalytic surfaces. During prediction, QE-Catalytic jointly leverages three-dimensional structures and structured configuration text, and injects ``3D geometric information'' into the language channel via graph-text alignment, allowing it to function as a high-performance text-based predictor when precise coordinates are unavailable, while also autoregressively generating CIF files for target-energy-driven structure design and information completion. On OC20, QE-Catalytic reduces the MAE of relaxed adsorption energy from 0.713~eV to 0.486~eV, and consistently outperforms baseline models such as CatBERTa and GAP-CATBERTa across multiple evaluation protocols.

