---
layout: default
title: "STAR: Learning Diverse Robot Skill Abstractions through Rotation-Augmented Vector Quantization"
---

# STAR: Learning Diverse Robot Skill Abstractions through Rotation-Augmented Vector Quantization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.03863" class="toolbar-btn" target="_blank">📄 arXiv: 2506.03863v2</a>
  <a href="https://arxiv.org/pdf/2506.03863.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.03863v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.03863v2', 'STAR: Learning Diverse Robot Skill Abstractions through Rotation-Augmented Vector Quantization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Li, Qi Lv, Rui Shao, Xiang Deng, Yinchuan Li, Jianye Hao, Liqiang Nie

**分类**: cs.RO, cs.LG

**发布日期**: 2025-06-04 (更新: 2025-06-11)

**备注**: Accepted by ICML 2025 Spotlight

**期刊**: Proceedings of the 42st International Conference on Machine Learning, PMLR 267, 2025

---

## 💡 一句话要点

**提出STAR框架以解决机器人技能抽象中的代码本崩溃问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `机器人技能学习` `技能抽象` `旋转增强` `因果建模` `自回归机制` `VQ-VAE` `复杂行为生成` `机器人操作`

## 📋 核心要点

1. 现有方法在学习技能抽象时容易出现代码本崩溃，且难以建模技能之间的因果关系。
2. 本文提出STAR框架，通过旋转增强残差技能量化和因果技能变换器来解决上述问题。
3. 实验结果显示，STAR在LIBERO基准和实际任务中表现优异，相较于基线提升约12%。

## 📝 摘要（中文）

将复杂动作转化为离散技能抽象在机器人操作中展现出强大的潜力。现有方法主要依赖潜变量模型（如VQ-VAE）通过学习向量（代码本）来学习技能抽象，但面临代码本崩溃和技能间因果关系建模的挑战。为了解决这些问题，本文提出了技能训练与增强旋转（STAR）框架，推动了技能学习和组合以完成复杂行为。具体而言，本文设计了旋转增强残差技能量化（RaRSQ），通过基于旋转的梯度机制将编码器输出间的相对角度编码到梯度流中，从而防止代码本崩溃。此外，提出的因果技能变换器（CST）通过自回归机制显式建模技能表示之间的依赖关系，以实现连贯的动作生成。实验结果表明，STAR在LIBERO基准和真实世界任务上均优于基线，提升约12%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有技能抽象方法中的代码本崩溃问题，以及技能间因果关系建模的不足。现有方法如VQ-VAE在技能学习中存在一定的局限性，导致技能表示不够稳定和连贯。

**核心思路**：论文提出的STAR框架通过引入旋转增强残差技能量化（RaRSQ）和因果技能变换器（CST）来增强技能学习的稳定性和连贯性。RaRSQ通过旋转机制优化梯度流，CST则通过自回归机制建模技能间的依赖关系。

**技术框架**：STAR框架主要包括两个模块：RaRSQ和CST。RaRSQ负责技能的量化与编码，确保技能表示的多样性；CST则负责生成连贯的动作序列，确保技能之间的因果关系得到有效建模。

**关键创新**：STAR的核心创新在于引入旋转增强机制和因果建模机制，前者有效防止了代码本崩溃，后者则提升了技能间的连贯性和可组合性。这与传统方法的设计思路有本质区别。

**关键设计**：在RaRSQ中，设计了基于旋转的梯度机制，通过调整技能代码间的相对位置来优化技能表示；在CST中，采用自回归模型来捕捉技能间的依赖关系，确保生成的动作序列具有逻辑一致性。

## 📊 实验亮点

实验结果表明，STAR在LIBERO基准和真实世界任务中均表现优异，相较于基线提升约12%。这一显著提升证明了STAR框架在技能学习和组合方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人操作、自动化制造和智能家居等。通过提升机器人技能学习的效率和准确性，STAR框架能够在复杂环境中实现更高效的任务执行，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Transforming complex actions into discrete skill abstractions has demonstrated strong potential for robotic manipulation. Existing approaches mainly leverage latent variable models, e.g., VQ-VAE, to learn skill abstractions through learned vectors (codebooks), while they suffer from codebook collapse and modeling the causal relationship between learned skills. To address these limitations, we present \textbf{S}kill \textbf{T}raining with \textbf{A}ugmented \textbf{R}otation (\textbf{STAR}), a framework that advances both skill learning and composition to complete complex behaviors. Specifically, to prevent codebook collapse, we devise rotation-augmented residual skill quantization (RaRSQ). It encodes relative angles between encoder outputs into the gradient flow by rotation-based gradient mechanism. Points within the same skill code are forced to be either pushed apart or pulled closer together depending on gradient directions. Further, to capture the causal relationship between skills, we present causal skill transformer (CST) which explicitly models dependencies between skill representations through an autoregressive mechanism for coherent action generation. Extensive experiments demonstrate the superiority of STAR on both LIBERO benchmark and realworld tasks, with around 12\% improvement over the baselines.

