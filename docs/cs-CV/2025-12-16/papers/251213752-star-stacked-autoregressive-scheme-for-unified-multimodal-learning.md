---
layout: default
title: STAR: STacked AutoRegressive Scheme for Unified Multimodal Learning
---

# STAR: STacked AutoRegressive Scheme for Unified Multimodal Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13752" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13752</a>
  <a href="https://arxiv.org/pdf/2512.13752.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13752" onclick="toggleFavorite(this, '2512.13752', 'STAR: STacked AutoRegressive Scheme for Unified Multimodal Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jie Qin, Jiancheng Huang, Limeng Qiao, Lin Ma

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出STAR：堆叠自回归方案，用于统一多模态学习，提升生成性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `自回归模型` `生成模型` `图像编辑` `统一模型` `堆叠结构` `任务渐进学习`

## 📋 核心要点

1. 多模态大模型面临理解和生成任务间的优化冲突和性能权衡问题，难以兼顾。
2. STAR通过堆叠自回归模块，将多模态学习分解为理解、生成和编辑阶段，避免任务干扰。
3. 实验结果表明，STAR在GenEval、DPG-Bench和ImgEdit等基准测试中取得了领先性能。

## 📝 摘要（中文）

多模态大型语言模型（MLLM）在推动通用人工智能发展中起着关键作用。然而，由于优化冲突和性能权衡，实现多模态理解和生成的统一目标仍然具有挑战性。为了有效提升生成性能，同时保留现有的理解能力，我们提出了STAR：一种用于任务渐进式统一多模态学习的堆叠自回归方案。该方法将多模态学习分解为多个阶段：理解、生成和编辑。通过冻结基础自回归（AR）模型的参数并逐步堆叠同构AR模块，避免了跨任务干扰，同时扩展了模型的能力。此外，我们引入了高容量VQ以增强图像表示的粒度，并采用隐式推理机制来提高复杂条件下的生成质量。实验表明，STAR在GenEval（0.91）、DPG-Bench（87.44）和ImgEdit（4.34）上实现了最先进的性能，验证了其在统一多模态学习中的有效性。

## 🔬 方法详解

**问题定义**：多模态大型语言模型在统一多模态理解和生成方面面临挑战，主要痛点在于不同任务之间的优化冲突和性能权衡，导致模型难以同时提升理解和生成能力。现有方法往往顾此失彼，要么牺牲理解能力来提升生成性能，要么反之。

**核心思路**：STAR的核心思路是将多模态学习过程解耦为多个阶段，包括理解、生成和编辑，并采用堆叠自回归模块的方式，逐步扩展模型的能力。通过冻结基础自回归模型的参数，避免了跨任务的干扰，从而能够在提升生成性能的同时，保持现有的理解能力。

**技术框架**：STAR的技术框架主要包含三个阶段：理解阶段、生成阶段和编辑阶段。在理解阶段，模型利用预训练的自回归模型进行多模态信息的编码和理解。在生成阶段，模型通过堆叠额外的自回归模块，学习生成新的内容。在编辑阶段，模型可以对已生成的内容进行修改和完善。整个框架采用任务渐进式的学习方式，逐步提升模型的能力。

**关键创新**：STAR最重要的技术创新点在于其堆叠自回归模块的设计。通过冻结基础模型的参数，并逐步堆叠同构的自回归模块，避免了跨任务的干扰，从而能够在提升生成性能的同时，保持现有的理解能力。此外，高容量VQ和隐式推理机制也进一步提升了图像表示的粒度和生成质量。

**关键设计**：STAR的关键设计包括：1) 基础自回归模型的选择和参数冻结策略；2) 堆叠自回归模块的数量和结构；3) 高容量VQ的设计，用于增强图像表示的粒度；4) 隐式推理机制的实现，用于提高复杂条件下的生成质量。具体的参数设置和损失函数等细节在论文中进行了详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13752/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13752/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13752/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

STAR在GenEval、DPG-Bench和ImgEdit等多个基准测试中取得了显著的性能提升。具体而言，在GenEval上达到了0.91的得分，在DPG-Bench上达到了87.44的得分，在ImgEdit上达到了4.34的得分。这些结果表明，STAR在统一多模态学习方面具有显著的优势，能够有效提升生成性能，同时保持现有的理解能力。

## 🎯 应用场景

STAR具有广泛的应用前景，可应用于智能对话、图像生成、视频编辑等领域。例如，可以利用STAR构建更强大的多模态对话系统，实现更自然、更流畅的人机交互。此外，STAR还可以用于生成高质量的图像和视频内容，为创意设计和内容创作提供支持。未来，STAR有望成为通用人工智能的重要组成部分。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) play a pivotal role in advancing the quest for general artificial intelligence. However, achieving unified target for multimodal understanding and generation remains challenging due to optimization conflicts and performance trade-offs. To effectively enhance generative performance while preserving existing comprehension capabilities, we introduce STAR: a STacked AutoRegressive scheme for task-progressive unified multimodal learning. This approach decomposes multimodal learning into multiple stages: understanding, generation, and editing. By freezing the parameters of the fundamental autoregressive (AR) model and progressively stacking isomorphic AR modules, it avoids cross-task interference while expanding the model's capabilities. Concurrently, we introduce a high-capacity VQ to enhance the granularity of image representations and employ an implicit reasoning mechanism to improve generation quality under complex conditions. Experiments demonstrate that STAR achieves state-of-the-art performance on GenEval (0.91), DPG-Bench (87.44), and ImgEdit (4.34), validating its efficacy for unified multimodal learning.

