---
layout: default
title: LaX: Boosting Low-Rank Training of Foundation Models via Latent Crossing
---

# LaX: Boosting Low-Rank Training of Foundation Models via Latent Crossing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21732" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21732v2</a>
  <a href="https://arxiv.org/pdf/2505.21732.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21732v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21732v2', 'LaX: Boosting Low-Rank Training of Foundation Models via Latent Crossing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruijie Zhang, Ziyue Liu, Zhengyang Wang, Zheng Zhang

**分类**: cs.LG

**发布日期**: 2025-05-27 (更新: 2025-10-24)

---

## 💡 一句话要点

**提出LaX以提升基础模型低秩训练性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `低秩训练` `基础模型` `信息流动` `参数高效` `深度学习`

## 📋 核心要点

1. 现有的基础模型训练方法计算成本高，低秩分解虽然参数高效，但性能受限于参数空间。
2. LaX模块通过促进低秩子空间之间的信息流动，增强了低秩模型的表现能力，提供了一种有效的解决方案。
3. 实验结果表明，LaX在多个模型上显著提升了性能，使用的参数量却减少了2-3倍。

## 📝 摘要（中文）

训练基础模型（如ViTs和LLMs）需要巨大的计算成本。低秩矩阵或张量分解提供了一种参数高效的替代方案，但由于参数空间的限制，往往会降低性能。本文提出了Latent Crossing（LaX）——一个简单而有效的插件模块，通过促进低秩子空间之间的信息流动，增强低秩模型的能力。我们在ViT-Base/Large和LLaMA类模型的预训练任务中广泛验证了LaX的优势，结果显示，LaX使低秩模型的性能达到或超过全秩基线，同时使用2-3倍更少的参数。在对LLaMA-7/13B进行微调时，结合低秩适配器（如LoRA），LaX在算术和常识推理任务上始终提高了性能，且成本微乎其微。

## 🔬 方法详解

**问题定义**：本文旨在解决基础模型训练中的高计算成本问题。现有的低秩分解方法虽然参数高效，但由于参数空间的限制，往往导致模型性能下降。

**核心思路**：LaX模块通过允许低秩子空间之间的信息流动，增强了低秩模型的表达能力。这种设计使得模型在保持参数效率的同时，能够更好地捕捉复杂的特征。

**技术框架**：LaX模块可以作为一个插件集成到现有的低秩模型中。整体架构包括输入层、低秩分解层、LaX模块和输出层。LaX模块在低秩子空间之间建立连接，促进信息共享。

**关键创新**：LaX的主要创新在于其信息流动机制，通过跨越低秩子空间的连接，显著提升了模型的性能。这与传统低秩方法的局限性形成鲜明对比。

**关键设计**：在实现上，LaX模块的设计考虑了参数的高效性和信息流动的有效性。具体的参数设置和损失函数设计旨在最大化模型的表达能力，同时保持计算的高效性。实验中使用了ViT和LLaMA模型，验证了设计的有效性。

## 📊 实验亮点

实验结果显示，LaX在ViT-Base/Large和LLaMA类模型上，能够使低秩模型的性能达到或超过全秩基线，且参数使用量减少了2-3倍。在对LLaMA-7/13B进行微调时，LaX在算术和常识推理任务上均表现出显著的性能提升，且成本几乎可以忽略不计。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、计算机视觉等基础模型的训练和微调。通过降低计算成本并提升性能，LaX模块可以使得更广泛的研究者和开发者能够在资源有限的情况下，训练和应用大型基础模型，推动相关领域的进步。

## 📄 摘要（原文）

> Training foundation models such as ViTs and LLMs requires tremendous computing cost. Low-rank matrix or tensor factorization offers a parameter-efficient alternative, but often downgrades performance due to the restricted parameter space. In this work, we introduce {\textbf{Latent Crossing (LaX)}} -- a simple yet effective plug-and-play module that enhances the capacity of low-rank models by enabling information flow across low-rank subspaces. We extensively validate the benefits of LaX on pre-training tasks with ViT-Base/Large and LLaMA-like models ranging from 60M to 1B parameters. LaX boosts low-rank model performance to match or exceed the full-rank baselines while using 2-3\(\times\) fewer parameters. When equipped with low-rank adapters (i.e., LoRA) for fine-tuning LLaMA-7/13B, LaX consistently improves performance on arithmetic and common sense reasoning tasks with negligible cost.

