---
layout: default
title: LPOI: Listwise Preference Optimization for Vision Language Models
---

# LPOI: Listwise Preference Optimization for Vision Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21061" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21061v1</a>
  <a href="https://arxiv.org/pdf/2505.21061.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21061v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21061v1', 'LPOI: Listwise Preference Optimization for Vision Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fatemeh Pesaran Zadeh, Yoojin Oh, Gunhee Kim

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-27

**备注**: ACL 2025 Main. Code is released at https://github.com/fatemehpesaran310/lpoi

**🔗 代码/项目**: [GITHUB](https://github.com/fatemehpesaran310/lpoi)

---

## 💡 一句话要点

**提出LPOI以解决视觉语言模型中的幻觉问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉语言模型` `偏好优化` `幻觉现象` `对象感知` `多模态学习` `图像理解` `机器学习`

## 📋 核心要点

1. 现有的对齐视觉语言模型与人类偏好的方法存在过拟合文本信息和加剧幻觉的问题。
2. 本文提出LPOI，通过对象遮蔽和插值生成逐步完整的图像序列，训练模型按可见性排序，从而减少幻觉。
3. 在MMHalBench、AMBER和Object HalBench上的实验表明，LPOI在减少幻觉和提升模型性能方面显著优于现有方法。

## 📝 摘要（中文）

对齐大型视觉语言模型（VLMs）与人类偏好的任务具有挑战性，现有方法如RLHF和DPO常常过拟合文本信息或加剧幻觉现象。尽管增强负样本部分解决了这些问题，但尚无研究采用列表偏好优化方法。本文提出LPOI，这是首个针对VLMs的对象感知列表偏好优化方法，旨在减少幻觉。LPOI通过识别和遮蔽图像中的关键对象，并在正负样本之间插值形成逐步完整的图像序列，训练模型按对象可见性升序排列这些图像，从而有效降低幻觉并保持视觉保真度。实验结果表明，LPOI在减少幻觉和提升VLM性能方面优于现有方法。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉语言模型（VLMs）在对齐人类偏好时出现的幻觉现象。现有方法如RLHF和DPO往往过于依赖文本信息，导致模型在图像理解上出现偏差。

**核心思路**：LPOI的核心思路是通过对象遮蔽和插值技术，生成一系列逐步完整的图像，从而训练模型按对象可见性进行排序。这种方法能够有效减少幻觉，同时保持图像的视觉保真度。

**技术框架**：LPOI的整体架构包括三个主要模块：对象识别与遮蔽、图像插值生成和排序训练。首先，识别图像中的关键对象并进行遮蔽；然后，通过插值生成一系列图像；最后，训练模型对这些图像进行排序。

**关键创新**：LPOI的主要创新在于首次引入对象感知的列表偏好优化方法，解决了现有方法在构建列表样本时的复杂性和成本问题。与传统方法相比，LPOI无需额外的注释数据，自动生成排序列表。

**关键设计**：LPOI采用标准的成对偏好数据进行训练，设计了特定的损失函数来优化排序结果。关键参数包括遮蔽区域的选择和插值策略，这些设计确保了模型在减少幻觉的同时，保持图像的视觉质量。

## 📊 实验亮点

实验结果显示，LPOI在MMHalBench、AMBER和Object HalBench上显著优于现有的偏好优化方法，减少幻觉现象的同时，提升了模型性能。具体而言，LPOI在减少幻觉方面的提升幅度达到了XX%，在VLM性能评估中表现出色。

## 🎯 应用场景

LPOI的研究成果在多个领域具有广泛的应用潜力，尤其是在图像生成、图像理解和人机交互等领域。通过减少幻觉现象，LPOI可以提升视觉语言模型在实际应用中的可靠性和用户体验，未来可能推动更智能的多模态系统的发展。

## 📄 摘要（原文）

> Aligning large VLMs with human preferences is a challenging task, as methods like RLHF and DPO often overfit to textual information or exacerbate hallucinations. Although augmenting negative image samples partially addresses these pitfalls, no prior work has employed listwise preference optimization for VLMs, due to the complexity and cost of constructing listwise image samples. In this work, we propose LPOI, the first object-aware listwise preference optimization developed for reducing hallucinations in VLMs. LPOI identifies and masks a critical object in the image, and then interpolates the masked region between the positive and negative images to form a sequence of incrementally more complete images. The model is trained to rank these images in ascending order of object visibility, effectively reducing hallucinations while retaining visual fidelity. LPOI requires no extra annotations beyond standard pairwise preference data, as it automatically constructs the ranked lists through object masking and interpolation. Comprehensive experiments on MMHalBench, AMBER, and Object HalBench confirm that LPOI outperforms existing preference optimization methods in reducing hallucinations and enhancing VLM performance. We make the code available at https://github.com/fatemehpesaran310/lpoi.

